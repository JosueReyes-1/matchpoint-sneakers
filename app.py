from flask import Flask, request, jsonify
import boto3


client = boto3.client('cognito-idp', region_name='us-east-2')
app = Flask(__name__)


@app.route('/')
def home():
    return 'estas en el inicio'


@app.route('/users/create', methods=['POST'])
def create_user():
    request_data = request.get_json()
    username = request_data['username']
    email = request_data['email']

    response = client.admin_create_user(
        UserPoolId='us-east-2_Hkdcyy6SP',
        Username=username,
        UserAttributes=[
            {
                'Name': 'email',
                'Value': email
            },
            {
                'Name': 'name',
                'Value': username
            },
        ],
    )
    print(response)
    return 'usuario creado'


@app.route('/users/login', methods=['POST'])
def login():
    request_data = request.get_json()
    password = request_data['password']
    email = request_data['email']
    user_pool_id = 'us-east-2_Hkdcyy6SP'
    client_id = '49d8sqiv20ttb62rups91i1ovi'
    user_credentials = {"USERNAME": email, "PASSWORD": password}
    response = client.admin_initiate_auth(
        UserPoolId=user_pool_id,
        ClientId=client_id,
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters=user_credentials
    )
    print(response)
    return 'hola'


@app.route('/users/change-password', methods=['POST'])
def change_password():
    request_data = request.get_json()
    new_password = request_data['new_password']
    email=request_data['email']
    response = client.admin_set_user_password(
        UserPoolId='us-east-2_Hkdcyy6SP',
        Username=email,
        Password=new_password,
        Permanent=True
    )
    print(response)
    return 'fue cambiada con exito'
