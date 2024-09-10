import services.dataBase as db

def cadastrarAcao(acao):
    query = """
    INSERT INTO BD_ACOES ([Adversario+Data],[Atleta],[Tipo de Ação],[X],[Y])
    VALUES (?, ?, ?, ?, ?)"""
    valores = (acao.advData, acao.atleta, acao.acao, acao.X, acao.Y)
    db.cursor.execute(query, valores)
    db.cnxn.commit()

