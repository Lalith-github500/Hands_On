"""
Same two endpoints as step 04 (GET/POST /courses), but now every course is
actually saved to a SQLite database file, so the data survives a restart.

Run with: python app.py
"""
from flask import Flask, jsonify, request

from models import Course, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///courses.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # creates courses.db and the `courses` table if missing


@app.route("/courses", methods=["GET"])
def list_courses():
    courses = Course.query.all()
    return jsonify([c.to_dict() for c in courses]), 200


@app.route("/courses", methods=["POST"])
def create_course():
    data = request.get_json()

    required_fields = ["name", "code", "credits"]
    missing = [f for f in required_fields if f not in (data or {})]
    if missing:
        return jsonify({
            "status": "error",
            "message": f"Missing fields: {', '.join(missing)}",
        }), 400

    new_course = Course(
        name=data["name"],
        code=data["code"],
        credits=int(data["credits"]),
    )
    db.session.add(new_course)
    db.session.commit()  # actually writes the row to courses.db

    return jsonify({"status": "success", "data": new_course.to_dict()}), 201


if __name__ == "__main__":
    app.run(debug=True)
