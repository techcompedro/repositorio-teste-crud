import streamlit as st
import funcoesCrud as fc
import pandas as pd

st.set_page_config(page_title='cadastro de produtos')

# título e sub-título
st.title('SISTEMA EM DESENVOLVIMENTO')

col1, col2 = st. columns(2)
cont = col2.container(border=True)
containertitulo = col1.container(border=True)
containerlista= st.container(border=True)

# inserir produto
with st.container():
    containertitulo.markdown('### campo para cadastro de produto')
    nome = containertitulo.text_input('Nome do produto', placeholder='Nome do produto com no máximo 50 caracteres')
    imagem = containertitulo.text_input('Imagem do produto', placeholder='Url da imagem do produto com até 100 caracteres')
    codigo = containertitulo.text_input('Código do produto', placeholder='Código do produto')
    preco = float(containertitulo.number_input('Preço produto'))

    btnCadastrarProduto = containertitulo.button('Cadastrar Produto')

    if btnCadastrarProduto:
        a = fc.cadastrar(nome, preco, codigo, imagem)
        st.write('Produto cadastrado com sucesso')


with st.container():

    id01 = cont.number_input("Digite o código do produto: ", value=None, placeholder= "0")
    nome01 = str(cont.text_input('Digite o nome do produto:'))
    atualizar01 = cont.button('atualizar')
    if atualizar01:
            modificarnome = fc.att_nome(id01, nome01)


# delete produto pelo o id
with st.expander('delete um produto'):
    id01 = st.text_input('digite o código do produto', placeholder='qual o código do produto')

    btndelete = st.button('deletar')
    if btndelete:
        delete_produto = fc.deletarProduto(id01)


with containerlista:
    listaprodutos = fc.selecionarTodosProdutos()

    tabela = pd.DataFrame(listaprodutos, columns=('id', 'nome', 'preço'))
    st.dataframe(tabela)


col3, col4 = st.columns(2)
containerumproduto = col3.container(border=True)


with containerumproduto:
    containerumproduto.markdown('## listar um produto')
    codigodoproduto = 