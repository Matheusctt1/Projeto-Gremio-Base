import services.dataBase as db
import pandas as pd




def cadastrarGoleiro(goleiro):
    query ="""
    INSERT INTO BD_GOLEIROINDV ([Data_de_Cadastro],[Goleiro],[vb_imagem])
    VALUES (?, ?, ?)
     """
    valores = (goleiro.dataCadastro, goleiro.nome, goleiro.file)
    db.cursor.execute(query, valores)
    db.cnxn.commit()

def exibirAtleta(nome):
    def init_connection():
            return db.cnxn

    conn = init_connection()


    query = f"""SELECT [vb_imagem] FROM [BD_GOLEIROINDV] WHERE [Goleiro] = '{nome}'"""
    df = pd.read_sql(query, conn)
                        
    return df