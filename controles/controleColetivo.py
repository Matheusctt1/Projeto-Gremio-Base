import streamlit as st
import services.dataBase as db
import pandas as pd

def cadastrarColetivo(coletivo):
    count = db.cursor.execute("""
    INSERT INTO BD_COLETIVO ([Adversario+data],[Nivel de jogo],[Data],[Campeonato],[Categoria],[Referencia],[Tempo de jogo],[Gol],[Finalização no gol]
    ,[Finalização pra fora],[Finalização bloqueada],[Assistencia para finalização],[Assistencia para gol],[Chance clara],[Bloqueio de finalização]
    ,[Intercepção],[Desarme certo],[Desarme errado],[Falta],[Drible certo],[Perda da bola],[Falta sofrida],[Passe certo],[Passe errado],[Passe vertical]
    ,[Passe vertical errado],[Passe longo],[Passe longo errado],[Cruzamento],[Cruzamento errado],[Vitória jogo aéreo],[Derrota jogo aéreo]
    ,[Mudança de comportamento defensiva],[Mudança de comportamento ofensiva],[Posse geral],[Posse ofensiva],[Posse meio],[Posse defensiva]
    ,[Finalizacao Org],[Finalizacao TR],[Finalizacao BP])
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
    coletivo.adversarioData, coletivo.nivelJogo, coletivo.dataJogo, coletivo.campeonato, coletivo.categoria, coletivo.referencia, coletivo.tempoTotalJogo,
    coletivo.gol, coletivo.finaGol, coletivo.finaFora, coletivo.finaBloq, coletivo.assistFina, coletivo.assistGol, coletivo.chanceClara, 
    coletivo.interceptacao, coletivo.bloqFina, coletivo.desarmeCerto, coletivo.desarmeErrado, coletivo.falta, coletivo.dribleCerto, coletivo.perdaBola,
    coletivo.faltaSofrida, coletivo.passeVert, coletivo.passeVertErrado, coletivo.passeCerto ,coletivo.passeErra, coletivo.passeLongo, coletivo.passeLongoErra, 
    coletivo.cruzamento, coletivo.cruzamentoErra, coletivo.vitoriaAereo, coletivo.derrotaAereo, coletivo.MCD, coletivo.MCO, coletivo.posseGeral,
    coletivo.posseOfensiva,coletivo.posseMeio,coletivo.posseDefensiva,coletivo.finalizacaoOrg,coletivo.finalizacaoTR,coletivo.finalizacaoBP).rowcount
    db.cnxn.commit()

def mostrarBanco():
    def init_connection():
            return db.cnxn

    conn = init_connection()


    query = 'SELECT * FROM BD_COLETIVO'
    df = pd.read_sql(query, conn)
    df['Data'] = pd.to_datetime(df.Data)
    df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')
    st.data_editor(df, key=3,hide_index=True, height=600,)
                        
    return df

def excluir(listId):
       for id in listId:
            count = db.cursor.execute("""
            DELETE FROM BD_COLETIVO WHERE [ID] = ?""", id)
            db.cnxn.commit()

            st.rerun