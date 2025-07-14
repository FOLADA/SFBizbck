from flask import Flask
from flask_cors import CORS
from db import init_db
from routes import bp as business_routes
import os

app = Flask(__name__)
CORS(app)

init_db()

app.register_blueprint(business_routes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(debug=True, host="0.0.0.0", port=port)  
