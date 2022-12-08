import csv
from app import app, db
from app.test_measurement.models import Test
from app.user.views import token_required
from flask import request


@app.route("/add_data", methods=["POST"])
@token_required
def test_measuments(current_user):
    """ Function to upload a test file"""
    filepath = request.form.get("filepath")
    try:
        with open(filepath, "r") as file:
            csvreader = csv.reader(file)
            for data in csvreader:
                todo = Test(
                    id=hash(data[0]),
                    v2=data[1],
                    v5=data[2],
                    v6=data[3],
                    driving_style=data[4],
                    public_id=current_user.public_id,
                )
                db.session.add(todo)
                db.session.commit()
    except Exception as error:
        print(f"Error: {error}")
        # Error in the file loading
        return {
            "status_code": 500,
            "Message": "Error in the server, please contact the admin",
        }
    # Data file upload and processing success
    return {"status_code": 200, "Message": "Processed CSV successfully"}
