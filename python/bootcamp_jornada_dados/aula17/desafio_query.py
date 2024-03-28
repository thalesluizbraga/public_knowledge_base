#%%
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey # Tipos de dados, colunas, chaves 
from sqlalchemy.orm import declarative_base # modulo para instanciar uma base que as classes que formam as tabelas usam
from sqlalchemy.orm import relationship # modulos para fazer relacionamento de tabelas
from sqlalchemy.exc import SQLAlchemyError  # Importa exceções do SQLAlchemy



Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores' # instancia do nome da tabela na memoria do pc
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))


class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    fornecedor = relationship("Fornecedor")  # Relação entre Produto e Fornecedor

engine = create_engine('sqlite:///desafio_query.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_preco')
).join(Produto, Fornecedor.id == Produto.fornecedor_id
).group_by(Fornecedor.nome).all()

for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")  




# %%
