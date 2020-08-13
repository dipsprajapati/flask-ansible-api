from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import subprocess

class AdhocCmd(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument(
        'inventory',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )

    parser.add_argument(
        'hosts',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )

    parser.add_argument(
        'module',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )

    @jwt_required()
    def post(self):
        data = AdhocCmd.parser.parse_args()
        cmd_details = {'inventory': data['inventory'], 
                        'hosts': data['hosts'],
                        'module': data['module']
                    }

        p1 = subprocess.run(
            'ansible -i {} -m {} {}'.format(cmd_details['inventory'], cmd_details['module'], cmd_details['hosts']),
            shell=True,
            capture_output=True,
            text=True
        )   

        if p1.returncode == 0:  
            return {"messege": "Success", "output" : p1.stdout}
        else:
            return {"messege": "fail", "output": p1.stdout}



    