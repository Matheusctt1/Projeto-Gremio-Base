
import controles.controleADV as controleADV
import classes.adversario as adversario

def cadastrarADV(infoJogo, infoADV): 
    adversarioData = infoJogo[0]
    nivelJogo = infoJogo[1]
    dataJogo = infoJogo[2]
    campeonato = infoJogo[3]
    categoria = infoJogo[4]
    referencia = infoJogo[5]
    tempoTotalJogo = infoJogo[6]
    k = 0
    posseGeral = infoADV[k]
    k += 1
    posseDefensiva = infoADV[k]
    k += 1
    posseMeio = infoADV[k]
    k += 1
    posseOfensiva = infoADV[k]
    k += 1
    gol = infoADV[k]
    k += 1
    fina = infoADV[k]
    k += 1
    finaGol = infoADV[k]
    k += 1
    chanceClara = infoADV[k]
    k += 1
    cruzaCerto = infoADV[k]
    k += 1
    cruzaErrado = infoADV[k]
    k += 1
    passeLongo = infoADV[k]
    k += 1
    passeLongoErrado = infoADV[k]
    k += 1
    passeCerto = infoADV[k]
    k += 1
    passeErrado = infoADV[k]
    k += 1
    finalizacaoOrg = infoADV[k]
    k += 1
    finalizacaoTR = infoADV[k]
    k += 1
    finalizacaoBP = infoADV[k]

        
    controleADV.cadastrarADV(adversario.adversario(adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo,
                                            gol, fina, finaGol, chanceClara, passeCerto, passeErrado, passeLongo, passeLongoErrado, cruzaCerto, 
                                            cruzaErrado, posseGeral, posseOfensiva, posseMeio, posseDefensiva, finalizacaoOrg, finalizacaoTR, 
                                            finalizacaoBP))


    k = 0