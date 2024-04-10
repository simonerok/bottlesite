from bottle import default_app, get, post, response, run, static_file, template
import x
from icecream import ic
import bcrypt

##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")

##############################
@get("/images/<item_splash_image>")
def _(item_splash_image):
    return static_file(item_splash_image, "images")

##############################
@get("/")
def _():
    try:
        db = x.db()
        q = db.execute("SELECT * FROM items LIMIT 0, 3")
        items = q.fetchall()
        ic(items)
        return template("index.html", items=items)
    except Exception as ex:
        ic(ex)
        return "ups..."
    finally:
        if "db" in locals(): db.close()

##############################
@get("/login")
def _():
    return template("login.html")


##############################
@get("/api")
def _():
    return x.test()


##############################
##############################
##############################
@post("/signup")
def _():
    # password = b'password'
    # # Adding the salt to password
    # salt = bcrypt.gensalt()
    # # Hashing the password
    # hashed = bcrypt.hashpw(password, salt)
    # # printing the salt
    # print("Salt :")
    # print(salt)
    
    # # printing the hashed
    # print("Hashed")
    # print(hashed)    
    return "signup"


##############################
@post("/login")
def _():
    try:
        user_email = x.validate_email()
        user_password = x.validate_password()
        db = x.db()
        q = db.execute("SELECT * FROM users WHERE user_email = ? LIMIT 1", (user_email,))
        user = q.fetchone()
        if not user: raise Exception("user not found", 400)
        if not bcrypt.checkpw(user_password.encode(), user["user_password"].encode()): raise Exception("Invalid credentials", 400)
        user.pop("user_password") # Do not put the user's password in the cookie
        ic(user)
        try:
            import production
            is_cookie_https = True
        except:
            is_cookie_https = False        
        response.set_cookie("user", user, secret=x.COOKIE_SECRET, httponly=True, secure=is_cookie_https)
        return """
        <template mix-redirect="/profile">
        </template>
        """
    except Exception as ex:
        try:
            response.status = ex.args[1]
            return ex.args[0]
        except Exception as ex:
            ic(ex)
            response.status = 500
            return "ups..."

    finally:
        if "db" in locals(): db.close()



##############################
try:
    import production
    application = default_app()
except:
    run(host="0.0.0.0", port=80, debug=True, reloader=True, interval=0)








