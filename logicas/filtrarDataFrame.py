import streamlit as st
import pandas as pd
import logicas.cadastrarAcoes as cadastrarAcoes
import services.dataBase as db
import time

def verificarGoleiro(nome, conn):
    verificaBanco = f"""SELECT COUNT(*) FROM BD_GOLEIROINDV WHERE Goleiro = '{nome}'"""
    bancoVerificado = pd.read_sql(verificaBanco, conn)
    
    return bancoVerificado.iloc[0, 0] > 0
    

def filtrarDataFrame(infoJogo, infoColetivo, listaAtletas, listaGoleiros, df):
    
    def init_connection():
        return db.cnxn
    conn = init_connection()
    listaEixos = df.columns[1:].tolist()
    count = len(listaEixos)
    Y = []
    X = []
    YGo = []
    XGo = []
    tipoAcao = []
    tipoAcaoGo = []
    i= 0 

    while(i < count):
        eixo = listaEixos[i]
        posicao = eixo[0:1]
        if (eixo == 'PASSE CERTO'):
            i = count + 1
        else:        
            if verificarGoleiro(eixo[2:], conn):
                if(posicao == 'X'): 
                    valores_colunas = [df[eixo].dropna().tolist()]
                    filtered_df = df[df[eixo].notna()]
                    tipoAcaoGo.append(filtered_df['Row'].tolist())
                    for valores in valores_colunas:
                        if valores is str:
                            valores = valores.split(',', 1)
                            XGo.append(valores)
                        if valores is not None:
                            XGo.append(valores)

                if(posicao == 'Y'):
                    valores_colunas = [df[eixo].dropna().tolist()]
                    for valores in valores_colunas:
                        if valores is str:
                            valores = valores.split(',', 1)
                            YGo.append(valores)
                        if valores is not None:
                            YGo.append(valores)
                i += 1
                continue
            
            if(posicao == 'X'): 
                valores_colunas = [df[eixo].dropna().tolist()]
                filtered_df = df[df[eixo].notna()]
                tipoAcao.append(filtered_df['Row'].tolist())
                for valores in valores_colunas:
                    if valores is str:
                        valores = valores.split(',', 1)
                        X.append(valores)
                    if valores is not None:
                        X.append(valores)

            if(posicao == 'Y'):
                valores_colunas = [df[eixo].dropna().tolist()]
                for valores in valores_colunas:
                    if valores is str:
                        valores = valores.split(',', 1)
                        Y.append(valores)
                    if valores is not None:
                        Y.append(valores)
 
        i += 1 
    passeCertoTempoEmJogo = []
    passeCertoTempoEmJogoGo = []
    j = 0
    while (j < len(listaAtletas)):
        valoresPasse = [df[listaAtletas[j]].dropna().tolist()]
        for valor in valoresPasse:
            if valor is not None:
                passeCertoTempoEmJogo.append(valor)
        j += 1
    
    k = 0
    while (k < len(listaGoleiros)):
        valoresPasse = [df[listaGoleiros[k]].dropna().tolist()]
        for valor in valoresPasse:
            if valor is not None:
                passeCertoTempoEmJogoGo.append(valor)
        k += 1
    st.write("Filtrando Informações do XLS...")
    time.sleep(2)
    
    cadastrarAcoes.realizarCadastros(infoJogo, infoColetivo, listaAtletas, listaGoleiros,  passeCertoTempoEmJogo, passeCertoTempoEmJogoGo, tipoAcao, tipoAcaoGo, X, Y)
    
    
    