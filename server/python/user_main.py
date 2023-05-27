from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest, InternalServerError  # nicer exception for HTTP
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



if __name__ == '__main__':
    app.run(debug=True)
