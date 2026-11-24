"""SecureFlow demo application (Flask)."""
from flask import Flask, jsonify, abort

app = Flask(__name__)

ITEMS = [
    {"id": 1, "name": "Widget", "price": 9.99},
    {"id": 2, "name": "Gadget", "price": 19.99},
    {"id": 3, "name": "Gizmo", "price": 29.99},
]


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/items")
def list_items():
    return jsonify(ITEMS)


@app.get("/items/<int:item_id>")
def get_item(item_id: int):
    for item in ITEMS:
        if item["id"] == item_id:
            return jsonify(item)
    abort(404)


if __name__ == "__main__":
    # Local development only; the container uses gunicorn.
    app.run(host="127.0.0.1", port=5000)
