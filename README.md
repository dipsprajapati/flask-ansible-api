#flask-ansible-api

This is a simple flask api to run Ansible playbooks and adhoc commands

##Instalation

This is not a production grade api. To start the dev environemt running follow below mentioned steps.

1. clone the repo to your local machine
2. cd to the repo directory
3. create virtual enviornment venv --> python3 -m venv venv
3. Install required packages --> "pip install requirements.txt"
4. Run --> "Python app.py"

This will start the dev server at http://127.0.0.1:5000

##API Endpoints
1. POST /register --> register your credentials with parameters username and password
    Body:
    {
        "username": "username",
        "password": "password"
    }
2. GET /auth --> Get the auth token
3. POST /playbook/<playbook-name> --> Run the playbook with the inventory name provided in body
    Body:
    {
	"inventory": "inventory"
    }
4. POST /adhoc --> Run the adhoc command with the specified inventory, hosts and module
    Body:
    {
	"inventory": "inventory",
	"hosts": "all",
	"module": "ping"
    }



