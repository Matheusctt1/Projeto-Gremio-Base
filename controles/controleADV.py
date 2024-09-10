import streamlit as st
import services.dataBase as db
import pandas as pd

def cadastrarADV(adversario):
    count = db.cursor.execute("""
    INSERT INTO BD_ADVERSARIO ([adversario+data],[nivel de jogo],[data],[campeonato],[categoria],[referencia],[tempo de jogo],[Gol],[Finalizaçõesl]
      ,[Finalizacao no gol],[chance clara],[passe certo],[passe errado],[passe longo],[passe longo errado],[cruzamento],[cruzamento incompleto]
      ,[posse geral],[posse ofensiva],[posse meio],[posse defensiva],[finalizacao Org],[finalizacao TR],[finalizacao BP])
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
    adversario.adversarioData, adversario.nivelJogo, adversario.dataJogo, adversario.campeonato, adversario.categoria, adversario.referencia, 
    adversario.tempoTotalJogo, adversario.gol, adversario.fina, adversario.finaGol, adversario.chanceClara, adversario.passeCerto ,adversario.passeErra, 
    adversario.passeLongo, adversario.passeLongoErra, adversario.cruzamento, adversario.cruzamentoErra, adversario.posseGeral, adversario.posseOfensiva,
    adversario.posseMeio,adversario.posseDefensiva,adversario.finalizacaoOrg,adversario.finalizacaoTR,adversario.finalizacaoBP).rowcount
    db.cnxn.commit()

def mostrarBanco():
    def init_connection():
            return db.cnxn

    conn = init_connection()


    query = 'SELECT * FROM BD_ADVERSARIO'
    df = pd.read_sql(query, conn)
    df['data'] = pd.to_datetime(df.data)
    df['data'] = df['data'].dt.strftime('%d/%m/%Y')
    st.data_editor(df, key=3,hide_index=True, height=600,)
                        
    return df

def excluir(listId):
       for id in listId:
            count = db.cursor.execute("""
            DELETE FROM BD_ADVERSARIO WHERE [ID] = ?""", id)
            db.cnxn.commit()

            st.rerun