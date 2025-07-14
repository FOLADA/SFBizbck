from flask import request, jsonify
from db import get_db
from flask import Blueprint

bp = Blueprint("businesses", __name__)



@bp.route("/")
def home():
    return "Flask backend is working!"

@bp.route("/businesses", methods=["GET"])
def list_businesses():
    category = request.args.get("category")
    with get_db() as conn:
        if category:
            cursor = conn.execute("SELECT * FROM businesses WHERE category = ?", (category,))
        else:
            cursor = conn.execute("SELECT * FROM businesses")
        businesses = [dict(row) for row in cursor.fetchall()]
    return jsonify(businesses), 200

@bp.route("/businesses/<int:biz_id>", methods=["GET"])
def get_business(biz_id):
    with get_db() as conn:
        cursor = conn.execute("SELECT * FROM businesses WHERE id = ?", (biz_id,))
        business = cursor.fetchone()
    if business:
        return jsonify(dict(business)), 200
    return jsonify({"error": "Business not found"}), 404

@bp.route("/businesses", methods=["POST"])
def add_business():
    required_fields = ["name", "category", "description", "services", "contact", "image_url"]
    data = request.get_json(force=True)
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    with get_db() as conn:
        conn.execute(
            """
            INSERT INTO businesses (name, category, description, services, contact, image_url, location, rating)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["name"],
                data["category"],
                data["description"],
                data["services"],
                data["contact"],
                data["image_url"],
                data.get("location", ""),
                data.get("rating", None)
            ),
        )
        conn.commit()
        new_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    return jsonify({"id": new_id}), 201
