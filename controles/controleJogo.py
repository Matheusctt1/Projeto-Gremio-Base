import streamlit as st
import services.dataBase as db
import pandas as pd
import streamlit as st
import pandas as pd



def cadastrar(jogo):
       query = """
       INSERT INTO BD_INDIVIDUAL ([Adversario+data],[Nivel de jogo],[Data],[Campeonato],[Categoria],[Referencia],[Tempo de jogo],[Atleta],
              [Posição],[Tempo em jogo],[Gol],[Finalização no gol],[Finalização pra fora],[Finalização bloqueada],[Assistencia para finalização],
              [Assistencia para gol],[Chance clara],[Bloqueio de finalização],[Intercepção],[Desarme certo],[Desarme errado],[Falta],[Drible certo],
              [Perda da bola],[Falta sofrida],[Passe certo],[Passe errado],[Passe vertical],[Passe vertical errado],[Passe longo],[Passe longo errado],
              [Cruzamento],[Cruzamento errado],[Vitória jogo aéreo],[Derrota jogo aéreo],[Mudança de comportamento defensiva],[Mudança de comportamento ofensiva],
              [Nota final],[Criacoes],[Confront],[Complet],[Nota ofensiva],[Nota defensiva])
       VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
       valores = (jogo.adversarioData, jogo.nivelJogo, jogo.dataJogo, jogo.campeonato, jogo.categoria, jogo.referencia, jogo.tempoTotalJogo,
       jogo.atleta, jogo.posicao, jogo.tempo_em_jogo, jogo.gol, jogo.finaGol, jogo.finaFora, jogo.finaBloq, jogo.assistFina, jogo.assistGol, 
       jogo.chanceClara, jogo.bloqFina, jogo.interceptacao, jogo.desarmeCerto, jogo.desarmeErrado, jogo.falta, jogo.dribleCerto, jogo.perdaBola, 
       jogo.faltaSofrida, jogo.passeCerto, jogo.passeErrado, jogo.passeVert, jogo.passeVertErra, jogo.passeLongo, jogo.passeLongoErra, jogo.cruzamento,
       jogo.cruzamentoErra, jogo.vitoriaAereo, jogo.derrotaAereo, jogo.MCD, jogo.MCO, jogo.notaFinal, jogo.criacoes, jogo.confront, jogo.complet, 
       jogo.nota_ofensiva, jogo.nota_defensiva)
       
       db.cursor.execute(query, valores)
       db.cnxn.commit()
       
def acessarBanco():
       def init_connection():
              return db.cnxn

       conn = init_connection()

       return conn

def mostrarBanco():
       def init_connection():
              return db.cnxn

       conn = init_connection()


       query = 'SELECT * FROM BD_INDIVIDUAL'
       df = pd.read_sql(query, conn)
       df['Data'] = pd.to_datetime(df.Data)
       df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')
       st.data_editor(df, key=1,hide_index=True, height=600)
                        
       return df

def excluir(listId):
       for id in listId:
              count = db.cursor.execute("""
              DELETE FROM BD_INDIVIDUAL WHERE [ID] = ?""", id)
              db.cnxn.commit()
              st.rerun



def filtrar(adv):
       def init_connection():
              return db.cnxn  

       conn = init_connection()
       
       query = f"SELECT * FROM BD_INDIVIDUAL WHERE [Adversario+data] = '{adv[0]}'"
   
       df = pd.read_sql(query, conn)

       df['Data'] = pd.to_datetime(df['Data'])
       df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')
       st.data_editor(df, key=2, hide_index=True, height=600)

       return df
       