from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from models import db
from config import Config
from resources.auth import Register, Login
from resources.todo import TodoList, TodoResource

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(TodoList, '/todos')
api.add_resource(TodoResource, '/todos/<int:todo_id>')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
