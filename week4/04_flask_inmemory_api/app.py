"""
Goal: build the same idea as step 01 (a working endpoint) but in Flask,
which is a much smaller, more "do it yourself" framework than Django.

No database yet — we just store courses in a plain Python list while the
app is running. Restarting the app wipes the data. That's fine for now;
step 05 adds a real database.

Run with:  python app.py
Then visit: http://127.0.0.1:5000/courses
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Our "database" for now: just a list living in memory.
courses = []


@app.route("/courses", methods=["GET"])
def list_courses():
    return jsonify(courses), 200


@app.route("/courses", methods=["POST"])
def create_course():
    data = request.get_json()

    # Basic validation: make sure the client sent everything we need.
    required_fields = ["name", "code", "credits"]
    missing = [f for f in required_fields if f not in (data or {})]
    if missing:
        return jsonify({
            "status": "error",
            "message": f"Missing fields: {', '.join(missing)}",
        }), 400

    new_course = {
        "id": len(courses) + 1,
        "name": data["name"],
        "code": data["code"],
        "credits": data["credits"],
    }
    courses.append(new_course)
    return jsonify({"status": "success", "data": new_course}), 201


if __name__ == "__main__":
    app.run(debug=True)
