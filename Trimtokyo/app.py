import os
from flask import Flask, request, render_template, render_template_string, jsonify
from flask_mail import Mail, Message
from dotenv import load_dotenv
from weasyprint import HTML
from flask_cors import CORS

# Load environment variables
load_dotenv("config.env")

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Optional: Allow cross-origin requests

# Flask-Mail Config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

# 📬 Email Route
@app.route("/send", methods=["POST"])
def send_email():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"status": "error", "message": "Missing fields"}), 400

    try:
        # Load and render the PDF template
        with open("pdf_template.html") as f:
            html_template = f.read()

        rendered_html = render_template_string(html_template, name=name, email=email, message=message)
        pdf = HTML(string=rendered_html).write_pdf()

        msg = Message(subject="New Contact Form Submission",
                      recipients=[os.getenv('MAIL_RECEIVER')])
        msg.body = f"Contact form received from {name} <{email}>"
        msg.attach("contact-form.pdf", "application/pdf", pdf)

        mail.send(msg)
        return jsonify({"status": "success", "message": "Email sent!"})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 🏠 Serve Frontend
@app.route("/")
def index():
    return render_template("index.html")  # Automatically looks in templates/

# Optional: Serve other HTML pages
@app.route("/<page>")
def static_page(page):
    try:
        return render_template(page)
    except:
        return "404 Page Not Found", 404

if __name__ == "__main__":
    app.run(debug=True)
