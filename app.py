from flask import Flask, render_template, request, url_for, redirect, flash
import os
from flask_mail import Mail, Message

app = Flask(__name__)

app.secret_key = os.urandom(12)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Your SMTP server
app.config['MAIL_PORT'] = 587  # Your SMTP port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kiruifelix03@gmail.com'  # Your email username
app.config['MAIL_PASSWORD'] = 'uife imvl jidh ejtw'  # Your email password

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form.get("fullname")
        message = request.form.get("message")
        if name and message:
            try:
                # Send email
                send_email(name, message)
                flash("Message sent successfully!", "success")
                return render_template("confirm.html")
            except Exception as e:
                flash(f"An error occurred: {str(e)}", "error")
    return render_template("contact.html")

def send_email(name, message):
    msg = Message('New Message from Contact Form',
                  sender='kiruifelix03@gmail.com',
                  recipients=['arvinedagruzz03@gmail.com'])  # Recipient email address
    msg.body = f"Name: {name}\n\nMessage: {message}"
    mail.send(msg)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
