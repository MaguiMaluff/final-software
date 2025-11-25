from app import create_app, db
import os

app = create_app()

# Ensure the database is created if it doesn't exist
with app.app_context():
    db_path = os.path.join(os.getcwd(), 'umbook.db')
    if not os.path.exists(db_path):
        db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
