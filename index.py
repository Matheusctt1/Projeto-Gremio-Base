# Pagina de rosto do App

import streamlit as st
st.set_page_config(
    page_title='CDD.BASE',
    page_icon='.\\imagens\\icone_pagina.png',
    layout="wide",
    initial_sidebar_state='auto'
)
import page.pageCadastroIndividual as cadastroBancoIndividual
import page.paginaInicial as paginaInicial
import page.pageAtletas as PageAtletas
import page.teste as teste
import page.testeDashboards as dashboard

st.sidebar.header('Menu')

Page_cliente = st.sidebar.selectbox(
    'Ferramentas', ['Pagina Inicial', 'Cadastro Banco de Dados', 'Cadastro Atletas', 'Dashboard'], 0)

if Page_cliente == 'Pagina Inicial':
  paginaInicial.exibirPagina()

if Page_cliente == 'Cadastro Banco de Dados':
  cadastroBancoIndividual.cadastrar()

if Page_cliente  == 'Cadastro Atletas':
  PageAtletas.cadastrar()

if Page_cliente == 'Dashboard':
  dashboard.filtrarGraficos()

with st.sidebar.container(border=None):
        st.sidebar.image(image='.\\imagens\\simbolo gremio.png', width=220)



