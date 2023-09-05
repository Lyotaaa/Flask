from flask import Flask, jsonify
from errors import HttpError
from views import OwnerView

app = Flask("app")


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    response = jsonify(
        {
            "status": "error",
            "message": error.message,
        }
    )
    response.status_code = error.status_code
    return response


app.add_url_rule(
    "/owner/<int:owner_id>",
    view_func=OwnerView.as_view("owner"),
    methods=["GET", "PATCH", "DELETE"],
)
app.add_url_rule(
    "/owner/", view_func=OwnerView.as_view("create_owner"), methods=["POST"]
)

if __name__ == "__main__":
    app.run()
