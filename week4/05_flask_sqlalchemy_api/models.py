"""
Goal: replace the plain Python list from step 04 with a real database table,
using Flask-SQLAlchemy (an ORM — it lets us write Python classes instead of
raw SQL).
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    credits = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert this database row into a plain dict so jsonify() can use it."""
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "credits": self.credits,
        }
