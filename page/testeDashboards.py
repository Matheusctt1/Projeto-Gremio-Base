import streamlit as st
import pandas as pd
import numpy as np
import controles.controleAtleta as controleAtleta
import services.dataBase as db
import page.dashboard as gerarDashboard
import page.mapaCalor as mapaDeCalor
import page.Gráfico_de_Impacto as graficoDeImpacto

def renderizar_dashboard(dfIndividual_filt, dfIndividual, df_filtradoAtleta, dfNotas, dfAcoes_filt,
                         notas_ofensivas, notas_defensivas, tempo_em_jogo, filtro_atleta, colunas_para_excluir, dfAcoesJogador):

    with st.container(border=True):
                        graficosDashboard = gerarDashboard.gerarDashboard(dfIndividual_filt, dfIndividual,df_filtradoAtleta)
                        colContainer1 = st.columns([4,0.8])
                        
                        with colContainer1[0]:
                            colGraficos = st.columns([1,1.5,1,1,1,1,1,1])
                            with colGraficos[0]:
                                fotoDf = controleAtleta.exibirAtleta(df_filtradoAtleta)
                                
                                
                                fotoAtleta = fotoDf['vb_imagem'].values[0]
                                graficosDashboard['fotoJogador'](fotoAtleta)                 
                                
                            with colGraficos[1]:
                                dfNotas.reset_index(inplace=True)
                                dfNotas.rename(columns={'index': df_filtradoAtleta}, inplace=True)
                                dfNotas.rename(columns={ 0: 'Nota'}, inplace=True)
                                
                                st.dataframe(dfNotas, on_select='ignore', hide_index=True, use_container_width=True)
                            with colGraficos[2]:
                                graficosDashboard['grafPasseVertical']()
                            with colGraficos[3]:
                                graficosDashboard['grafConfrontOfen']()
                            with colGraficos[4]:
                                graficosDashboard['grafConfrontDefen']()
                            with colGraficos[5]:
                                graficosDashboard['grafConfrontAereo']()
                            with colGraficos[6]:
                                graficosDashboard['grafCruzamento']()
                            with colGraficos[7]:
                                graficosDashboard['grafUltTerco']()
                            tamanhoMapa = st.columns([0.042,0.1])
                            with tamanhoMapa[0]:
                                mapaDeCalor.mapaDeCalor(dfAcoes_filt)

                            with tamanhoMapa[1]:
                                graficoDeImpacto.plotarGrafico(notas_ofensivas, notas_defensivas, tempo_em_jogo, filtro_atleta)

                        with colContainer1[1]:
                            dfAcoesJogador = dfAcoesJogador.drop(colunas_para_excluir)
                            dfAcoesJogador.reset_index(inplace=True)
                            dfAcoesJogador.rename(columns={'index': 'Ações'}, inplace=True)
                            dfAcoesJogador.rename(columns={ 0: 'Total'}, inplace=True)
                            st.data_editor(dfAcoesJogador, height=913,use_container_width=True,disabled=True, hide_index=True)
                        

def mostre(string):
    return st.write(string)

def somarAcoesJogador(df, atleta):

    somaGols = sum(df[df['Atleta'] == atleta]['Gol'])
    somaFinaGol = sum(df[df['Atleta'] == atleta]['Finalização no gol'])
    somaFinaFora = sum(df[df['Atleta'] == atleta]['Finalização pra fora'])
    somaFinaBloq = sum(df[df['Atleta'] == atleta]['Finalização bloqueada'])
    somaAssistFina = sum(df[df['Atleta'] == atleta]['Assist. para finalização'])
    somaAssistGol = sum(df[df['Atleta'] == atleta]['Assist. para gol'])
    somaChanceClara = sum(df[df['Atleta'] == atleta]['Chance clara'])
    somaBloqFina = sum(df[df['Atleta'] == atleta]['Bloqueio de finalização'])
    somaIntercep = sum(df[df['Atleta'] == atleta]['Intercepção'])
    somaDesarmeCerto = sum(df[df['Atleta'] == atleta]['Desarme certo'])
    somaDesarmeErrado = sum(df[df['Atleta'] == atleta]['Desarme errado'])
    somaDribleCerto = sum(df[df['Atleta'] == atleta]['Drible certo'])
    somaPerdaBola = sum(df[df['Atleta'] == atleta]['Perda da bola'])
    somaPasseCerto = sum(df[df['Atleta'] == atleta]['Passe certo'])
    somaPasseErrado = sum(df[df['Atleta'] == atleta]['Passe errado'])
    somaPasseVertical = sum(df[df['Atleta'] == atleta]['Passe vertical'])
    somaPasseVerticalErrado = sum(df[df['Atleta'] == atleta]['Passe vertical errado'])
    somaPasseLongo = sum(df[df['Atleta'] == atleta]['Passe longo'])
    somaPasseLongoErrado = sum(df[df['Atleta'] == atleta]['Passe longo errado'])
    somaCruzamento = sum(df[df['Atleta'] == atleta]['Cruzamento'])
    somaCruzamentoErrado = sum(df[df['Atleta'] == atleta]['Cruzamento errado'])
    somaVitoriaAereo = sum(df[df['Atleta'] == atleta]['Vitória jogo aéreo'])
    somaDerrotaAereo = sum(df[df['Atleta'] == atleta]['Derrota jogo aéreo'])
    somaMCD = sum(df[df['Atleta'] == atleta]['MCD'])
    somaMCO = sum(df[df['Atleta'] == atleta]['MCO'])
    
    exibCriacoes = np.mean(df[df['Atleta'] == atleta]['Criacoes'])
    exibConfront = np.mean(df[df['Atleta'] == atleta]['Confront'])
    exibComplet = np.mean(df[df['Atleta'] == atleta]['Complet'])
    exibNotaFinal = np.mean(df[df['Atleta'] == atleta]['Nota final'])
    exibNotaOfensiva = np.mean(df[df['Atleta'] == atleta]['Nota ofensiva'])
    exibNotaDefensiva = np.mean(df[df['Atleta'] == atleta]['Nota defensiva'])
    exibTempoEmJogo = sum(df[df['Atleta'] == atleta]['Tempo em jogo'])

    dfSomado = pd.DataFrame({
        'Tempo em jogo' : [exibTempoEmJogo],
        'Gol' : [somaGols],
        'Finalização no gol' : [somaFinaGol],
        'Finalização pra fora' : [somaFinaFora],
        'Finalização bloqueada' : [somaFinaBloq],
        'Assist. para finalização' : [somaAssistFina],
        'Assist. para gol' : [somaAssistGol],
        'Chance clara' : [somaChanceClara],
        'Bloqueio de finalização' : [somaBloqFina],
        'Interceptação' : [somaIntercep],
        'Desarme certo' : [somaDesarmeCerto],
        'Desarme errado' : [somaDesarmeErrado],
        'Drible certo' : [somaDribleCerto],
        'Perda da bola' : [somaPerdaBola],
        'Passe certo' : [somaPasseCerto],
        'Passe errado' : [somaPasseErrado],
        'Passe vertical' : [somaPasseVertical],
        'Passe vertical errado' : [somaPasseVerticalErrado],
        'Passe longo' : [somaPasseLongo],
        'Passe Longo errado' : [somaPasseLongoErrado],
        'Cruzamento' : [somaCruzamento],
        'Cruzamento errado' : [somaCruzamentoErrado],
        'Vitória jogo aéreo' : [somaVitoriaAereo],
        'Derrota jogo aéreo' : [somaDerrotaAereo],
        'MCD' : [somaMCD],
        'MCO' : [somaMCO],
        'Nota final' : [round(exibNotaFinal, 1)],
        'Criacoes' : [round(exibCriacoes, 1)],
        'Confront' : [round(exibConfront, 1)],
        'Complet' : [round(exibComplet, 1)],
        'Nota ofensiva' : [round(exibNotaOfensiva, 1)],
        'Nota defensiva' : [round(exibNotaDefensiva, 1)]
    }) 

    return dfSomado

def filtrarGraficos():

    def init_connection():
        return db.cnxn

    conn = init_connection()

    # Mapa de Calor
    verificaBanco = 'SELECT COUNT([ID]) FROM BD_INDIVIDUAL'
    bancoVerificado = pd.read_sql(verificaBanco, conn)
    if bancoVerificado.empty:
            st.error("Erro!!! Não foi possivel encontrar jogos cadastrados. Revise seu Banco de dados Individual.")
    
    verificaBanco = 'SELECT COUNT([ID]) FROM BD_ACOES'
    bancoVerificado = pd.read_sql(verificaBanco, conn)
    if bancoVerificado.empty:
            st.error("Erro!!! Não foi possivel encontrar jogos cadastrados. Revise seu Banco de dados de Ações.")

    verificaBanco = 'SELECT COUNT([ID]) FROM BD_GOLEIROS'
    bancoVerificado = pd.read_sql(verificaBanco, conn)
    if bancoVerificado.empty:
            st.error("Erro!!! Não foi possivel encontrar jogos cadastrados. Revise seu Banco de dados de Goleiros.")

    queryAcoes = "SELECT [Adversario+Data],[Atleta],[Tipo de Ação],[X],[Y] FROM BD_ACOES;"
    queryIndividual = "SELECT * FROM BD_INDIVIDUAL;"
    queryGoleiros = "SELECT * FROM BD_GOLEIROS;"
    dfAcoes = pd.read_sql(queryAcoes, conn)
    dfIndividual = pd.read_sql(queryIndividual, conn)
    dfGoleiros = pd.read_sql(queryGoleiros, conn)
    dfIndividual.rename(columns={'Mudança de comportamento defensiva': 'MCD'}, inplace=True)
    dfIndividual.rename(columns={'Mudança de comportamento ofensiva': 'MCO'}, inplace=True)
    dfIndividual.rename(columns={'Assistencia para finalização': 'Assist. para finalização'}, inplace=True)
    dfIndividual.rename(columns={'Assistencia para gol': 'Assist. para gol'}, inplace=True)
    dfAcoes.rename(columns={'Mudança de comportamento defensiva': 'MCD'}, inplace=True)
    dfAcoes.rename(columns={'Mudança de comportamento ofensiva': 'MCO'}, inplace=True)
    filtro_adversario = dfIndividual['Adversario+data']
    button = None
    with st.sidebar.container(border=True, height=500):
            st.header('Filtros', divider='gray')
            df_filtradoADV = st.multiselect(
                'Selecione o Adversario:',
                options=filtro_adversario.unique(), 
                placeholder='Selecione uma Opção'
            )
    
            if df_filtradoADV:
                dfIndividual = dfIndividual[dfIndividual['Adversario+data'].isin(df_filtradoADV)]
                dfAcoes = dfAcoes[dfAcoes['Adversario+Data'].isin(df_filtradoADV)]
                dfGoleiros = dfGoleiros[dfGoleiros['Adversario+data'].isin(df_filtradoADV)]
                filtro_atleta = dfIndividual['Atleta']

                df_filtradoAtleta = st.selectbox(
                    'Selecione o Atleta:',
                    options=filtro_atleta.unique(), 
                    placeholder='Selecione uma Opção',
                    index=None,
                    key=1
                )
            
                dfIndividual_filt = dfIndividual[(dfIndividual['Atleta'] == df_filtradoAtleta) ]

                dfAcoes_filt = dfAcoes[(dfAcoes['Atleta'] == df_filtradoAtleta) ]
                dfExib = dfIndividual_filt
                colunas_para_exibir = ['Nota final', 'Nota ofensiva', 'Nota defensiva', 'Tempo em jogo']
                colunas_para_excluir = ['Tempo em jogo', 'Nota final','Criacoes','Confront','Complet','Nota ofensiva','Nota defensiva']
                dfIndividual_Transposto3 = dfExib[colunas_para_exibir].T
                dfIndividual_Transposto3 = dfIndividual_Transposto3.rename(columns={1:'Parâmetros:'})
                button = st.button('Gerar Dashboard')

                filtro_atleta = dfIndividual["Atleta"].unique()
                dfIndividual['Nota final'] = dfIndividual['Nota final'].astype(float)
                dfIndividual['Criacoes'] = dfIndividual['Criacoes'].astype(float)
                dfIndividual['Confront'] = dfIndividual['Confront'].astype(float)
                dfIndividual['Complet'] = dfIndividual['Complet'].astype(float)
                dfIndividual['Nota ofensiva'] = dfIndividual['Nota ofensiva'].astype(float)
                dfIndividual['Nota defensiva'] = dfIndividual['Nota defensiva'].astype(float)

                atletasFiltrados = []
                tempo_em_jogo = []
                notas_ofensivas = []
                notas_defensivas = []
                notas_finais = []
                               
                for atleta in filtro_atleta:
                    atletasFiltrados.append(atleta)
                    tempo_em_jogo.append(sum(dfIndividual[dfIndividual['Atleta'] == atleta]['Tempo em jogo']))
                    notas_ofensivas.append(np.mean(dfIndividual[dfIndividual['Atleta'] == atleta]['Nota ofensiva']))
                    notas_defensivas.append(np.mean(dfIndividual[dfIndividual['Atleta'] == atleta]['Nota defensiva']))
                    notas_finais.append(np.mean(dfIndividual[dfIndividual['Atleta'] == atleta]['Nota final']))

                
                dfSomado = somarAcoesJogador(dfIndividual, df_filtradoAtleta)
                dfAcoesJogador = dfSomado.T
                dfNotas = dfSomado[colunas_para_exibir].T
               
            else:
                st.error("Selecione um adversario.")   
                   
    if button:
        renderizar_dashboard(dfIndividual_filt, dfIndividual, df_filtradoAtleta, dfNotas, dfAcoes_filt,
                         notas_ofensivas, notas_defensivas, tempo_em_jogo, filtro_atleta, colunas_para_excluir, dfAcoesJogador)
            