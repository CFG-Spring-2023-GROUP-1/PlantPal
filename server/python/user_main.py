from flask import Flask, Blueprint, jsonify, request
# nicer exception for HTTP
from werkzeug.exceptions import BadRequest, InternalServerError
from user import User

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route("/users/", methods=["GET"])
def get_all_users():
    print(User.get_users())
    return jsonify({'user': User.get_users(), 'message': 'Users Fetched Succesfully'}), 200


@user_blueprint.route("/user/<u_id>", methods=["GET"])
def get_user_by_id(u_id):
    return jsonify({'user': User.get_user_by_id(u_id), 'message': 'User Fetched Succesfully'}), 200


@user_blueprint.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        user = User(
            data["FirstName"],
            data["LastName"],
            data["Email"],
            data["PhoneNo"],
            data["Dob"],
            data["Address"],
            data["Password"],
        )
        user_exist = user.does_user_exist(data)
        if user_exist:
            return 'A User with this Email Exists'
        user.add_user(data)
        return jsonify({'message': 'User Added Succesfully', 'user': data}), 200
    except Exception as exc:
        raise InternalServerError(f"Failed: {exc}")


@user_blueprint.route("/remove-user/", methods=["DELETE"])
def remove_user():
    try:
        data = request.json
        print(data)
        User.remove_user(data)
        return f'{request}'
    except Exception as exc:
        raise InternalServerError(f"Failed: {exc}")


# if __name__ == '__main__':
#     user_blueprint.run(debug=True)
