from flask import Flask, jsonify, request
import json
import os
from flask.views import MethodView
from flask_smorest import Api, Blueprint
from marshmallow import Schema, fields
from schemas.user_schema import ItemSchema, ItemResponseSchema


blp = Blueprint("Items", __name__, description="Operations on items")

# Route to fetch all items from role.json
@blp.route("/item")
class Item(MethodView):

    @blp.response(200, ItemResponseSchema(many=False))
    def get(self):
        with open("role.json", "r", encoding="utf-8") as role:
            data = json.load(role)
        return {"status": 200, "message": "Items fetched successfully", "data": data}    
    
        
    # Route to add a new item to role.json
    @blp.arguments(ItemSchema)
    def post(self, new_item):
        with open("role.json", "r", encoding="utf-8") as role:
            data = json.load(role)
        item = next((i for i in data if i.get("id") == new_item.get("id")), None)
        if item:
            return {"status": 200, "message": "Item already exists, try with different ID"}
        else:
            with open("role.json", "r+", encoding="utf-8") as role:
                data = json.load(role)
                data.append(new_item)
                role.seek(0)
                json.dump(data, role, indent=4)
            return {"status": 201, "message": "Item added successfully", "data": new_item}, 201


# Route to fetch a specific item by ID from role.json
@blp.route("/item/<int:item_id>")
class ItemDetail(MethodView):

    @blp.response(200, ItemResponseSchema(many=False))
    def get(self, item_id):
        with open("role.json", "r", encoding="utf-8") as role:
            data = json.load(role)
        item = next((i for i in data if i.get("id") == item_id), None)
        if item:
            return {"status": 200, "message": "Item fetched successfully", "data": item}
        else:
            return {"status": 404, "message": "Item not found"}, 404

    # Route to update an existing item in role.json
    @blp.arguments(ItemSchema)
    def put(self, updated_item, item_id):
        with open("role.json", "r", encoding="utf-8") as role:
            data = json.load(role)
        item = next((i for i in data if i.get("id") == item_id), None)
        if item:
            data.remove(item)
            data.append(updated_item)
            with open("role.json", "w", encoding="utf-8") as role:
                json.dump(data, role, indent=4)
            return {"status": 200, "message": "Item updated", "data": updated_item}, 200
        else:
            return {"status": 404, "message": "Item not found"}, 404
            
    # Route to delete an item from role.json
    def delete(self, item_id):
        file_path = "role.json"
        if not os.path.exists(file_path):
            return {"status": 404, "message": "role.json file not found"}, 404
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        item = next((i for i in data if i.get("id") == item_id), None)
        if item is None:
            return {"status": 404, "message": "Item not found"}, 404
        updated_data = [i for i in data if i.get("id") != item_id]
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(updated_data, file, ensure_ascii=False, indent=4)
        if item:
            return { "status": 200, "message": "Item deleted successfully", "deleted_item": item }, 200
        else:
            return { "status": 404, "message": "Item not found" }, 404