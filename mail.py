from flask import Flask
from flask_mail import Mail,Message
app=Flask(__name__)
mail=Mail(app)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "mailid@gmail.com"
app.config["MAIL_PASSWORD"] = "****************"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail=Mail(app)
@app.route("/")
def user():
    msg = Message("FLASK COMPANY",sender = "mailid@gmail.com",recipients = ["ID1@gmail.com"])
    msg.body ="You have selected for our company"
    mail.send(msg)
    return "message sent successfully"
if __name__ == "__main__":
    app.run(debug = True)