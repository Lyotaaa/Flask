import flask
from flask import jsonify, request
from flask import MethodView

app = flask.Flask("app")

class AdsView(MethodView):

    def get(self):
        pass

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass









if __name__ == "__main__":
    app.run()