from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skills Display</title>
</head>
<body>
    <h1>Enter Your Details</h1>
    <form method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <label for="skills">Skills (comma-separated):</label><br>
        <input type="text" id="skills" name="skills" required><br><br>
        <button type="submit">Submit</button>
    </form>
    {% if name and skills %}
        <h2>Hello, {{ name }}!</h2>
        <p>Your skills are:</p>
        <ul>
            {% for skill in skills %}
                <li>{{ skill }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    skills = None
    if request.method == "POST":
        name = request.form.get("name")
        skills = [skill.strip() for skill in request.form.get("skills").split(",")]
    return render_template_string(HTML_TEMPLATE, name=name, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)
