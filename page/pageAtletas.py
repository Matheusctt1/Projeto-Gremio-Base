import streamlit as st
from streamlit import session_state
import controles.controleGoleiroIndv as controleGoleiro
import classes.goleiroIndv as goleiro
import controles.controleAtleta as controleAtleta
import classes.atleta as atleta
import time
from datetime import date
import services.dataBase as db
import pandas as pd

def mostrarBanco():
       def init_connection():
              return db.cnxn

       conn = init_connection()


       query = 'SELECT * FROM bd_atletas'
       df = pd.read_sql(query, conn)
       st.data_editor(df, key=1,hide_index=True, height=600)
                        
       return df

def init_connection():
    return db.cnxn

def verificarBDAtletas(nome, conn):
    verificaBanco = f"""SELECT COUNT(*) FROM BD_ATLETAS WHERE Atleta = '{nome}'"""
    bancoVerificado = pd.read_sql(verificaBanco, conn)
    return bancoVerificado.iloc[0, 0] > 0

def verificarBDGoleiro(nome, conn):
    verificaBanco = f"""SELECT COUNT(*) FROM  BD_GOLEIROINDV WHERE Goleiro = '{nome}'"""
    bancoVerificado = pd.read_sql(verificaBanco, conn)
    return bancoVerificado.iloc[0, 0] > 0

def cadastrar():
    tab1, tab2 = st.tabs(["Cadastrar Atletas", "Cadastrar Goleiros"])
    data_atual = date.today()
    data_cadastro = data_atual.strftime('%d/%m/%Y')
    conn = init_connection()
    with tab1:
                with st.container():
                    st.title('Cadastro de Atletas')
                    nomeJogador = st.text_input('Insira o Nome do Jogador')

                    urlFoto = st.text_input('Insira a URL da foto do jogador')
                    st.caption('A URL da foto do jogador, pode ser encontrada no site da SGA, copiando o endereço da imagem do jogador.')
                                
                    button = st.button('Cadastrar Jogador')
                    if button:
                        if nomeJogador is None or nomeJogador == '':
                            st.error('Por favor, insira o nome do jogador')
                        if urlFoto is None or urlFoto == '':
                            st.error('Por favor, insira a URL da foto')
                        with st.spinner('Um momento..'):
                            time.sleep(3)
                            if verificarBDAtletas(nomeJogador, conn):
                                st.error("Esse jogador já está cadastrado.")
                            else:
                                controleAtleta.cadastrarAtleta(atleta.atleta(data_cadastro, nomeJogador, urlFoto))
                                st.success(f"Cadastro do Jogador: {nomeJogador}, concluído!")    
                                          
        
    with tab2:
                with st.container():
                    st.title('Cadastro de Goleiros')
                    nomeGoleiro = st.text_input('Insira o Nome do Goleiro')

                    urlFotoGo = st.text_input('Insira a URL da foto do Goleiro')
                    st.caption('A URL da foto do Goleiro, pode ser encontrada no site da SGA, copiando o endereço da imagem do jogador.')
                                
                    button = st.button('Cadastrar Goleiro')
                    if button:
                        if nomeGoleiro is None:
                            st.error('Por favor, insira o nome do Goleiro')
                        if urlFoto is None:
                            st.error('Por favor, insira a URL da foto')
                        with st.spinner('Um momento..'):
                            time.sleep(3)
                            if verificarBDGoleiro(nomeGoleiro, conn):
                                st.error("Esse Goleiro já está cadastrado.")
                            else:
                                controleGoleiro.cadastrarGoleiro(goleiro.goleiro(data_cadastro, nomeGoleiro, urlFotoGo))
                                st.success(f"Cadastro do Goleiro: {nomeGoleiro}, concluído!")
            

                        
                    
            