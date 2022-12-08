from app import app, db
import app.user.views as user_views
import app.test_measurement.views as test_views


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
