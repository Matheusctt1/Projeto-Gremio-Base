import streamlit as st
def aproveitamento(x, y, z):
    if(x == 0):
        aproveitamento = 0
            
    else:
        aproveitamento = (((100 / ((x + y) / x)) * z) / 100)

    return aproveitamento
 
def calculaComplet(x, y, z):
    if(x == 0):
        calculaComplet = 0
    else:
        calculaComplet = ((x / y) * 100)

        if(calculaComplet > z):
            calculaComplet = z

    return calculaComplet

def calculaIntercep(x, y, z):
    #st.write(x)
    #st.write(y)
    if(x== 0):
        calculaIntercep = 0
    else:
        calculaIntercep = ((x / y) * 100)

        if (calculaIntercep > z):
            calculaIntercep = z
    
    return calculaIntercep

class criacoes:
    def __init__(self, posicao, gol, finaGol, finaFora, finaBloq, chanceClara, assistFina, assistGol):
        
        if posicao == 'ZAGUEIRO':   
            self.gol = 20 * gol
            self.finaGol = 4 * finaGol
            self.finaFora = 2 * finaFora
            self.finaBloq = 0.5 * finaBloq
            self.chanceClara = 4 * chanceClara
            self.assistFina = 2.5 * assistFina
            self.assistGol = 7 * assistGol
        
        if posicao == 'LATERAL':
            self.gol = 25 * gol
            self.finaGol = 5 * finaGol
            self.finaFora = 2.5 * finaFora
            self.finaBloq = 1.5 * finaBloq
            self.chanceClara = 9 * chanceClara
            self.assistFina = 5 * assistFina
            self.assistGol = 12 * assistGol
        
        if posicao == 'VOLANTE':
            self.gol = 25 * gol
            self.finaGol = 6.5 * finaGol
            self.finaFora = 3.5 * finaFora
            self.finaBloq = 2 * finaBloq
            self.chanceClara = 8 * chanceClara
            self.assistFina = 5 * assistFina
            self.assistGol = 10 * assistGol

        if posicao == 'MEIO CAMPO':
            self.gol = 25 * gol
            self.finaGol = 9 * finaGol
            self.finaFora = 4.5 * finaFora
            self.finaBloq = 2.5 * finaBloq
            self.chanceClara = 9.5 * chanceClara
            self.assistFina = 7.5 * assistFina
            self.assistGol = 12 * assistGol

        if posicao == 'EXTREMA':
            self.gol = 25 * gol
            self.finaGol = 10 * finaGol
            self.finaFora = 5.5 * finaFora
            self.finaBloq = 3 * finaBloq
            self.chanceClara = 9.5 * chanceClara
            self.assistFina = 6 * assistFina
            self.assistGol = 11 * assistGol

        if posicao == 'CENTROAVANTE':
            self.gol = 30 * gol
            self.finaGol = 14 * finaGol
            self.finaFora = 9 * finaFora
            self.finaBloq = 4.5 * finaBloq
            self.chanceClara = 7.5 * chanceClara
            self.assistFina = 5 * assistFina
            self.assistGol = 10 * assistGol

class confront:
    def __init__(self, posicao, passeCerto, passeErrado,  passeVertical, passeVerticalErrado, passeLongo, passeLongoErrado, desarmeCerto,
                desarmeErrado, dribleCerto, perdaBola, vitoriaAereo, derrotaAereo, cruzamento, cruzamentoErrado, falta, faltaSofrida):
        if posicao == 'ZAGUEIRO': 
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 8)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 7)
            self.Ndrible = aproveitamento (dribleCerto, perdaBola, 1)
            self.Ndesarme = aproveitamento(desarmeCerto, desarmeErrado, 15)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 17)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 1)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 6) 
            self.falta = falta * 0
            self.faltaSofrida = faltaSofrida * 0
                  
        if posicao == 'LATERAL':
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 1.5)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 0.5)
            self.Ndrible = aproveitamento (dribleCerto, perdaBola, 6)
            self.Ndesarme = aproveitamento(desarmeCerto, desarmeErrado, 11)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 9)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 17)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 5)  
            self.falta = falta * 0
            self.faltaSofrida = faltaSofrida * 0
        
        if posicao == 'VOLANTE': 
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 9.5)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 5.5)
            self.Ndrible = aproveitamento (dribleCerto, perdaBola, 3.5)
            self.Ndesarme = aproveitamento(desarmeCerto, desarmeErrado, 12)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 9.5)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 2.5)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 7.5) 
            self.falta = falta * 0
            self.faltaSofrida = faltaSofrida * 0

        if posicao == 'MEIO CAMPO': 
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 10)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 4)
            self.Ndrible = aproveitamento (dribleCerto, perdaBola, 10)
            self.Ndesarme = aproveitamento(desarmeCerto, desarmeErrado, 4)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 2.5)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 6.5)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 8)
            self.falta = falta * 0
            self.faltaSofrida = faltaSofrida * 0

        if posicao == 'EXTREMA':
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 7)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 2)
            self.Ndesarme = aproveitamento (dribleCerto, perdaBola, 18)
            self.Ndrible = aproveitamento(desarmeCerto, desarmeErrado, 4)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 1)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 8)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 5)  
            self.falta = falta * 0
            self.faltaSofrida = faltaSofrida * 0

        if posicao == 'CENTROAVANTE':
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 4)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 3)
            self.Ndrible = aproveitamento (dribleCerto, perdaBola, 12.5)
            self.Ndesarme = aproveitamento(desarmeCerto, desarmeErrado, 3)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 12.5)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 4)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 6)  
            self.falta = falta * 0
            self.faltaSofrida = faltaSofrida * 0

class complet:

    def __init__(self, posicao, MCD, MCO, intercep, 
                 bloqFina, MCDTotal, MCOTotal, intercepTotal):
        if posicao == 'ZAGUEIRO':   
            self.NMCD = calculaComplet(MCD, MCDTotal, 10)
            self.NMCO = calculaComplet(MCO, MCOTotal, 8)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 22)
            self.Nbloqfina = 10 * bloqFina
        
        if posicao == 'LATERAL':
            self.NMCD = calculaComplet(MCD, MCDTotal, 11.5)
            self.NMCO = calculaComplet(MCO, MCOTotal, 10)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 8.5)
            self.Nbloqfina = 5 * bloqFina
        
        if posicao == 'VOLANTE':
            self.NMCD = calculaComplet(MCD, MCDTotal, 11.5)
            self.NMCO = calculaComplet(MCO, MCOTotal, 10)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 8.5)
            self.Nbloqfina = 5 * bloqFina

        if posicao == 'MEIO CAMPO':
            self.NMCD = calculaComplet(MCD, MCDTotal, 8.5)
            self.NMCO = calculaComplet(MCO, MCOTotal, 11.5)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 5)
            self.Nbloqfina = 4 * bloqFina

        if posicao == 'EXTREMA':
            self.NMCD = calculaComplet(MCD, MCDTotal, 8.5)
            self.NMCO = calculaComplet(MCO, MCOTotal, 11.5)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 5)
            self.Nbloqfina = 4 * bloqFina

        if posicao == 'CENTROAVANTE':
            self.NMCD = calculaComplet(MCD, MCDTotal, 7.5)
            self.NMCO = calculaComplet(MCO, MCOTotal, 9.5)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 3)
            self.Nbloqfina = 2 * bloqFina

class ofensivas:
    def __init__(self, posicao, gol, finaGol, finaFora, finaBloq, chanceClara,
                assistFina, assistGol, dribleCerto, perdaBola, passeCerto, passeErrado, 
                passeVertical, passeVerticalErrado, passeLongo, passeLongoErrado, 
                cruzamento, cruzamentoErrado, MCO, MCOTotal):
        if posicao == 'ZAGUEIRO':   
            self.gol = 2 * gol
            self.finaGol = 20 * finaGol
            self.finaFora = 4 * finaFora
            self.finaBloq = 2 * finaBloq
            self.chanceClara = 0.5 * chanceClara
            self.assistFina = 4 * assistFina
            self.assistGol = 2.5 * assistGol
            self.drible = aproveitamento (dribleCerto, perdaBola, 1)
            self.passeCerto = aproveitamento(passeCerto, passeErrado, 6) 
            self.passeVertical = aproveitamento(passeVertical, passeVerticalErrado, 8)
            self.passeLongo = aproveitamento(passeLongo, passeLongoErrado, 7)
            self.cruzamento = aproveitamento(cruzamento, cruzamentoErrado, 1)
            self.MCO = calculaComplet(MCO, MCOTotal, 8)


        if posicao == 'LATERAL':
            self.gol = 2.5 * gol
            self.finaGol = 25 * finaGol
            self.finaFora = 5 * finaFora
            self.finaBloq = 2.5 * finaBloq
            self.chanceClara = 1.5 * chanceClara
            self.assistFina = 9 * assistFina
            self.assistGol = 5 * assistGol
            self.drible = aproveitamento (dribleCerto, perdaBola, 6)
            self.passeCerto = aproveitamento(passeCerto, passeErrado, 5) 
            self.passeVertical = aproveitamento(passeVertical, passeVerticalErrado, 1.5)
            self.passeLongo = aproveitamento(passeLongo, passeLongoErrado, 0.5)
            self.cruzamento = aproveitamento(cruzamento, cruzamentoErrado, 17)
            self.MCO = calculaComplet(MCO, MCOTotal, 10)
        
        if posicao == 'VOLANTE':
            self.gol = 2.5 * gol
            self.finaGol = 25 * finaGol
            self.finaFora = 6.5 * finaFora
            self.finaBloq = 3.5 * finaBloq
            self.chanceClara = 2 * chanceClara
            self.assistFina = 8 * assistFina
            self.assistGol = 5 * assistGol
            self.drible = aproveitamento (dribleCerto, perdaBola, 3.5)
            self.passeCerto = aproveitamento(passeCerto, passeErrado, 7.5) 
            self.passeVertical = aproveitamento(passeVertical, passeVerticalErrado, 9.5)
            self.passeLongo = aproveitamento(passeLongo, passeLongoErrado, 5.5)
            self.cruzamento = aproveitamento(cruzamento, cruzamentoErrado, 2.5)
            self.MCO = calculaComplet(MCO, MCOTotal, 10)

        if posicao == 'MEIO CAMPO':
            self.gol = 2.5 * gol
            self.finaGol = 25 * finaGol
            self.finaFora = 9 * finaFora
            self.finaBloq = 4.5 * finaBloq
            self.chanceClara = 2.5 * chanceClara
            self.assistFina = 9.5 * assistFina
            self.assistGol = 7.5 * assistGol
            self.drible = aproveitamento (dribleCerto, perdaBola, 10)
            self.passeCerto = aproveitamento(passeCerto, passeErrado, 8) 
            self.passeVertical = aproveitamento(passeVertical, passeVerticalErrado, 10)
            self.passeLongo = aproveitamento(passeLongo, passeLongoErrado, 4)
            self.cruzamento = aproveitamento(cruzamento, cruzamentoErrado, 6.5)
            self.MCO = calculaComplet(MCO, MCOTotal, 11.5)

        if posicao == 'EXTREMA':
            self.gol = 2.5 * gol
            self.finaGol = 25 * finaGol
            self.finaFora = 10 * finaFora
            self.finaBloq = 5.5 * finaBloq
            self.chanceClara = 3 * chanceClara
            self.assistFina = 9.5 * assistFina
            self.assistGol = 6 * assistGol
            self.drible = aproveitamento (dribleCerto, perdaBola, 18)
            self.passeCerto = aproveitamento(passeCerto, passeErrado, 5) 
            self.passeVertical = aproveitamento(passeVertical, passeVerticalErrado, 7)
            self.passeLongo = aproveitamento(passeLongo, passeLongoErrado, 2)
            self.cruzamento = aproveitamento(cruzamento, cruzamentoErrado, 8)
            self.MCO = calculaComplet(MCO, MCOTotal, 11.5)

        if posicao == 'CENTROAVANTE':
            self.gol = 3 * gol
            self.finaGol = 30 * finaGol
            self.finaFora = 14 * finaFora
            self.finaBloq = 9 * finaBloq
            self.chanceClara = 4.5 * chanceClara
            self.assistFina = 7.5 * assistFina
            self.assistGol = 5 * assistGol
            self.drible = aproveitamento (dribleCerto, perdaBola, 12.5)
            self.passeCerto = aproveitamento(passeCerto, passeErrado, 6) 
            self.passeVertical = aproveitamento(passeVertical, passeVerticalErrado, 4)
            self.passeLongo = aproveitamento(passeLongo, passeLongoErrado, 3)
            self.cruzamento = aproveitamento(cruzamento, cruzamentoErrado, 4)
            self.MCO = calculaComplet(MCO, MCOTotal, 9.5)

class defensivas:
    def __init__(self, posicao, bloqFina, intercep, intercepTotal,
                desarmeCerto, desarmeErrado, MCD, MCDTotal):
        
        if posicao == 'ZAGUEIRO':
            self.bloqfina = 10 * bloqFina
            self.intercep = calculaIntercep(intercep, intercepTotal, 22)
            self.desarme = aproveitamento(desarmeCerto, desarmeErrado, 15)
            self.MCD = calculaComplet(MCD, MCDTotal, 10)
            
                  
        if posicao == 'LATERAL':
            self.bloqfina = 5 * bloqFina
            self.intercep = calculaIntercep(intercep, intercepTotal, 8.5)
            self.desarme = aproveitamento(desarmeCerto, desarmeErrado, 11)
            self.MCD = calculaComplet(MCD, MCDTotal, 11.5)

        if posicao == 'VOLANTE': 
            self.bloqfina = 5 * bloqFina
            self.intercep = calculaIntercep(intercep, intercepTotal, 8.5)
            self.desarme = aproveitamento(desarmeCerto, desarmeErrado, 12)
            self.MCD = calculaComplet(MCD, MCDTotal, 11.5)

        if posicao == 'MEIO CAMPO': 
            self.bloqfina = 4 * bloqFina
            self.intercep = calculaIntercep(intercep, intercepTotal, 5)
            self.desarme = aproveitamento(desarmeCerto, desarmeErrado, 4)
            self.MCD = calculaComplet(MCD, MCDTotal, 8.5)

        if posicao == 'EXTREMA':
            self.bloqfina = 4 * bloqFina
            self.intercep = calculaIntercep(intercep, intercepTotal, 5)
            self.desarme = aproveitamento(desarmeCerto, desarmeErrado, 4)
            self.MCD = calculaComplet(MCD, MCDTotal, 8.5)

        if posicao == 'CENTROAVANTE':
            self.bloqfina = 2 * bloqFina
            self.intercep = calculaIntercep(intercep, intercepTotal, 3)
            self.desarme = aproveitamento(desarmeCerto, desarmeErrado, 3)
            self.MCD = calculaComplet(MCD, MCDTotal, 7.5)