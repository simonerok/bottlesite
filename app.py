from bottle import default_app, get, run, static_file, template
from icecream import ic

# https://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@github.com/santiagodonoso/bottlesite.git

##############################
@get("/")
def _():
    return template("index")


##############################
try:
    # import production
    run(host="0.0.0.0", port=80, debug=True, reloader=True, interval=0)
except:
    application = default_app()








