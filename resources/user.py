import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help='This field cannot be left blank')

    parser.add_argument('password',
            type=str,
            required=True,
            help='This field cannot be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"messege": "A user with the username already exists"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {'messege': 'user created successfully'}, 201