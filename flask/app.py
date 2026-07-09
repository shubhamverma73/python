import os
from extensions import app
from flask_cors import CORS

# import controllers.user_controller as user_controller
# import controllers.product_controller as product_controller

from controllers import user_controller, product_controller

CORS(app)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

if __name__ == "__main__":
    app.run(debug=True)