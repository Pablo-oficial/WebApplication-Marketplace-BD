from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://professor:professor@database-1.c3tyn5siqwcx.us-east-1.rds.amazonaws.com:5432/postgres'
db = SQLAlchemy(app)

class Endereco(db.Model):
    __tablename__ = 'endereco_type'

    cep = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(45))
    bairro = db.Column(db.String(45))
    numero = db.Column(db.Integer)
    cidade = db.Column(db.String(45))
    estado = db.Column(db.String(2))

class Usuario(db.Model):
    __tablename__ = 'Usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), unique=True, nullable=False)
    senha = db.Column(db.String(45), nullable=False)
    conta_bancaria = db.Column(db.String(45), unique=True)
    nome = db.Column(db.String(45), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('endereco_type.cep'))
    endereco = db.relationship('Endereco', foreign_keys=[endereco_id])
    telefone = db.Column(db.ARRAY(db.Integer), nullable=False)

class Vendedor(db.Model):
    __tablename__ = 'Vendedor'

    idvendedor = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.Integer, unique=True, nullable=False)
    razao_social = db.Column(db.String(45), nullable=False)
    nome_fantasia = db.Column(db.String(45))
    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('vendedores', lazy=True))

class Comprador(db.Model):
    __tablename__ = 'Comprador'

    idcomprador = db.Column(db.Integer, primary_key=True)
    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('compradores', lazy=True))

class CompradorFisico(db.Model):
    __tablename__ = 'Comprador_fisico'

    cpf = db.Column(db.Integer, primary_key=True)
    data_nascimento = db.Column(db.Date, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    comprador_idcomprador = db.Column(db.Integer, nullable=False)
    comprador_usuario_id_usuario = db.Column(db.Integer, nullable=False)
    comprador = db.relationship('Comprador', backref=db.backref('comprador_fisico', uselist=False))

class CompradorJuridico(db.Model):
    __tablename__ = 'Comprador_juridico'

    cnpj = db.Column(db.Integer, primary_key=True)
    razao_social = db.Column(db.String(45), nullable=False)
    nome_fantasia = db.Column(db.String(45))
    comprador_idcomprador = db.Column(db.Integer, nullable=False)
    comprador_usuario_id_usuario = db.Column(db.Integer, nullable=False)
    comprador = db.relationship('Comprador', backref=db.backref('comprador_juridico', uselist=False))

class Produto(db.Model):
    __tablename__ = 'Produto'

    idproduto = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(15), nullable=False)
    condicao = db.Column(db.String(10), nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    descricao = db.Column(db.String(300), nullable=False)
    foto = db.Column(db.LargeBinary, nullable=False)
    dimensoes = db.Column(db.String(20), nullable=False)
    vendedor_idvendedor = db.Column(db.Integer, db.ForeignKey('Vendedor.idvendedor'), nullable=False)
    vendedor = db.relationship('Vendedor', backref=db.backref('produtos', lazy=True))

class Estoque(db.Model):
    __tablename__ = 'Estoque'

    quantidade = db.Column(db.Integer, nullable=False)
    produto_idproduto = db.Column(db.Integer, db.ForeignKey('Produto.idproduto'), nullable=False)
    vendedor_idvendedor = db.Column(db.Integer, db.ForeignKey('Vendedor.idvendedor'), nullable=False)
    primary_key = db.PrimaryKeyConstraint(produto_idproduto, vendedor_idvendedor)

class Carrinho(db.Model):
    __tablename__ = 'Carrinho'

    idcarrinho = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    comprador_idcomprador = db.Column(db.Integer, db.ForeignKey('Comprador.idcomprador'), nullable=False)
    comprador = db.relationship('Comprador', backref=db.backref('carrinhos', lazy=True))

class Pagamento(db.Model):
    __tablename__ = 'Pagamento'

    idtransacao = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Date, nullable=False)
    comprador_idcomprador = db.Column(db.Integer, db.ForeignKey('Comprador.idcomprador'), nullable=False)
    comprador = db.relationship('Comprador', backref=db.backref('pagamentos', lazy=True))

class Boleto(db.Model):
    __tablename__ = 'Boleto'

    codigo_barras = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    data_emissao = db.Column(db.Date, nullable=False)
    data_vencimento = db.Column(db.Date, nullable=False)
    pagamento_idtransacao = db.Column(db.Integer, db.ForeignKey('Pagamento.idtransacao'), nullable=False)
    pagamento = db.relationship('Pagamento', backref=db.backref('boletos', lazy=True))

class Pix(db.Model):
    __tablename__ = 'Pix'

    chave = db.Column(db.String(45), primary_key=True)
    banco = db.Column(db.String(20), nullable=False)
    titular = db.Column(db.String(45), nullable=False)
    data = db.Column(db.Date, nullable=False)
    pagamento_idtransacao = db.Column(db.Integer, db.ForeignKey('Pagamento.idtransacao'), nullable=False)
    pagamento = db.relationship('Pagamento', backref=db.backref('pix', lazy=True))

class Cartao(db.Model):
    __tablename__ = 'Cartao'

    numero_cartao = db.Column(db.Integer, primary_key=True)
    agencia = db.Column(db.String(10), nullable=False)
    titular = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    ccv = db.Column(db.Integer, nullable=False)
    validade = db.Column(db.Date, nullable=False)
    pagamento_idtransacao = db.Column(db.Integer, db.ForeignKey('Pagamento.idtransacao'), nullable=False)
    pagamento = db.relationship('Pagamento', backref=db.backref('cartoes', lazy=True))

class Contem(db.Model):
    __tablename__ = 'Contem'

    produto_idproduto = db.Column(db.Integer, nullable=False)
    carrinho_idcarrinho = db.Column(db.Integer, nullable=False)
    primary_key = db.PrimaryKeyConstraint(produto_idproduto, carrinho_idcarrinho)
    produto = db.relationship('Produto', backref=db.backref('contem', lazy=True))
    carrinho = db.relationship('Carrinho', backref=db.backref('contem', lazy=True))

class Transportadora(db.Model):
    __tablename__ = 'Transportadora'

    idtransportadora = db.Column(db.Integer, primary_key=True)
    status_entrega = db.Column(db.String(10), nullable=False)
    contem_quantidade = db.Column(db.Integer, nullable=False)
    contem_produto_idproduto = db.Column(db.Integer, nullable=False)
    contem_carrinho_idcarrinho = db.Column(db.Integer, nullable=False)
    primary_key = db.PrimaryKeyConstraint(contem_produto_idproduto, contem_carrinho_idcarrinho)
    contem = db.relationship('Contem', backref=db.backref('transportadora', lazy=True))

class Credito(db.Model):
    __tablename__ = 'Credito'

    limite = db.Column(db.Integer, nullable=False)
    data_fatura = db.Column(db.Date, nullable=False)
    cartao_numero_cartao = db.Column(db.Integer, nullable=False)
    cartao_pagamento_idtransacao = db.Column(db.Integer, nullable=False)
    primary_key = db.PrimaryKeyConstraint(cartao_numero_cartao, cartao_pagamento_idtransacao)
    cartao = db.relationship('Cartao', backref=db.backref('credito', lazy=True))

class Debito(db.Model):
    __tablename__ = 'Debito'

    saldo = db.Column(db.Integer, nullable=False)
    conta_corrente = db.Column(db.String(15), nullable=False)
    cartao_numero_cartao = db.Column(db.Integer, nullable=False)
    cartao_pagamento_idtransacao = db.Column(db.Integer, nullable=False)
    primary_key = db.PrimaryKeyConstraint(cartao_numero_cartao, cartao_pagamento_idtransacao)
    cartao = db.relationship('Cartao', backref=db.backref('debito', lazy=True))

class Venda(db.Model):
    __tablename__ = 'Venda'

    idvenda = db.Column(db.Integer, primary_key=True)
    nota_fiscal = db.Column(db.String(15), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    pagamento_idtransacao = db.Column(db.Integer, db.ForeignKey('Pagamento.idtransacao'), nullable=False)
    carrinho_idcarrinho = db.Column(db.Integer, db.ForeignKey('Carrinho.idcarrinho'), nullable=False)
    pagamento = db.relationship('Pagamento', backref=db.backref('vendas', lazy=True))
    carrinho = db.relationship('Carrinho', backref=db.backref('vendas', lazy=True))

class VendaHasVendedor(db.Model):
    __tablename__ = 'Venda_has_Vendedor'

    venda_idvenda = db.Column(db.Integer, nullable=False)
    vendedor_idvendedor = db.Column(db.Integer, nullable=False)
    lucro = db.Column(db.Integer, nullable=False)
    primary_key = db.PrimaryKeyConstraint(venda_idvenda, vendedor_idvendedor)
    venda = db.relationship('Venda', backref=db.backref('venda_has_vendedor', lazy=True))
    vendedor = db.relationship('Vendedor', backref=db.backref('venda_has_vendedor', lazy=True))

class VendaHasProduto(db.Model):
    __tablename__ = 'Venda_has_Produto'

    venda_idvenda = db.Column(db.Integer, nullable=False)
    produto_idproduto = db.Column(db.Integer, nullable=False)
    produto_vendedor_idvendedor = db.Column(db.Integer, nullable=False)
    primary_key = db.PrimaryKeyConstraint(venda_idvenda, produto_idproduto, produto_vendedor_idvendedor)
    venda = db.relationship('Venda', backref=db.backref('venda_has_produto', lazy=True))
    produto = db.relationship('Produto', backref=db.backref('venda_has_produto', lazy=True))
