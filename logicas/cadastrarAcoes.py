import streamlit as st
import controles.controleAcao as controleAcao
import classes.acao as acao
import logicas.definicaoVariaveis as definicaoVariaveis
import time
def verificaEixo(valList):
    XV = []
    separados = []
    for x in valList:
        if isinstance(x, str):
            separados = x.split(',')
            for valor in separados:
                XV.append(int(valor))
        else:
            XV.append(x)
    
    return XV


def realizarCadastros(infoJogo, infoColetivo, atleta, listaGoleiros,  passeCertoTempoEmJogo, passeCertoTempoEmJogoGo, tipoAcao, tipoAcaoGo, X, Y):
    adversarioData = infoJogo[0]
    h = 0
    MCDTotal = 0 
    MCOTotal = 0 
    intercepTotal = 0
    loading = 0
    loadingGo = 0
    count = len(atleta)
    countGo = len(listaGoleiros)
    p = 0

    for tipoDaAcao in tipoAcao:
        j = 0
        while(j < len(tipoDaAcao)):
            tipoDaAcao2 = tipoDaAcao[j]
            if(tipoDaAcao2 == 'MUDANÇA DE COMPORTAMENTO DEFENSIVA'):
                MCDTotal += 1
            if(tipoDaAcao2 == 'MUDANÇA DE COMPORTAMENTO OFENSIVA'):
                MCOTotal += 1
            if(tipoDaAcao2 == 'INTERCEPTAÇÃO'):
                intercepTotal += 1
                
            j += 1
        
    for tipoDaAcao, eixoX, eixoY in zip(tipoAcao, X, Y):
        eixoXV = verificaEixo(eixoX)
        eixoYV = verificaEixo(eixoY)
        atleta2 = atleta[h]
        passeCertoTempoEmJogo2 = passeCertoTempoEmJogo[h]
        loading += 1
        i = 0
        while(i != len(eixoX)):
            eixoX2 = eixoXV[i]
            eixoY2 = eixoYV[i]
            
            tipoDaAcao2 = tipoDaAcao[i]
            i += 1
            
            controleAcao.cadastrarAcao(acao.acao(adversarioData, atleta2, tipoDaAcao2, eixoX2, eixoY2))
        
        
        definicaoVariaveis.cadastroBancoIndividual(infoJogo, infoColetivo, atleta2, tipoDaAcao, passeCertoTempoEmJogo2, MCDTotal, MCOTotal, intercepTotal)
        h += 1
    if (loading == count):
        st.write("Realizando Cadastro BD. Individual...")
        time.sleep(2)
                

    k = 0
    for goleiros in listaGoleiros:
        passeCertoTempoEmJogoGo2 = passeCertoTempoEmJogoGo[k]
        tipoAcaoGo2 = tipoAcaoGo[k]
        loadingGo += 1
        #cadastrarGoleiro.cadastroBanco(infoJogo, goleiros, tipoAcaoGo2, passeCertoTempoEmJogoGo2)
        k += 1
    if (loadingGo == countGo):
        st.write("Realizando Cadastro BD. Goleiros...")
        time.sleep(2)