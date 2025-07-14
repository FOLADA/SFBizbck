from flask import Flask
from flask_cors import CORS
from db import init_db
from routes import bp as business_routes

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # ✅ Allow frontend

init_db()

app.register_blueprint(business_routes)

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Optional: specify port explicitly
