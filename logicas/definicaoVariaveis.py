import logicas.definicaoNotas as nota

def cadastroBancoIndividual(infoJogo, infoColetivo, atleta, acoes, passeCertoTempoEmJogo, MCDTotal, MCOTotal, intercepTotal):
    
    adversarioData = infoJogo[0]
    nivelJogo = infoJogo[1]
    dataJogo = infoJogo[2]
    campeonato = infoJogo[3]
    categoria = infoJogo[4]
    referencia = infoJogo[5]
    tempoTotalJogo = infoJogo[6]
    nomeAtleta = atleta
    posicao = passeCertoTempoEmJogo[0]
    passeCerto = passeCertoTempoEmJogo[1]
    tempoEmJogo = passeCertoTempoEmJogo[2]

    gol = 0 
    finaGol = 0  
    finaFora = 0  
    finaBloq = 0  
    assistFina = 0  
    assistGol = 0  
    chanceClara = 0 
    bloqFina = 0  
    intercep = 0  
    desarmeCerto = 0  
    desarmeErrado = 0  
    falta = 0
    dribleCerto = 0
    perdaBola = 0
    faltaSofrida = 0 
    passeErrado = 0  
    passeVertical = 0  
    passeVerticalErrado = 0  
    passeLongo = 0 
    passeLongoErra = 0  
    cruzamento = 0  
    cruzamentoErrado = 0  
    vitoriaAereo = 0  
    derrotaAereo = 0  
    MCD = 0  
    MCO = 0 

    TotalGol = 0 
    TotalFinaGol = 0  
    TotalFinaFora = 0  
    TotalFinaBloq = 0  
    TotalAssistFina = 0  
    TotalAssistGol = 0  
    TotalChanceClara = 0 
    TotalBloqFina = 0  
    TotalDesarmeCerto = 0  
    TotalDesarmeErrado = 0  
    TotalFalta = 0
    TotalDribleCerto = 0
    TotalPerdaBola = 0
    TotalFaltaSofrida = 0 
    TotalPasseCerto = 0
    TotalPasseErrado = 0  
    TotalPasseVertical = 0  
    TotalPasseVerticalErrado = 0  
    TotalPasseLongo = 0 
    TotalPasseLongoErra = 0  
    TotalCruzamento = 0  
    TotalCruzamentoErrado = 0  
    TotalVitoriaAereo = 0  
    TotalDerrotaAereo = 0 

    #TotalPasseCerto = sum(passeCerto)
    listaDeAcoes = ['GOL', 'FINALIZAÇÃO NO GOL', 'FINALIZAÇÃO PRA FORA', 'FINALIZAÇÃO BLOQUEADA', 
                'ASSISTÊNCIA P/FINALIZAÇÃO', 'ASSISTÊNCIA P/GOL', 'CHANCES CLARAS', 'BLOQUEIO DE FINALIZAÇÃO',
                'INTERCEPTAÇÃO', 'DESARME CERTO', 'DRIBLE SOFRIDO', 'FALTA', 'DRIBLE CERTO','PERDA DA BOLA', 
                'FALTA SOFRIDA', 'PASSE ERRADO', 'PASSE VERTICAL', 'PASSE VERTICAL ERRADO', 'PASSE LONGO', 
                'PASSE LONGO ERRADO', 'CRUZAMENTO', 'CRUZAMENTO ERRADO', 'VITÓRIA JOGO AÉREO', 'DERROTA JOGO AÉREO',
                'MUDANÇA DE COMPORTAMENTO DEFENSIVA','MUDANÇA DE COMPORTAMENTO OFENSIVA','TEMPO DE JOGO']
    #25 ações
    # Sem contar passe certo e contando tempo de jogo

    for tipoAcao in acoes:
    
        if (tipoAcao == listaDeAcoes[0]):  
            gol += 1
            TotalGol = gol + TotalGol
        if (tipoAcao == listaDeAcoes[1]): 
            finaGol += 1 
            TotalFinaGol = finaGol + TotalFinaGol
        if (tipoAcao == listaDeAcoes[2]): 
            finaFora += 1 
            TotalFinaFora = finaFora + TotalFinaFora
        if (tipoAcao == listaDeAcoes[3]):  
            finaBloq += 1
            TotalFinaBloq = finaBloq + TotalFinaBloq
        if (tipoAcao == listaDeAcoes[4]):  
            assistFina += 1
            TotalAssistFina = assistFina + TotalAssistFina
        if (tipoAcao == listaDeAcoes[5]):
            assistGol += 1  
            TotalAssistGol = assistGol + TotalAssistGol
        if (tipoAcao == listaDeAcoes[6]):
            chanceClara += 1 
            TotalChanceClara = chanceClara + TotalChanceClara 
        if (tipoAcao == listaDeAcoes[7]):
            bloqFina += 1  
            TotalBloqFina = bloqFina + TotalBloqFina
        if (tipoAcao == listaDeAcoes[8]):
            intercep += 1  
        if (tipoAcao == listaDeAcoes[9]):
            desarmeCerto += 1  
            TotalDesarmeCerto = desarmeCerto + TotalDesarmeCerto
        if (tipoAcao == listaDeAcoes[10]):
            desarmeErrado += 1  
            TotalDesarmeErrado = desarmeErrado + TotalDesarmeErrado
        if (tipoAcao == listaDeAcoes[11]):
            falta += 1  
            TotalFalta = falta + TotalFalta
        if (tipoAcao == listaDeAcoes[12]):
            dribleCerto += 1  
            TotalDribleCerto = dribleCerto + TotalDribleCerto
        if (tipoAcao == listaDeAcoes[13]):
            perdaBola += 1  
            TotalPerdaBola = perdaBola + TotalPerdaBola
        if (tipoAcao == listaDeAcoes[14]):
            faltaSofrida += 1  
            TotalFaltaSofrida = faltaSofrida + TotalFaltaSofrida
        if (tipoAcao == listaDeAcoes[15]):
            passeErrado += 1  
            TotalPasseErrado = passeErrado + TotalPasseErrado
        if (tipoAcao == listaDeAcoes[16]):  
            passeVertical += 1
            TotalPasseVertical = passeVertical + TotalPasseVertical
        if (tipoAcao == listaDeAcoes[17]):
            passeVerticalErrado += 1
            TotalPasseVerticalErrado = passeVerticalErrado + TotalPasseVerticalErrado  
        if (tipoAcao == listaDeAcoes[18]):
            passeLongo += 1  
            TotalPasseLongo = passeLongo + TotalPasseLongo
        if (tipoAcao == listaDeAcoes[19]):
            passeLongoErra += 1  
            TotalPasseLongoErra = passeLongoErra + TotalPasseLongoErra
        if (tipoAcao == listaDeAcoes[20]):
            cruzamento += 1       
            TotalCruzamento = cruzamento + TotalCruzamento
        if (tipoAcao == listaDeAcoes[21]):
            cruzamentoErrado += 1  
            TotalCruzamentoErrado = cruzamentoErrado + TotalCruzamentoErrado
        if (tipoAcao == listaDeAcoes[22]):
            vitoriaAereo += 1  
            TotalVitoriaAereo = vitoriaAereo + TotalVitoriaAereo
        if (tipoAcao == listaDeAcoes[23]):
            derrotaAereo += 1  
            TotalDerrotaAereo = derrotaAereo + TotalDerrotaAereo
        if (tipoAcao == listaDeAcoes[24]):
            MCD += 1  
        if (tipoAcao == listaDeAcoes[25]):
            MCO += 1  

        
        

    nota.calcularNotas(adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo, nomeAtleta, posicao, gol, finaGol,
                    finaFora, finaBloq, assistFina, assistGol, chanceClara, bloqFina, intercep, desarmeCerto, desarmeErrado, falta, dribleCerto,
                    perdaBola, faltaSofrida, passeCerto, passeErrado, passeVertical, passeVerticalErrado, passeLongo, passeLongoErra, cruzamento, 
                    cruzamentoErrado, vitoriaAereo, derrotaAereo, MCD, MCO, tempoEmJogo, MCDTotal, MCOTotal, intercepTotal)
    #st.write(TotalFinaFora)
    #st.write(finaFora)
    #coletivo.cadastrarColetivo(infoColetivo, adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo, TotalGol, TotalFinaGol,
    #                TotalFinaFora, TotalFinaBloq, TotalAssistFina, TotalAssistGol, TotalChanceClara, TotalBloqFina, TotalDesarmeCerto, TotalDesarmeErrado, TotalDribleCerto,
    #                TotalPerdaBola, TotalPasseErrado, TotalPasseVertical, TotalPasseVerticalErrado, TotalPasseLongo, TotalPasseLongoErrado, TotalCruzamento, 
    #                TotalCruzamentoErrado, TotalVitoriaAereo, TotalDerrotaAereo, MCDTotal, MCOTotal, intercepTotal)    

       
      
            
        