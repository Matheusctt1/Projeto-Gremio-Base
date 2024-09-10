# Plotar grafico de impacto

import streamlit as st
import pandas as pd
import services.dataBase as db
import numpy as np
import matplotlib.pyplot as plt
from adjustText import adjust_text

def plotarGrafico(x, y, tamanho, atletas):
    #with st.container(border=True):

        x = np.array(x)
        y = np.array(y)
        tamanho = np.array(tamanho)

        deslocamento_x = 4
        deslocamento_y = 4
        x_rótulos = x + np.random.uniform(-deslocamento_x, deslocamento_x, size=len(x))
        y_rótulos = y + np.random.uniform(-deslocamento_y, deslocamento_y, size=len(y))

        fig, ax = plt.subplots(figsize=(8, 4.8))  # Largura de 12 polegadas e altura de 8 polegadas

        # Criar o gráfico de dispersão
        ax.scatter(x + 0.08, y - 0.1, s=tamanho*2, c='gray', alpha=0.25, edgecolor='none')
        scatter = ax.scatter(x, y, s=tamanho*2, c= '#3e8ed0', edgecolor = 'black', linewidth=0.3)
        
        for i in range(len(x)): 
            ax.plot([x[i], x_rótulos[i]], [y[i], y_rótulos[i]], color='black', linestyle='-', linewidth=0.4)

        # Adicionar os rótulos e armazenar em uma lista para ajuste posterior
        texts = [ax.text(x_rótulos[i], y_rótulos[i], atletas[i], fontsize=6, ha='center') for i in range(len(x))]

        # Ajustar os rótulos para evitar sobreposição
        adjust_text(texts, avoid_self=True)

    

        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(True, which='major', linestyle='-', linewidth=1, color='black')
                
        Xmax = max(x-3)
        Xmin = min(x+3)
        Ymax = max(y-3)
        Ymin = min(y+3)

        ax.set_ylim(Ymin - 8, Ymax + 8)  # Limitando o eixo x de 0 a 105
        ax.set_xlim(Xmin - 8, Xmax + 8) 
        
        titleFont = {
            'family': 'sans-serif',
            'weight': 'normal',
            'size': 10,
        }
        plt.title(' Gráfico de Impacto', fontdict=titleFont)

        axesFont = {
            'family': 'sans-serif',
            'weight': 'normal',
            'size': 8,
        }
        plt.xlabel('Nota Ofensiva', fontdict=axesFont)
        plt.ylabel('Nota Defensiva', fontdict=axesFont)

        st.pyplot(fig)



def graficoImpacto():
    def init_connection():
        return db.cnxn

    conn = init_connection()

    verificaBanco = "SELECT COUNT([Adversario+data]) FROM BANCO_DE_DADOS_INDIVIDUAL3;"
    bancoVerificado = pd.read_sql(verificaBanco, conn)
    
    query = "SELECT [Adversario+data], [Atleta], [Tempo em jogo], [Nota final], [Nota defensiva], [Nota ofensiva]  FROM BANCO_DE_DADOS_INDIVIDUAL3;"
    df = pd.read_sql(query, conn)
    

    filtro_adversario = df["Adversario+data"]


    with st.sidebar.container(border=True, height=500):
        st.header('Filtros', divider='gray')
        if bancoVerificado.values == 0:
            st.error("Erro!!! Não foi possivel encontrar jogos cadastrados. Revise seu Banco de dados.")
        adversario_filtrado = st.multiselect(
            'Selecione o Adversario:',
            options=filtro_adversario.unique(), 
            placeholder='Selecione uma Opção'
        )
        
        if st.button('Gerar novamente'):
            st.rerun
        if adversario_filtrado:
            df_filtered = df[df['Adversario+data'].isin(adversario_filtrado)]
        else:
            df_filtered = pd.DataFrame()
    
    
    if df_filtered.empty:
        if adversario_filtrado == None:
                st.error("Selecione um adversario.")

    else:
        
        filtro_atleta = df_filtered[df_filtered.duplicated(keep=False)]["Atleta"].unique()
        df_filtered['Nota final'] = df_filtered['Nota final'].astype(float)
        atletasFiltrados = []
        tempo_em_jogo = []
        notas_ofensivas = []
        notas_defensivas = []
        notas_finais = []
        for atleta in filtro_atleta:
            atletasFiltrados.append(atleta)
            tempo_em_jogo.append(sum(df_filtered[df_filtered['Atleta'] == atleta]['Tempo em jogo']))
            notas_ofensivas.append(np.mean(df_filtered[df_filtered['Atleta'] == atleta]['Nota ofensiva']))
            notas_defensivas.append(np.mean(df_filtered[df_filtered['Atleta'] == atleta]['Nota defensiva']))
            notas_finais.append(np.mean(df_filtered[df_filtered['Atleta'] == atleta]['Nota final']))
       
        plotarGrafico(notas_ofensivas, notas_defensivas, tempo_em_jogo, atletasFiltrados)

        # Criar um DataFrame usando arrays
        df_tabelas = pd.DataFrame({
            'Atleta': atletasFiltrados,
            'Nota final': notas_finais,
            'Nota ofensiva': notas_ofensivas,
            'Nota defensiva' : notas_defensivas
        })

        st.divider()

        table1, table2, table3 = st.columns(3)

        with table1:
            st.header("Nota Geral", divider='gray')
            st.data_editor(df_tabelas, key=1,hide_index=True, column_order=['Atleta', 'Nota final'],width=400, height=840, column_config={
                    "Atleta": st.column_config.Column(label='Atletas'),
                    "Nota final": st.column_config.Column(label='Nota Geral')
            })

        with table2:
            st.header("Nota Ofensiva", divider='gray')
            st.data_editor(df_tabelas, key=2,hide_index=True, column_order=['Atleta', 'Nota ofensiva'],width=400, height=840, column_config={
                    "Atleta": st.column_config.Column(label='Atletas'),
                    "Nota ofensiva": st.column_config.Column(label='Nota Ofensiva')
            })


        with table3:
            st.header("Nota Defensiva", divider='gray')
            st.data_editor(df_tabelas, key=3, hide_index=True, column_order=['Atleta', 'Nota defensiva'],width=400, height=840, column_config={
                    "Atleta": st.column_config.Column(label='Atletas'),
                    "Nota defensiva": st.column_config.Column(label='Nota Defensiva')
            })

