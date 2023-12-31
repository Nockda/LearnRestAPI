from app import app, db
from model.user_model import User_model
from flask import request, jsonify

user = User_model()


@app.route("/users", methods=["GET", "POST"])
def search_users():
    if request.method == "GET":
        all_users = User_model.query.all()
        users_list = [
            {
                "user_no": user.user_no,
                "user_id": user.user_id,
                "user_name": user.user_name,
            }
            for user in all_users
        ]
        return jsonify({"users": users_list})
    elif request.method == "POST":
        data = request.json
        new_user = User_model(
            user_id=data["user_id"],
            user_name=data["user_name"],
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully!"})
