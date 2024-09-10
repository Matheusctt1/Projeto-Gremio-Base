import streamlit as st
import pandas as pd
import time
import altair as alt
import controles.controleJogo as controle
import numpy as np


def criarDashboard():

    with open( "services\\style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    button = None
    conn = controle.acessarBanco()

    query = 'SELECT * FROM BANCO_DE_DADOS_INDIVIDUAL3'
    db = pd.read_sql(query, conn)

    atletas = db['Atleta']
    adversario = db['Adversario+data']
    
    with st.sidebar:
        st.header("⚽ Filtros:", divider='gray')

        adversarioFiltrado = st.selectbox('Selecione o jogo:', adversario.unique(),
                                              placeholder='Selecione uma Opção',
                                              index=None)
        
        if adversarioFiltrado:
            filtroAtleta = st.selectbox('Selecione um Jogador:', atletas.unique(),
                                    placeholder='Selecione uma Opção',
                                    index=None)
            if adversarioFiltrado:
                dbAdvFiltrado = db[(db['Adversario+data'] == adversarioFiltrado)]
                dbFiltrado = db[(db['Adversario+data'] == adversarioFiltrado) & 
                                (db['Atleta'] == filtroAtleta)]
                button = st.button('Gerar Dashboard')
                    
    if button:
        with st.sidebar:
            with st.spinner('Um momento..'):
                time.sleep(3)
        gerarDashboard(dbFiltrado, dbAdvFiltrado)

def gerarDashboard(db, dbAdv, atletaSelecionado):
    #Ações Rosquinha
    passesVerticais = db['Passe vertical']
    passesVerticaisErrados = db['Passe vertical errado']
    totalPassesVerticais = passesVerticaisErrados + passesVerticais

    dribleCerto = db['Drible certo']
    dribleErrado = db['Perda da bola']
    totalDrible = dribleCerto + dribleErrado

    desarmeCerto = db['Desarme certo']
    desarmeErrado = db['Desarme errado']
    totalDesarme = desarmeCerto + desarmeErrado

    vitoriaJogoAereo = db['Vitória jogo aéreo']
    derrotaJogoAereo = db['Derrota jogo aéreo']
    totalJogoAereo = vitoriaJogoAereo + derrotaJogoAereo

    cruzamento = db['Cruzamento']
    cruzamentoErrado = db['Cruzamento errado']
    totalCruzamento = cruzamento + cruzamentoErrado


    porcentagemPasseVertical = ((passesVerticais * 100) / totalPassesVerticais)
    porcentagemDrible = ((dribleCerto * 100) / totalDrible)
    porcentagemDesarme = ((desarmeCerto * 100) / totalDesarme)
    porcentagemJogoAereo = ((vitoriaJogoAereo * 100) / totalJogoAereo)
    porcentagemCruzamento = ((cruzamento * 100) / totalCruzamento)
    #Fim Ações Rosquinha

    #Ações ultimo
    totalGols = dbAdv['Gol']
    totalFinaGol = dbAdv['Finalização no gol']
    totalFinaFora = dbAdv['Finalização pra fora']
    totalFinaBloq = dbAdv['Finalização bloqueada']
    totalAssistFina = dbAdv['Assist. para finalização']
    totalAssistGol = dbAdv['Assist. para gol']
    totalChanceClara = dbAdv['Chance clara'] 
    totalCruzamentoCerto = dbAdv['Cruzamento']
    totalCruzamentoErrado = dbAdv['Cruzamento errado']
        
    gol = db['Gol']
    finaGol = db['Finalização no gol']
    finaFora = db['Finalização pra fora']
    finaBloq = db['Finalização bloqueada']
    assistFina = db['Assist. para finalização']
    assistGol = db['Assist. para gol']
    chanceClara = db['Chance clara']
    cruzamentoCertoA = db['Cruzamento']
    cruzamentoErradoA = db['Cruzamento errado'] 


    aproveitamentoGol = ((gol * 100) / totalGols)
    aproveitamentoFinaGol = ((finaGol * 100) / totalFinaGol)
    aproveitamentoFinaFora = ((finaFora * 100) / totalFinaFora)
    aproveitamentoFinaBloq = ((finaBloq * 100) / totalFinaBloq)
    aproveitamentoAssistFina = ((assistFina * 100) / totalAssistFina)
    aproveitamentoAssistGol = ((assistGol * 100) / totalAssistGol)
    aproveitamentoChanceClara = ((chanceClara * 100) / totalChanceClara)
    aproveitamentoCruzamentoCerto = ((cruzamentoCertoA * 100) / totalCruzamentoCerto)
    aproveitamentoCruzamentoErrado = ((cruzamentoErradoA * 100) / totalCruzamentoErrado)
    aproveitamentoGeral =(aproveitamentoGol + aproveitamentoAssistFina + aproveitamentoAssistGol + aproveitamentoChanceClara + aproveitamentoFinaGol + 
                          aproveitamentoFinaFora + aproveitamentoFinaBloq + aproveitamentoCruzamentoCerto + aproveitamentoCruzamentoErrado)

    #fim ações ultimo
    porcentagemPasseVertical = porcentagemPasseVertical.iloc[0]
    porcentagemDrible = porcentagemDrible.iloc[0]
    porcentagemDesarme = porcentagemDesarme.iloc[0]
    porcentagemJogoAereo = porcentagemJogoAereo.iloc[0]
    porcentagemCruzamento = porcentagemCruzamento.iloc[0]
    aproveitamentoGeral = aproveitamentoGeral.iloc[0]

    if np.isnan(porcentagemPasseVertical):
        porcentagemPasseVertical = 0
    if np.isnan(porcentagemDrible):
        porcentagemDrible = 0
    if np.isnan(porcentagemDesarme):
        porcentagemDesarme = 0
    if np.isnan(porcentagemJogoAereo):
        porcentagemJogoAereo = 0
    if np.isnan(aproveitamentoGeral):
        aproveitamentoGeral = 0
    if np.isnan(porcentagemCruzamento):
        porcentagemCruzamento = 0  

    #passeVertical
    graficoPasseVertical = pd.DataFrame({
        "Topic": ['', 'Passe Vertical'],
        "% value": [100-porcentagemPasseVertical, porcentagemPasseVertical]
    })
    backgroundGrafico = pd.DataFrame({
        "Topic": ['', 'Passe Vertical'],
        "% value": [100, 0]
    })
    plot = alt.Chart(graficoPasseVertical).mark_arc(innerRadius=45, cornerRadius=25).encode(
        theta="% value",
        color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Passe Vertical', ''],
                        range=['#2896fc', '#e2e1df']),
                    legend=None),
    ).properties(width=130, height=130)
    text = plot.mark_text(align='center', color="#29b5e8", fontSize=20, fontWeight=700).encode(text=alt.value(f'{porcentagemPasseVertical:.1f} %'))
    plot_bg = alt.Chart(backgroundGrafico).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Passe Vertical', '']),
                    legend=None),
    ).properties()
    plotPasseVertical = plot_bg + plot + text

    #drible
    graficoDrible = pd.DataFrame({
        "Topic": ['', 'Confronto Ofensivo'],
        "% value": [100-porcentagemDrible, porcentagemDrible]
    })
    backgroundGrafico = pd.DataFrame({
        "Topic": ['', 'Confronto Ofensivo'],
        "% value": [100, 0]
    })
    plot2 = alt.Chart(graficoDrible).mark_arc(innerRadius=45, cornerRadius=25).encode(
        theta="% value",
        color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Confronto Ofensivo', ''],
                        range=['#2896fc', '#e2e1df']),
                    legend=None),
    ).properties(width=130, height=130)
    text2 = plot.mark_text(align='center', color="#29b5e8", fontSize=20, fontWeight=700).encode(text=alt.value(f'{porcentagemDrible:.1f} %'))
    plot_bg2 = alt.Chart(backgroundGrafico).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Confronto Ofensivo', '']),
                    legend=None),
    ).properties()

    plotDrible = plot_bg2 + plot2 + text2

    #desarme
    graficoDesarme = pd.DataFrame({
        "Topic": ['', 'Confronto Defensivo'],
        "% value": [100-porcentagemDesarme, porcentagemDesarme]
    })
    backgroundGrafico = pd.DataFrame({
        "Topic": ['', 'Confronto Defensivo'],
        "% value": [100, 0]
    })
    plot3 = alt.Chart(graficoDesarme).mark_arc(innerRadius=45, cornerRadius=25).encode(
        theta="% value",
        color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Confronto Defensivo', ''],
                        range=['#2896fc', '#e2e1df']),
                    legend=None),
    ).properties(width=130, height=130)
    text3 = plot.mark_text(align='center', color="#29b5e8", fontSize=20, fontWeight=700).encode(text=alt.value(f'{porcentagemDesarme:.1f} %'))
    plot_bg3 = alt.Chart(backgroundGrafico).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Confronto Defensivo', '']),
                    legend=None),
    ).properties()

    plotDesarme = plot_bg3 + plot3 + text3

    #Jogo Aereo
    graficoAereo = pd.DataFrame({
        "Topic": ['', 'Confronto Aereo'],
        "% value": [100-porcentagemJogoAereo, porcentagemJogoAereo]
    })
    backgroundGrafico = pd.DataFrame({
        "Topic": ['', 'Confronto Aereo'],
        "% value": [100, 0]
    })
    plot4 = alt.Chart(graficoAereo).mark_arc(innerRadius=45, cornerRadius=25).encode(
        theta="% value",
        color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Confronto Aereo', ''],
                        range=['#2896fc', '#e2e1df']),
                    legend=None),
    ).properties(width=130, height=130)
    text4 = plot.mark_text(align='center', color="#29b5e8", fontSize=20, fontWeight=700).encode(text=alt.value(f'{porcentagemJogoAereo:.1f} %'))
    plot_bg4 = alt.Chart(backgroundGrafico).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Confronto Aereo', '']),
                    legend=None),
    ).properties()

    plotAereo = plot_bg4 + plot4 + text4

    #Cruzamento
    graficoCruzamento = pd.DataFrame({
        "Topic": ['', 'Cruzamento'],
        "% value": [100-porcentagemCruzamento, porcentagemCruzamento]
    })
    backgroundGrafico = pd.DataFrame({
        "Topic": ['', 'Cruzamento'],
        "% value": [100, 0]
    })
    plot5 = alt.Chart(graficoCruzamento).mark_arc(innerRadius=45, cornerRadius=25).encode(
        theta="% value",
        color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Cruzamento', ''],
                        range=['#2896fc', '#e2e1df']),
                    legend=None),
    ).properties(width=130, height=130)
    text5 = plot.mark_text(align='center', color="#29b5e8", fontSize=20, fontWeight=700).encode(text=alt.value(f'{porcentagemCruzamento:.1f} %'))
    plot_bg5 = alt.Chart(backgroundGrafico).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Cruzamento', '']),
                    legend=None),
    ).properties()

    plotCruzamento = plot_bg5 + plot5 + text5

    #aproveitamento geral
    graficoGeral = pd.DataFrame({
        "Topic": ['', 'Ações Ultimo Terço'],
        "% value": [100-aproveitamentoGeral, aproveitamentoGeral]
    })
    backgroundGrafico = pd.DataFrame({
        "Topic": ['', 'Ações Ultimo Terço'],
        "% value": [100, 0]
    })
    plot6 = alt.Chart(graficoGeral).mark_arc(innerRadius=45, cornerRadius=25).encode(
        theta="% value",
        color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Ações Ultimo Terço', ''],
                        range=['#2896fc', '#e2e1df']),
                    legend=None),
    ).properties(width=130, height=130)
    text6 = plot.mark_text(align='center', color="#29b5e8", fontSize=20, fontWeight=700).encode(text=alt.value(f'{aproveitamentoGeral:.1f} %'))
    plot_bg6 = alt.Chart(backgroundGrafico).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                    scale=alt.Scale(
                        domain=['Ações Ultimo Terço', '']),
                    legend=None),
    ).properties()

    plotAcoesUltimoTerco = plot_bg6 + plot6 + text6
       

    st.markdown('''<style>
                        
                        img{
                            border-radius: 10px;
                            gap: 0;
                        }
                        .st-emotion-cache-asc41u h1, .st-emotion-cache-asc41u h2, .st-emotion-cache-asc41u h3, .st-emotion-cache-asc41u h4, .st-emotion-cache-asc41u h5, .st-emotion-cache-asc41u h6, .st-emotion-cache-asc41u span {
                            text-size: 1px;
                            text-wrap: nowrap;
                            justify-content: center;
                            display: flex;

                        }
                        
                        </style>'''

                        , unsafe_allow_html=True)
    def fotoJogador(fotoAtleta):
        st.image(fotoAtleta)
    def grafPasseVertical():
        st.markdown('<p style="text-align:center;display:flex;justify-content:center;text-wrap:nowrap;font-size:18px;">Passe Vertical</p>', unsafe_allow_html=True)
        st.altair_chart(plotPasseVertical, use_container_width=True)
    def grafConfrontOfen():
        st.markdown('<p style="text-align:center;display:flex;justify-content:center;text-wrap:nowrap;font-size:18px;"> Confronto Ofen.</p>', unsafe_allow_html=True)
        st.altair_chart(plotDrible, use_container_width=True)
    def grafConfrontDefen():
        st.markdown('<p style="text-align:center;display:flex;justify-content:center;text-wrap:nowrap;font-size:18px;"> Confronto Defen.</p>', unsafe_allow_html=True)
        st.altair_chart(plotDesarme, use_container_width=True)
    def grafConfrontAereo():
        st.markdown('<p style="text-align:center;display:flex;justify-content:center;text-wrap:nowrap;font-size:18px;"> Confronto Aéreo</p>', unsafe_allow_html=True)
        st.altair_chart(plotAereo, use_container_width=True)
    def grafCruzamento():
        st.markdown('<p style="text-align:center;display:flex;justify-content:center;text-wrap:nowrap;font-size:18px;"> Cruzamento</p>', unsafe_allow_html=True)
        st.altair_chart(plotCruzamento, use_container_width=True)
    def grafUltTerco():
        st.markdown('<p style="text-align:center;display:flex;justify-content:center;text-wrap:nowrap;font-size:18px;"> Ações Ult. Terço</p>', unsafe_allow_html=True)
        st.altair_chart(plotAcoesUltimoTerco, use_container_width=True)
    
    return { 'fotoJogador': fotoJogador, 
            'grafPasseVertical': grafPasseVertical, 
            'grafConfrontOfen': grafConfrontOfen, 
            'grafConfrontDefen': grafConfrontDefen, 
            'grafConfrontAereo': grafConfrontAereo, 
            'grafCruzamento': grafCruzamento, 
            'grafUltTerco': grafUltTerco}