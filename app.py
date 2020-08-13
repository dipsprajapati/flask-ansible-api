from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, idendity
from resources.user import UserRegister
from resources.playbook import Playbook, PlaybookList
from resources.adhoc_cmd import AdhocCmd
from db import db
# from item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'dipesh'
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app, authenticate, idendity) #auth


api.add_resource(Playbook, '/playbook/<string:name>')
api.add_resource(PlaybookList, '/playbooks')
api.add_resource(AdhocCmd, '/adhoc')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)






