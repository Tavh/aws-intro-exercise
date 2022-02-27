from flask import Flask
from controllers.greeting_blueprint import greeting_blueprint

app = Flask(__name__)
app.register_blueprint(greeting_blueprint, url_prefix='/greeting')


if __name__ == "__main__":
    app.run(host='0.0.0.0')

