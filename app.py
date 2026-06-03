from flask import Flask , request , jsonify
from models.user import User
from database import db
from flask_login import LoginManager , login_user, logout_user, login_required , current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

#view login
login_manager.login_view = 'login'
#Session <- conexão ativa 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=["POST"])
def login():
    data = request.json 
    username = data.get("username")
    password = data.get("password")

    if username and password:
        #login
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return jsonify({"message": "Autenticacao realizada com sucesso"})
    
    return jsonify({"message": "Credenciais invalidas"}), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout realizado com sucesso'})

@app.route('/user', methods=["POST"])
@login_required
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message' : f'Usuario: {username} foi cadastrado com sucesso'})

    return jsonify({'message': 'Dados Invalidos'}), 400

@app.route('/user/<int:id_user>', methods=['GET'])
@login_required
def read_user(id_user):
    user = User.query.get(id_user)

    if user:
        return jsonify({'username': user.username})
    
    return jsonify({'message': 'Usuario não encontrado'}),404

@app.route('/user/<int:id_user>', methods=['PUT'])
@login_required
def update_user(id_user):
    data = request.json
    new_password = data.get("password")
    user = User.query.get(id_user)

    if user and new_password:
        user.password = new_password
        db.session.commit()
        return jsonify({"message": f"O usuario {user.username} teve sua senha atualizada com sucesso"})
    
    return jsonify({'message': 'Usuario não encontrado'}),404

@app.route('/user/<int:id_user>', methods=["DELETE"])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)

      #Não é pemitido deletar o usuario que esta autenticado
    if id_user == current_user.id:
        return jsonify({"message": f"{user.username}, não é permitdo deletar o mesmo usario autenticado"}), 403

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuario {user.username} deletado com sucesso"})
    
    return jsonify({'message': 'Usuario não encontrado'}),404


if __name__ == '__main__':
    app.run(debug=True)
