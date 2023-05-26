from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest, InternalServerError  # nicer exception for HTTP
from user import User

app = Flask(__name__)


@app.route("/users/", methods=["GET"])
def get_all_users():
    return jsonify(User.get_users())


@app.route("/user/<u_id>", methods=["GET", "DELETE"])
def get_user_by_id(u_id):
    try:
        if request.method == "GET":
            return jsonify(User.get_user_by_id(u_id))
        elif request.method == "DELETE":
            User.remove_user(u_id)
            return f'{u_id} removed successfully'
    except Exception as exc:
        raise InternalServerError(f"Failed: {exc}")


@app.route("/register", methods=["POST"])
def register():
    # deal with input payload
    try:
        data = request.json
        user_exist = user.does_user_exist(data)
        if user_exist:
            return 'A User with this Email Exists'
        user.add_user(data)
        return f'{request}'
    except Exception as exc:
        raise InternalServerError(f"Failed: {exc}")


@app.route("/login", methods=["POST"])
def login():
    # deal with input payload
    try:
        data = request.json
        user.login(data)
        return f'{data}'
    except Exception as exc:
        raise InternalServerError(f"Failed: {exc}")


if __name__ == '__main__':
    app.run(debug=True)
