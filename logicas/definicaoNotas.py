import services.notas as nota
import controles.controleJogo as controle
import classes.jogo as jogo

def obter_limites(posicao):
    limites = {
        'ZAGUEIRO': {'criacao': 30, 'confronto': 75, 'complet': 45, 'ofensiva': 66, 'defensiva': 57},
        'LATERAL': {'criacao': 50, 'confronto': 65, 'complet': 35, 'ofensiva': 90.5, 'defensiva': 36},
        'VOLANTE': {'criacao': 50, 'confronto': 65, 'complet': 35, 'ofensiva': 91, 'defensiva': 37},
        'MEIO CAMPO': {'criacao': 65, 'confronto': 55, 'complet': 30, 'ofensiva': 110.5, 'defensiva': 21.5},
        'EXTREMA': {'criacao': 65, 'confronto': 55, 'complet': 30, 'ofensiva': 113, 'defensiva': 21.5},
        'CENTROAVANTE': {'criacao': 70, 'confronto': 50, 'complet': 30, 'ofensiva': 112, 'defensiva': 15.5}
    }
    return limites.get(posicao, {'criacao': 0, 'confronto': 0, 'complet': 0, 'ofensiva': 0, 'defensiva': 0})

def calcular_nota_final(notaFinal, nivelJogo):
    if nivelJogo == '2':
        notaFinal -= (10 * notaFinal) / 100
    elif nivelJogo == '3':
        notaFinal -= (5 * notaFinal) / 100
    elif nivelJogo == '5':
        notaFinal += (5 * notaFinal) / 100
    
    return min(notaFinal, 10) if notaFinal >= 100 else notaFinal / 10

def calcularNotas(adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo, atleta, posicao, gol, finaGol,
                   finaFora, finaBloq, assistFina, assistGol, chanceClara, bloqFina, intercep, desarmeCerto, desarmeErrado, falta, dribleCerto,
                   perdaBola, faltaSofrida, passeCerto, passeErrado, passeVertical, passeVerticalErrado, passeLongo, passeLongoErrado, cruzamento, 
                   cruzamentoErrado, vitoriaAereo, derrotaAereo, MCD, MCO, tempoEmJogo, MCDTotal, MCOTotal, intercepTotal):

    limites = obter_limites(posicao)
    
    valoresConfront = nota.confront(posicao, passeCerto, passeErrado, passeVertical, passeVerticalErrado, passeLongo, 
                                    passeLongoErrado, desarmeCerto, desarmeErrado, dribleCerto, perdaBola, vitoriaAereo, 
                                    derrotaAereo, cruzamento, cruzamentoErrado, falta, faltaSofrida)
    valoresCriacoes = nota.criacoes(posicao, gol, finaGol, finaFora, finaBloq, chanceClara, assistFina, assistGol)
    valoresComplet = nota.complet(posicao, MCD, MCO, intercep, bloqFina, MCDTotal, MCOTotal, intercepTotal)
    valoresOfensivos = nota.ofensivas(posicao, gol, finaGol, finaFora, finaBloq, chanceClara, assistFina, assistGol,
                                      dribleCerto, perdaBola, passeCerto, passeErrado, passeVertical, passeVerticalErrado,
                                      passeLongo, passeLongoErrado, cruzamento, cruzamentoErrado, MCO, MCOTotal)
    valoresDefensivos = nota.defensivas(posicao, bloqFina, intercep, intercepTotal, desarmeCerto, desarmeErrado, MCD, MCDTotal)

    criacoes = (valoresCriacoes.assistFina + valoresCriacoes.assistGol + valoresCriacoes.chanceClara + valoresCriacoes.finaBloq
                + valoresCriacoes.finaFora + valoresCriacoes.finaGol) 

    confront = (valoresConfront.Ncruzamento + valoresConfront.NpasseLongo + valoresConfront.NpasseVertical + valoresConfront.Ndrible
                + valoresConfront.Ndesarme + valoresConfront.NvitoriaAereo)

    complet = valoresComplet.Nbloqfina + valoresComplet.Nintercep + valoresComplet.NMCD + valoresComplet.NMCO 

    criacoes = min(criacoes, limites['criacao']) + valoresCriacoes.gol
    confront = min(confront, limites['confronto'])
    complet = min(complet, limites['complet'])

    notaFinal = criacoes + confront + complet
    notaFinal = calcular_nota_final(notaFinal, nivelJogo)

    nota_ofensiva = ((valoresOfensivos.gol + valoresOfensivos.finaGol + valoresOfensivos.finaFora + valoresOfensivos.finaBloq + 
                      valoresOfensivos.chanceClara + valoresOfensivos.assistFina + valoresOfensivos.assistGol +
                      valoresOfensivos.drible + valoresOfensivos.passeCerto + valoresOfensivos.passeVertical +
                      valoresOfensivos.passeLongo + valoresOfensivos.cruzamento + valoresOfensivos.MCO) / limites['ofensiva']) * 100

    nota_defensiva = ((valoresDefensivos.bloqfina + valoresDefensivos.intercep + valoresDefensivos.desarme + valoresDefensivos.MCD) / limites['defensiva']) * 100

    nota_ofensiva = min(nota_ofensiva, limites['ofensiva']) / 10
    nota_defensiva = min(nota_defensiva, limites['defensiva']) / 10

    controle.cadastrar(jogo.jogo(adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo,
                                  atleta, posicao, tempoEmJogo, gol, finaGol, finaFora, finaBloq, assistFina, assistGol,
                                  chanceClara, bloqFina, intercep, desarmeCerto, desarmeErrado, falta, dribleCerto, perdaBola, faltaSofrida,
                                  passeCerto, passeErrado, passeVertical, passeVerticalErrado, passeLongo, passeLongoErrado, 
                                  cruzamento, cruzamentoErrado, vitoriaAereo, derrotaAereo, MCD, MCO, round(notaFinal, 1), criacoes, 
                                  confront, complet, round(nota_ofensiva, 1), round(nota_defensiva, 1)))
