from sqlalchemy.future import select
from sqlalchemy import update, delete
from schemma import (
    session, Produto, Fornecedor, Categoria
)


def criar_produto(nome, nome_fornecedor):
    with session as s:
        produto = (Produto(nome=nome))

        # Verifica se o fornecedor passado no parametro já existe
        query_fornecedor = select(Fornecedor).where(Fornecedor.nome == nome_fornecedor)
        result = s.execute(query_fornecedor).scalar()

        # se result for False, cadastra o novo fornecedor e coloca no produto
        # se for verdadeiro, apenas da um append desse produto na lista dos fornecedores
        if not result:
            novo_fornecedor = Fornecedor(nome=nome_fornecedor)
            produto.fornecedores.append(novo_fornecedor)
        else:
            produto.fornecedores.append(result)

        s.add(produto)
        s.commit()

def criar_fornecedor(nome):
    with session as s:
        
        s.add(Produto(nome=nome))
        s.commit()


def buscar_produto(nome):
    with session as s:
        query = s.execute(
            select(Produto).where(Produto.nome == nome)
        )
        return query.scalar()
    

def atualizar_nome_produto(nome_antigo, nome_novo):
    with session as s:
        s.execute(
            update(Produto).where(Produto.nome == nome_antigo).
            values(nome=nome_novo)
        )
        s.commit()


def deletar_produto(nome):
    with session as s:
        s.execute(
            delete(Produto).where(Produto.nome == nome)
        )
        s.commit()


def buscar_fornecedores_por_produto(nome_produto):
    with session as s:
        query = s.execute(select(Produto, Fornecedor).join(
            Fornecedor.produtos).where(Produto.nome == nome_produto))
        result = query.first()
        return result
    
