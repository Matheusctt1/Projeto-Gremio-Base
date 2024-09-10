

import controles.controleColetivo as controleColetivo
import classes.coletivo as coletivo

def cadastrarColetivo(infoColetivo, adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo, gol, finaGol,
                finaFora, finaBloq, assistFina, assistGol, chanceClara, bloqFina, intercep, desarmeCerto, desarmeErrado, dribleCerto,
                perdaBola, passeCerto, passeErrado, passeVertical, passeVerticalErrado, passeLongo, passeLongoErra, cruzamento, 
                cruzamentoErrado, vitoriaAereo, derrotaAereo, MCD, MCO): 

    k = 0
    posseGeral = infoColetivo[k]
    k += 1
    posseOfensiva = infoColetivo[k]
    k += 1
    posseMeio = infoColetivo[k]
    k += 1
    posseDefensiva = infoColetivo[k]
    k += 1
    finalizacaoOrg = infoColetivo[k]
    k += 1
    finalizacaoTR = infoColetivo[k]
    k += 1
    finalizacaoBP = infoColetivo[k]

        
    controleColetivo.cadastrarColetivo(coletivo.coletivo(adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo
                    ,gol, finaGol, finaFora, finaBloq, assistFina, assistGol, chanceClara, intercep,bloqFina, desarmeCerto, desarmeErrado
                    ,dribleCerto, perdaBola, passeCerto, passeErrado, passeVertical, passeVerticalErrado,passeLongo,passeLongoErra,cruzamento
                    ,cruzamentoErrado, vitoriaAereo, derrotaAereo, MCD, MCO, posseGeral, posseOfensiva
                    ,posseMeio, posseDefensiva, passeCerto, finalizacaoOrg, finalizacaoTR, finalizacaoBP))


    k = 0