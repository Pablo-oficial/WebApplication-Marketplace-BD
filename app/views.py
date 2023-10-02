from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Configuração do banco de dados
conn = psycopg2.connect(
    dbname="postgres",
    user="professor",
    password="professor",
    host="database-1.c3tyn5siqwcx.us-east-1.rds.amazonaws.com",
    port="5432" 
)
cur = conn.cursor()

# Rotas para operações CRUD de Usuario
@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuario/index.html', usuarios=usuarios)

@app.route('/usuarios/criar', methods=['GET', 'POST'])
def criar_usuario():
    if request.method == 'POST':
        # Processar o formulário e inserir um novo usuário no banco de dados
        novo_usuario = Usuario(email=request.form['email'], senha=request.form['senha'], nome=request.form['nome'], endereco=request.form['endereco'], telefone=request.form['telefone'])
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('listar_usuarios'))
    return render_template('usuario/criar.html')

@app.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        # Processar o formulário e atualizar o usuário no banco de dados
        usuario.email = request.form['email']
        usuario.senha = request.form['senha']
        usuario.nome = request.form['nome']
        usuario.endereco = request.form['endereco']
        usuario.telefone = request.form['telefone']
        db.session.commit()
        return redirect(url_for('listar_usuarios'))
    return render_template('usuario/editar.html', usuario=usuario)

@app.route('/usuarios/excluir/<int:id>')
def excluir_usuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('listar_usuarios'))

# Rotas para operações CRUD de Produto (você pode criar rotas semelhantes para Produto e Carrinho)
# ...

if __name__ == '__main__':
    app.run(debug=True)
