from main import create_app
from main import db
app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables for our models
    app.run(debug=True)