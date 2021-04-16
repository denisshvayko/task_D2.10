import os
from bottle import route, run
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
   dsn="https://876d118550ae4980968d23c2304c8949@o571003.ingest.sentry.io/5723290",
   integrations=[BottleIntegration()]
)


@route("/success")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Проверка запроса</title>
  </head>
  <body>
    <div class="container">
      <h1>Статус 200, все ок!</h1>
    </div>
  </body>
</html>
"""
    return html


@route("/fail")
def index():
    raise RuntimeError("There is an error!")


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
