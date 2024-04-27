import streamlit as st

st.title('TÍTULO')

st.write('escreve esse texto')

escolha = st.selectbox('selecione o turno de interesse:',
                       ['manhã', 'tarde', 'noite'])
if escolha:
    st.write(escolha)

alternativa = st.radio('escolha uma opção',
         ['manhã', ' tarde', 'noite'])

texto = st.text_input('digite seu vulgo:')
if texto:
    st.write(texto)

numero = st.number_input('digite um numero:')

cpf = st.text_input('digite seu cpf:', placeholder='000.000.000-00' )

btncadastrar = st.button('gostaria de avaliar')
if btncadastrar:
    st.write(btncadastrar)

    textobig = st.text_area('digite sua avaliação:')