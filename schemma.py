from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, Table,
)
from sqlalchemy.future import select
from sqlalchemy.orm import (
    sessionmaker, declarative_base, relationship,
)


engine = create_engine('sqlite+pysqlite:///dbteste.sql')
Session = sessionmaker(bind=engine, future=True)
session = Session()
Base = declarative_base()


fornecedores_produtos = Table('fornecedores_produtos', Base.metadata,
                             Column('id_produto', Integer, ForeignKey('produtos.id')),
                             Column('id_fornecedor', Integer, ForeignKey('fornecedores.id'))
                             )


categorias_produtos = Table('categorias de produtos', Base.metadata,
                            Column('id_produto', Integer, ForeignKey('produtos.id')),
                            Column('id_categoria', Integer, ForeignKey('categorias.id'))
                            )

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))

    fornecedores = relationship('Fornecedor', secondary=fornecedores_produtos, back_populates='produtos')
    categorias = relationship('Categoria', secondary=categorias_produtos, back_populates='produtos')

    def __repr__(self):
        return f'<Produto(nome={self.nome})>'

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True)
    nome = Column(String(30))

    produtos = relationship('Produto', secondary=fornecedores_produtos, back_populates='fornecedores')

    def __repr__(self):
        return f'<Fornecedor(nome={self.nome})>'
    
class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nome = Column(String(20))

    produtos = relationship('Produto', secondary=categorias_produtos, back_populates='categorias')

    def __repr__(self):
        return f'<Categoria(nome={self.nome})>'
                  

Base.metadata.create_all(engine)
