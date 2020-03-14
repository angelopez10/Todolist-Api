from flask import Flask, render_template, request, jsonify, json
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, Usuario

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["ENV"]  = "development"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:0210456l@localhost/user'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)
CORS(app)

@app.route("/")
def root():
    return render_template("index.html")
    
   
@app.route("/api/todos/user/<username>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def usuarios(username):
    if request.method == 'POST':
        todos = request.get_json()

        usuario = Usuario()
        usuario.username = username
        usuario.todos = json.dumps(todos)

        db.session.add(usuario)
        db.session.commit()

        return jsonify(usuario.serialize()), 201
    
    if request.method == 'GET':
            usuarios = Usuario.query.filter_by(username=username).first()
            if usuarios:
                return jsonify(usuarios.serialize()), 200
            else:
                return jsonify({"msg":"username not found"}), 404
        

    if request.method == 'PUT':
        todos = request.get_json()

        usuario = Usuario.query.filter_by(username=username).first()
        usuario.username = username
        usuario.todos = json.dumps(todos)

        db.session.commit()

        return jsonify(usuario.serialize()), 200

    if request.method == 'DELETE':
        usuario = Usuario.query.filter_by(username=username).first()
        db.session.delete(usuario)
        db.session.commit()

        return jsonify({"msg": "Usuario eliminado"}), 200

if __name__ == "__main__":
    manager.run()

