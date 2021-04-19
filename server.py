import os
from bottle import route, run
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration
from config import sentry_token
sentry_sdk.init(
   dsn=sentry_token,
   integrations=[BottleIntegration()]
)
@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Проверка запросов и логирования через sentry</title>
  </head>
  <body>
    <div class="container">
      <h1>попробуй маршрут /success который вернет запрос - Статус 200, все ок!</h1>
      <h1>попробуй маршрут /fail который вернет запрос - Который вернет 500 Error!</h1>
    </div>
  </body>
</html>
"""
    return html

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
