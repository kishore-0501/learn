from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Dummy database (for practice)
users = []

# -------------------------------
# HOME PAGE
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# REGISTER
# -------------------------------
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    password = data.get("password")
    role = data.get("role")

    # simple validation
    if not name or not email or not password:
        return jsonify({
            "status": "error",
            "message": "Missing fields"
        })

    # check if user exists
    for user in users:
        if user["email"] == email:
            return jsonify({
                "status": "error",
                "message": "User already exists"
            })

    # save user
    users.append({
        "name": name,
        "email": email,
        "phone": phone,
        "password": password,
        "role": role
    })

    return jsonify({
        "status": "approved",
        "message": "Registration successful!"
    })


# -------------------------------
# LOGIN
# -------------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    for user in users:
        if user["email"] == email and user["password"] == password:
            return jsonify({
                "status": "approved",
                "message": "Login successful!",
                "role": user["role"]
            })

    return jsonify({
        "status": "error",
        "message": "Invalid credentials"
    })


# -------------------------------
# DUMMY PAGES
# -------------------------------
@app.route("/courses-page")
def courses():
    return "<h1>Courses Page (Coming Soon)</h1>"


@app.route("/instructor")
def instructor():
    return "<h1>Instructor Dashboard (Coming Soon)</h1>"


# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    print("Running Flask...")
    app.run(host="0.0.0.0", port=5000, debug=True)