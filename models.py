from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    todos = db.Column(db.String(400), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "todos": self.todos        
        }