import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bdloja",
)

cursor = conexao.cursor()
print("Conexão como o banco de dados feita com sucesso! \n")


# funcao inserir
def cadastrar(nome: str, preco: float, id: str, img: str):
    ''' Faz a inserção de um produto no banco de dados. A imagem é a URL da imagem do produto na web.
    Utilizar formatos encurtados com quantidade de caracteres inferiores a 100
    Você poderá usar o https://www.encurtarlink.com/ para ajustar ao formato adequado'''

    comando_sql = f"insert into produtos (nome, preco, id, imagem) value ('{nome}', {preco},'{id}','{img}')"

    cursor.execute(comando_sql)
    conexao.commit()  # aqui é onde vamos inserir os dados
    print("Produto cadastrado com sucesso!")


# funcao selecionar
def selecionarTodosProdutos():
    comando_sql = f'select id, nome, preco from produtos'
    cursor.execute(comando_sql)
    resultado_consulta = cursor.fetchall()
    return resultado_consulta


# funcao atualizar
def atualizarPreco(id: str, novo_valor: float):
    comando_sql = f' UPDATE produtos SET preco = {novo_valor} WHERE id = "{id}"'
    cursor.execute(comando_sql)
    conexao.commit()


# funcao deletar
def deletarProduto(id: int):
    comando_sql = f'DELETE FROM produtos WHERE id = "{id}"'
    cursor.execute(comando_sql)
    conexao.commit()

def att_nome(id: int, novo_nome:str ):
    #UPATE - ATT OS DADOS, ATRAVÉS DO ID
    consultaSQL = f'UPDATE produtos SET nome_produto = "{novo_nome}"\
    WHERE id_produto = {id}'
    cursor.execute(consultaSQL)
    conexao.commit()

def vs():
    # consultarTodos
    # R - READ - SELECT
    comandoSQL = f'SELECT id, nome, preco * FROM produtos'
    cursor.execute(comandoSQL)
    resultadoConsulta = cursor.fetchall()
    return resultadoConsulta


def consultarPeloId(id):
    # R - READ - SELECT
    comandoSQL = f'SELECT id, nome, imagem from produtos WHERE id = {id}'
    cursor.execute(comandoSQL)

    resultadoConsulta = cursor.fetchone()

    return resultadoConsulta