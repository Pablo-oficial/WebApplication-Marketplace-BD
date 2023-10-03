from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Usuario, Produto, Carrinho

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://professor:professor@database-1.c3tyn5siqwcx.us-east-1.rds.amazonaws.com:5432/postgres'
db = SQLAlchemy(app)

# Rota para criar um novo usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    novo_usuario = Usuario(**data)
    
    try:
        db.session.add(novo_usuario)
        db.session.commit()
        return jsonify({'mensagem': 'Usuário criado com sucesso!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

# Rota para listar todos os usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    usuarios_json = [{'id_usuario': u.id_usuario, 'nome': u.nome, 'email': u.email} for u in usuarios]
    return jsonify(usuarios_json)

# Rota para atualizar um usuário pelo ID
@app.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def atualizar_usuario(id_usuario):
    data = request.json
    usuario = Usuario.query.get(id_usuario)
    
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404
    
    for key, value in data.items():
        setattr(usuario, key, value)
    
    try:
        db.session.commit()
        return jsonify({'mensagem': 'Usuário atualizado com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

# Rota para excluir um usuário pelo ID
@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def excluir_usuario(id_usuario):
    usuario = Usuario.query.get(id_usuario)
    
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404
    
    try:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'mensagem': 'Usuário excluído com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

# Rota para criar um novo produto
@app.route('/produtos', methods=['POST'])
def criar_produto():
    data = request.json
    novo_produto = Produto(**data)
    
    try:
        db.session.add(novo_produto)
        db.session.commit()
        return jsonify({'mensagem': 'Produto criado com sucesso!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

# Rota para listar todos os produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    produtos_json = [{'idproduto': p.idproduto, 'nome': p.nome, 'preco': p.preco} for p in produtos]
    return jsonify(produtos_json)

# Rota para atualizar um produto pelo ID
@app.route('/produtos/<int:idproduto>', methods=['PUT'])
def atualizar_produto(idproduto):
    data = request.json
    produto = Produto.query.get(idproduto)
    
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    
    for key, value in data.items():
        setattr(produto, key, value)
    
    try:
        db.session.commit()
        return jsonify({'mensagem': 'Produto atualizado com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

# Rota para excluir um produto pelo ID
@app.route('/produtos/<int:idproduto>', methods=['DELETE'])
def excluir_produto(idproduto):
    produto = Produto.query.get(idproduto)
    
    if not produto:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    
    try:
        db.session.delete(produto)
        db.session.commit()
        return jsonify({'mensagem': 'Produto excluído com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400
    
# Rota para criar um novo carrinho
@app.route('/carrinhos', methods=['POST'])
def criar_carrinho():
    data = request.json
    novo_carrinho = Carrinho(**data)
    
    try:
        db.session.add(novo_carrinho)
        db.session.commit()
        return jsonify({'mensagem': 'Carrinho criado com sucesso!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

# Rota para listar todos os carrinhos
@app.route('/carrinhos', methods=['GET'])
def listar_carrinhos():
    carrinhos = Carrinho.query.all()
    carrinhos_json = [{'idcarrinho': c.idcarrinho, 'quantidade': c.quantidade, 'preco': c.preco} for c in carrinhos]
    return jsonify(carrinhos_json)

# Rota para atualizar um carrinho pelo ID
@app.route('/carrinhos/<int:idcarrinho>', methods=['PUT'])
def atualizar_carrinho(idcarrinho):
    data = request.json
    carrinho = Carrinho.query.get(idcarrinho)
    
    if not carrinho:
        return jsonify({'erro': 'Carrinho não encontrado'}), 404
    
    for key, value in data.items():
        setattr(carrinho, key, value)
    
    try:
        db.session.commit()
        return jsonify({'mensagem': 'Carrinho atualizado com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

# Rota para excluir um carrinho pelo ID
@app.route('/carrinhos/<int:idcarrinho>', methods=['DELETE'])
def excluir_carrinho(idcarrinho):
    carrinho = Carrinho.query.get(idcarrinho)
    
    if not carrinho:
        return jsonify({'erro': 'Carrinho não encontrado'}), 404
    
    try:
        db.session.delete(carrinho)
        db.session.commit()
        return jsonify({'mensagem': 'Carrinho excluído com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)