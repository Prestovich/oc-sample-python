from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return 'Hello World!'
    
@application.route("/hum")
def humbe():
    return "Hello Humberto!"

@application.route("/ben")
def humbe():
    return "Hello Benny!"

@application.route("/rh")
def humbe():
    return "Red Hat loves LINUX!"

@application.route("/bob")
def bob():
    return "Hi Bob!"

@application.route("/bo")
def boeing():
    return "Thank you boeing!"

if __name__ == "__main__":
    application.run()
