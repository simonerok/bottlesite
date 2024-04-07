try:
    import production
    from bottlesite.bottle  import default_app, get, run, static_file
except:
    from bottle             import default_app, get, run, static_file

# https://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@github.com/santiagodonoso/bottlesite.git

##############################
@get("/")
def _():
    return [{"name":"one"}]


##############################
try:
    import production
    application = default_app()
except:
    run(host="0.0.0.0", port=80, debug=True, reloader=True, interval=0)








