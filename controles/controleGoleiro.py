import streamlit as st
import services.dataBase as db
import pandas as pd



def cadastrarGoleiro(goleiro):
    
    count = db.cursor.execute("""
    INSERT INTO BD_GOLEIROS ([Adversario+data],[Nivel de jogo],[Data],[Campeonato],[Categoria],[Referencia],[Tempo de jogo]
                            ,[Goleiros],[Tempo em jogo],[Cobertura certa],[Cobertura errada],[Defesa dificil],[Defesa rebote]
                            ,[Defesa sem rebote],[Falha],[Gol sofrido],[Passes certos],[Reposição rapida],[Assistência],[Reposição curta certa],[Reposição curta errada]
                            ,[Reposição media certa],[Reposição media errada],[Reposição longa certa],[Reposição longa errada]
                            ,[Saida aerea certa],[Saida aerea errada])
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
    goleiro.adversarioData, goleiro.nivelJogo, goleiro.dataJogo, goleiro.campeonato, goleiro.categoria, goleiro.referencia, 
    goleiro.tempoTotalJogo, goleiro.goleiro, goleiro.tempoEmJogo, goleiro.coberturaCerta, goleiro.coberturaErrada, goleiro.defesaDificil, goleiro.defesaRebote, goleiro.defesaSemRebote, 
    goleiro.falha, goleiro.golSofrido, goleiro.passesCertos, goleiro.reposicaoRapida, goleiro.assistencia, goleiro.reposicaoCurtaCerta, goleiro.reposicaoCurtaErrada, goleiro.reposicaoMediaCerta, 
    goleiro.reposicaoMediaErrada, goleiro.reposicaoLongaCerta, goleiro.reposicaoLongaErrada, goleiro.saidaAereaCerta, goleiro.saidaAereaErrada).rowcount
    db.cnxn.commit()

def mostrarBanco():
       def init_connection():
              return db.cnxn

       conn = init_connection()


       query = 'SELECT * FROM BD_GOLEIROS'
       df = pd.read_sql(query, conn)
       df['Data'] = pd.to_datetime(df.data)
       df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')
       st.data_editor(df, key=2,hide_index=True, height=600)
       return df

def excluir(listId):
       for id in listId:
              count = db.cursor.execute("""
              DELETE FROM BD_GOLEIROS WHERE [ID] = ?""", id)
              db.cnxn.commit()

              st.rerun