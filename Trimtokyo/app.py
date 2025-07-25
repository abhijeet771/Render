import os
from flask import Flask, render_template, request, jsonify, render_template_string
from flask_mail import Mail, Message
from flask_cors import CORS
from dotenv import load_dotenv
from weasyprint import HTML

# Load environment variables
load_dotenv("config.env")

app = Flask(__name__)
CORS(app)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Contact form POST handler
@app.route("/send", methods=["POST"])
def send_email():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"status": "error", "message": "Missing fields"}), 400

    try:
        with open("pdf_template.html") as f:
            html_template = f.read()

        html = render_template_string(html_template, name=name, email=email, message=message)
        pdf = HTML(string=html).write_pdf()

        msg = Message(subject="New Contact Form Submission",
                      recipients=[os.getenv('MAIL_RECEIVER')])
        msg.body = f"Contact form received from {name} <{email}>"
        msg.attach("contact-form.pdf", "application/pdf", pdf)

        mail.send(msg)
        return jsonify({"status": "success", "message": "Email sent!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Register page
@app.route("/register")
def register():
    return render_template("register.html")

# Login page
@app.route("/login")
def login():
    return render_template("login.html")

# Services page
@app.route("/services")
def services():
    return render_template("services.html")

# Contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Admin dashboard (optional if used)
@app.route("/admin")
def admin():
    return render_template("admin_dashboard.html")

# User dashboard (optional if used)
@app.route("/user")
def user():
    return render_template("user_dashboard.html")

# Barber dashboard (optional if used)
@app.route("/barber")
def barber():
    return render_template("barber_dashboard.html")

# Health check
@app.route("/ping")
def ping():
    return "✅ App is running!"

if __name__ == "__main__":
    app.run(debug=True)
