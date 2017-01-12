from flask import Flask
from routes import category, item, api, auth, user

app = Flask(__name__)

app.register_blueprint(category)
app.register_blueprint(item)
app.register_blueprint(api)
app.register_blueprint(auth)
app.register_blueprint(user)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
