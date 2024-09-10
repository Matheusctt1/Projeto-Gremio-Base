import streamlit as st
import pandas as pd
import plotly.express as px
import services.dataBase as db

def teste():
    def init_connection():
        return db.cnxn

    conn = init_connection()

    query = "SELECT [adversario+data], [atleta], [tempo_em_jogo], [notaFinal], [nota_defensiva], [nota_ofensiva]  FROM BANCO_DE_DADOS_INDIVIDUAL3;"
    df = pd.read_sql(query, conn)

    filtro_adversario = df["adversario+data"]

    with st.sidebar.container(border=True, height=500):
        st.header('Filtros', divider='gray')

        adversario_filtrado = st.selectbox(
            'Selecione o Adversario:',
            options=filtro_adversario.unique(), 
            placeholder='Selecione uma Opção'
        )

    df_filtered = df[(df['adversario+data'] == adversario_filtrado) ] 
    if df_filtered.empty:
        st.error("Erro!!! Aparentemente seu banco de dados esta vazio. Tente fazer um cadastro e após isso, retorne para gerar o gráfico.")
    else:
        notas_defensivas = df_filtered["nota_defensiva"] 
        notas_ofensivas = df_filtered["nota_ofensiva"]
        tempo_em_jogo = df_filtered["tempo_em_jogo"]
        filtro_atleta = df_filtered["atleta"]



        with st.container(border=True):
            st.header('Gráfico de Impacto', divider='gray')

            grafico_impacto = px.scatter(x=notas_ofensivas,
                                        y=notas_defensivas,
                                        size= tempo_em_jogo,
                                        text= filtro_atleta,
                                        title= 'Grafico de Impacto',
                                        height= 600)
    
            grafico_impacto.update_traces(marker_size = tempo_em_jogo * 10,textposition= 'middle center')
            grafico_impacto.update_layout(xaxis_title='Nota Ofensiva', 
                                        yaxis_title='Nota Defensiva',
                                        xaxis=dict(
                                            tickmode='array',
                                            tickvals=[],  # Lista vazia para ocultar os valores do eixo x
                                            ),
                                        yaxis=dict(
                                            tickmode='array',
                                            tickvals=[],  # Lista vazia para ocultar os valores do eixo y
                                            )
                                        )

            
            st.plotly_chart(grafico_impacto, use_container_width=True)


            df_filtered_table = df[(df['adversario+data'] == adversario_filtrado)]
            df_filtered_table = pd.DataFrame(df_filtered_table, columns=['atleta', 'notaFinal', 'nota_defensiva', 'nota_ofensiva'])

            st.divider()

            table1, table2, table3 = st.columns(3)

            with table1:
                st.header("Nota Geral", divider='gray')
                st.data_editor(df_filtered_table, key=1,hide_index=True, column_order=['atleta', 'notaFinal'],width=400, height=840, column_config={
                        "atleta": st.column_config.Column(label='Atletas'),
                        "notaFinal": st.column_config.Column(label='Nota Geral')
                })

            with table2:
                st.header("Nota Ofensiva", divider='gray')
                st.data_editor(df_filtered_table, key=2,hide_index=True, column_order=['atleta', 'nota_ofensiva'],width=400, height=840, column_config={
                        "atleta": st.column_config.Column(label='Atletas'),
                        "nota_ofensiva": st.column_config.Column(label='Nota Ofensiva')
                })


            with table3:
                st.header("Nota Defensiva", divider='gray')
                st.data_editor(df_filtered_table, key=3, hide_index=True, column_order=['atleta', 'nota_defensiva'],width=400, height=840, column_config={
                        "atleta": st.column_config.Column(label='Atletas'),
                        "nota_defensiva": st.column_config.Column(label='Nota Defensiva')
                })

