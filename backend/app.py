from flask import Flask, jsonify, request
from models import db, User
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # This creates all tables defined by models
    
# test route
@app.route('/')
def working():
    return "Flask server working!"
# test route
@app.route('/hello')
def hello_world():
    return "Hello, World!"

# Route to get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# Route to get a user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200

# Route to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    try:
        user = User(name=data['name'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to update user by ID and email
@app.route('/users/<int:id>', methods=['PUT'])
def update_user_by_id(id):
    data = request.json
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    try:
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify(user.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete user by ID
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'User {id} deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete user by email
@app.route('/users', methods=['DELETE'])
def delete_user_by_email():
    email = request.args.get('email')
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'User with email {email} deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 40

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)