# Definição da classe jogo

class jogo:
    def __init__(self, adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo
                ,atleta, posicao, tempo_em_jogo, gol, finaGol, finaFora, finaBloq, assistFina, assistGol, chanceClara
                ,bloqFina, interceptacao, desarmeCerto, desarmeErrado, falta, dribleCerto, perdaBola, faltaSofrida, passeCerto, passeErrado
                ,passeVert, passeVertErra, passeLongo, passeLongoErra, cruzamento, cruzamentoErra, vitoriaAereo
                ,derrotaAereo, MCD, MCO, notaFinal,criacoes, confront, complet, nota_ofensiva, nota_defensiva
                ):
                self.adversarioData = adversarioData
                self.nivelJogo = nivelJogo
                self.dataJogo = dataJogo
                self.campeonato = campeonato
                self.categoria = categoria
                self.referencia = referencia
                self.tempoTotalJogo = tempoTotalJogo
                self.atleta = atleta
                self.posicao = posicao
                self.tempo_em_jogo = tempo_em_jogo
                self.gol = gol
                self.finaGol = finaGol
                self.finaFora = finaFora
                self.finaBloq = finaBloq
                self.assistFina = assistFina
                self.assistGol = assistGol
                self.chanceClara = chanceClara
                self.bloqFina = bloqFina
                self.interceptacao = interceptacao
                self.desarmeCerto = desarmeCerto
                self.desarmeErrado = desarmeErrado
                self.falta = falta
                self.dribleCerto = dribleCerto
                self.perdaBola = perdaBola
                self.faltaSofrida = faltaSofrida
                self.passeCerto = passeCerto
                self.passeErrado = passeErrado
                self.passeVert = passeVert
                self.passeVertErra = passeVertErra
                self.passeLongo = passeLongo
                self.passeLongoErra = passeLongoErra
                self.cruzamento = cruzamento
                self.cruzamentoErra = cruzamentoErra
                self.vitoriaAereo = vitoriaAereo
                self.derrotaAereo = derrotaAereo
                self.MCD = MCD
                self.MCO = MCO
                self.notaFinal = notaFinal
                self.criacoes = criacoes
                self.confront = confront
                self.complet = complet
                self.nota_ofensiva = nota_ofensiva
                self.nota_defensiva = nota_defensiva
