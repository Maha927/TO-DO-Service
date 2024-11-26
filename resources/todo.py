from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Todo

class TodoList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        todos = Todo.query.filter_by(user_id=user_id).all()
        return jsonify([{"id": todo.id, "title": todo.title, "description": todo.description} for todo in todos])

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        todo = Todo(title=data["title"], description=data.get("description", ""), user_id=user_id)
        db.session.add(todo)
        db.session.commit()
        return {"message": "To-do created"}, 201

class TodoResource(Resource):
    @jwt_required()
    def put(self, todo_id):
        user_id = get_jwt_identity()
        todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()

        if not todo:
            return {"message": "Todo not found"}, 404

        data = request.get_json()
        todo.title = data.get("title", todo.title)
        todo.description = data.get("description", todo.description)
        db.session.commit()
        return {"message": "Todo updated"}, 200

    @jwt_required()
    def delete(self, todo_id):
        user_id = get_jwt_identity()
        todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()

        if not todo:
            return {"message": "Todo not found"}, 404

        db.session.delete(todo)
        db.session.commit()
        return {"message": "Todo deleted"}, 200
