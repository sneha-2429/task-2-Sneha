from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get('name')
    age = data.get('age')

    if not name or not age:
        return jsonify({"error": "Name and Age are required"}), 400

    student = {
        "id": len(students) + 1,
        "name": name,
        "age": age
    }

    students.append(student)

    return jsonify({
        "message": "Student added successfully",
        "student": student
    }), 201

if __name__ == '__main__':
    app.run(debug=True)