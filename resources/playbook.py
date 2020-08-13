from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import subprocess

playbooks = [
    {
        'name': 'site.yml'
    }
]

inventories = [
    {
        "name": "invenory"
    }
]

class Playbook(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument('inventory',
            type=str,
            required=False,
            help='This field cannot be left blank'  
    )

    def get(self, name):
        playbook = next(filter(lambda x: x['name'] == name, playbooks),None)
        return {'playbook': playbook}, 404

    @jwt_required()
    def post(self, name):
        data = Playbook.parser.parse_args()
        playbook_details = {'name': name, 'inventory': data['inventory']}
        # inventory = request_data['inventory']
        # print(inventory)
        p1 = subprocess.run(
            ['ansible-playbook', '-i', '{}'.format(playbook_details['inventory']), '{}'.format(playbook_details['name'])],
            capture_output=True,
            text=True
        )

        
        if p1.returncode == 0:  
            return {"messege": "Success", "output" : p1.stdout}
        else:
            return {"messege": "fail", "output": p1.stdout}


class PlaybookList(Resource):

    def get(self):
        return {"playbboks": playbooks}
