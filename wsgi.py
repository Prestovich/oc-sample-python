from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return 'Hello World!'
    
@application.route("/rh")
def redhat():
    return "Red Hat loves linux"


@application.route("/bo")
def boeing():
    return "Thanks Boeing for allowing us to work with you!!"

if __name__ == "__main__":
    application.run()
