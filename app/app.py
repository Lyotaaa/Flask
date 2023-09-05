from flask import Flask, jsonify
from flask import MethodView
from errors import HttpError
from views import AdsView

app = Flask("app")


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    response = jsonify({
        "status": "error",
        "message": error.message,
    })
    response.status_code = error.status_code
    return response


app.add_url_rule("/user/<int:user_id>",
                 view_func=AdsView,
                 methods=["GET", "PATCH", "DELETE"]
                 )
app.add_url_rule("/user/",
                 view_func=AdsView,
                 methods=["POST"]
                 )

if __name__ == "__main__":
    app.run()
