import controles.controleGoleiro as controleGoleiro
import classes.goleiro as jogo



def cadastroBanco(infoJogo, listaGoleiros, tipoAcao, passeCertoTempoEmJogo):
    adversarioData = infoJogo[0]
    nivelJogo = infoJogo[1]
    dataJogo = infoJogo[2]
    campeonato = infoJogo[3]
    categoria = infoJogo[4]
    referencia = infoJogo[5]
    tempoTotalJogo = infoJogo[6]
    
    goleiro = listaGoleiros
    coberturaCerta = 0
    coberturaErrada = 0
    defesaDificil = 0
    defesaRebote = 0
    defesaSemRebote = 0
    falha = 0
    golSofrido = 0
    reposicaoRapida = 0
    reposicaoCurtaCerta = 0
    reposicaoCurtaErrada = 0
    reposicaoMediaCerta = 0
    reposicaoMediaErrada = 0 
    reposicaoLongaCerta = 0
    reposicaoLongaErrada = 0
    saidaAereaCerta = 0
    saidaAereaErrada = 0
    

    listaDeAcoes = ['COBERTURA CERTA','COBERTURA ERRADA','DEFESA DIFÍCIL','DEFESA REBOTE',
                    'DEFESA SEM REBOTE','FALHA','GOL SOFRIDO','REPOSIÇÃO RÁPIDA','REPOSIÇÃO CURTA CERTA',
                    'REPOSIÇÃO CURTA ERRADA','REPOSIÇÃO MÉDIA CERTA','REPOSIÇÃO MÉDIA ERRADA',
                    'REPOSIÇÃO LONGA CERTA','REPOSIÇÃO LONGA ERRADA','SAÍDA AÉREA CERTA','SAÍDA AÉREA ERRADA']

    for acao in tipoAcao:
    
        if (acao == listaDeAcoes[0]):  
            coberturaCerta += 1
        if (acao == listaDeAcoes[1]): 
            coberturaErrada += 1 
        if (acao == listaDeAcoes[2]): 
            defesaDificil += 1 
        if (acao == listaDeAcoes[3]):  
            defesaRebote += 1
        if (acao == listaDeAcoes[4]):  
            defesaSemRebote += 1
        if (acao == listaDeAcoes[5]):
            falha += 1  
        if (acao == listaDeAcoes[6]):
            golSofrido += 1  
        if (acao == listaDeAcoes[7]):
            reposicaoRapida += 1  
        if (acao == listaDeAcoes[8]):
            reposicaoCurtaCerta += 1  
        if (acao == listaDeAcoes[9]):
            reposicaoCurtaErrada += 1  
        if (acao == listaDeAcoes[10]):
            reposicaoMediaCerta += 1  
        if (acao == listaDeAcoes[11]):
            reposicaoMediaErrada += 1  
        if (acao == listaDeAcoes[12]):
            reposicaoLongaCerta += 1  
        if (acao == listaDeAcoes[13]):
            reposicaoLongaErrada += 1  
        if (acao == listaDeAcoes[14]):  
            saidaAereaCerta += 1
        if (acao == listaDeAcoes[15]):
            saidaAereaErrada += 1  
    
    controleGoleiro.cadastrarGoleiro(jogo.goleiro(adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo,
                                        goleiro, passeCertoTempoEmJogo[1], coberturaCerta, coberturaErrada, defesaDificil, defesaRebote, defesaSemRebote,
                                        falha, golSofrido, passeCertoTempoEmJogo[0], reposicaoRapida, reposicaoCurtaCerta, reposicaoCurtaErrada, reposicaoMediaCerta,
                                        reposicaoMediaErrada, reposicaoLongaCerta, reposicaoLongaErrada, saidaAereaCerta, saidaAereaErrada))

