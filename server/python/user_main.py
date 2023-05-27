from flask import Flask, jsonify, request
# nicer exception for HTTP
from werkzeug.exceptions import BadRequest, InternalServerError
from user import User

app = Flask(__name__)

user = User(
    "Emina",
    "Ergul",
    "emina.ergul@example.com",
    "+1234567890",
    "1990-01-01",
    "123 Main Street, City, Country",
    "password123",
)


@app.route("/users/", methods=["GET"])
def get_all_users():
    print(User.get_users())
    return jsonify(User.get_users())


@app.route("/user/<u_id>", methods=["GET"])
def get_user_by_id(u_id):
    return jsonify(User.get_user_by_id(u_id))


@app.route("/register", methods=["POST"])
def register():
    # deal with input payload
    try:
        data = request.json
        user_exist = user.does_user_exist(data)
        print(user_exist)
        if user_exist:
            return 'A User with this Email Exists'
        user.add_user(data)
        return f'{request}'
    except Exception as exc:
        raise InternalServerError(f"Failed: {exc}")


@app.route("/remove-user/", methods=["DELETE"])
def remove_user():
    # deal with input payload
    try:
        data = request.json
        print(data)
        user.remove_user(data)
        return f'{request}'
    except Exception as exc:
        raise InternalServerError(f"Failed: {exc}")


if __name__ == '__main__':
    app.run(debug=True)
