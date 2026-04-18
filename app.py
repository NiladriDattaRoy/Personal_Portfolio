from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create DB
def init_db():
    conn = sqlite3.connect('skills.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Get all skills
@app.route('/skills', methods=['GET'])
def get_skills():
    conn = sqlite3.connect('skills.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM skills")
    data = cursor.fetchall()
    conn.close()

    skills = [{"id": row[0], "name": row[1]} for row in data]
    return jsonify(skills)

# Add new skill
@app.route('/add-skill', methods=['POST'])
def add_skill():
    data = request.json
    name = data.get("name")

    conn = sqlite3.connect('skills.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO skills (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Skill added!"})

if __name__ == '__main__':
    app.run(debug=True)