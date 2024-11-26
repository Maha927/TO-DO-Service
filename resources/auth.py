from flask import request, jsonify
from flask_restful import Resource
from models import db, User
from flask_jwt_extended import create_access_token

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        
        if User.query.filter_by(username=username).first():
            return {"message": "User already exists"}, 400
        
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return {"message": "User created successfully"}, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            return {"message": "Invalid credentials"}, 401
        
        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}, 200
