import streamlit as st
from streamlit import session_state
import logicas.definicaoVariaveis as cadastrarBanco
import logicas.numerosGoleiro as cadastrarGoleiro
import logicas.definicaoColetivo as cadastrarColetivo
import logicas.definicaoADV as cadastrarADV
import logicas.filtrarDataFrame as filtrarDataFrame
import services.dataBase as db
import pandas as pd

na_values = ['NA', 'N/A', '#N/A', 'NaN', 'nan']

def init_connection():
    return db.cnxn

def verificarGoleiro(nome, conn):
    verificaBanco = f"""SELECT COUNT(*) FROM BD_GOLEIROINDV WHERE Goleiro = '{nome}'"""
    bancoVerificado = pd.read_sql(verificaBanco, conn)
    
    return bancoVerificado.iloc[0, 0] > 0

def cadastrar():
    with st.container():
        st.title('Cadastro Banco de Dados')
        uploadedFile = st.file_uploader(label='Insira o Arquivo XLS para começar o cadastro', type='xlsx')
        
        if uploadedFile is None:
            st.write('Aguardando...')
            limparVariaveis()
        else:
            df = pd.read_excel(uploadedFile, na_values=na_values, sheet_name=0)
            
            mostrarFormDados(df)

def mostrarFormDados(df):
    
    if 'listaPosicao' not in session_state:
        session_state.listaPosicao = []

    def cadastrarPosicao(posicao):
        session_state.listaPosicao.append(posicao)
    conn = init_connection()
    categorias = ['Sub 14', 'Sub 15', 'Sub 16', 'Sub 17', 'Sub 19', 'Sub 20']
    referencias = ['Infantil', 'Juvenil', 'Junior']
    niveis = ['2', '3', '4', '5']
    posicoes = ['ZAGUEIRO', 'LATERAL', 'VOLANTE', 'MEIO CAMPO', 'EXTREMA', 'CENTROAVANTE']
    listaAtletas = df.columns[1:].tolist()
    numeroAtletas = len(listaAtletas)
    listaGoleiros = []
    listaAtletasFiltered = []
    i = 0
    
    while(i < numeroAtletas):
        atleta = listaAtletas[i]
        posicao = atleta[0:1]
                    
            
        if (atleta == 'PASSE CERTO'):
            i = numeroAtletas + 1
        else:

            if(posicao == 'X'):
                listaAtletasFiltered.append(atleta[2:])  
        i += 1
    
    for nome in listaAtletasFiltered:
        if verificarGoleiro(nome, conn):
            listaGoleiros.append(nome)
            listaAtletasFiltered.remove(nome)
    

    tab1, tab2, tab3  = st.tabs(["Cadastrar Jogo", "Cadastrar Coletivo", "Cadastrar Adversário"])

    with tab1:
        st.subheader('Cadastrar Informações do Jogo', divider='gray')
        table1, table2, table3 = st.columns(3)
        with table1:
            adversarioData = st.text_input('Adversario + Data:', placeholder='Ex: Grêmio 07/09/1903')
            nivelJogo = st.selectbox('Nivel do Jogo:', placeholder='Ex: 5', options=niveis)
            dataJogo = st.text_input('Data:', placeholder='Ex: 07/09/1903')
        
        with table2:
            campeonato = st.text_input('Campeonato:', placeholder='Ex: Campeonato Brasileiro 2024')
            categoria = st.selectbox('Categoria:', placeholder='Ex: Sub 20', options=categorias)

        with table3:
            referencia = st.selectbox('Referência:', placeholder='Ex: Junior', options=referencias)
            tempoTotalJogo = st.text_input('Tempo Total de Jogo:', placeholder='Ex: 90')
           
    with tab2:
        st.subheader('Cadastrar Informações Coletivo', divider='gray')
        column5, column6 = st.columns(2)
        with column5:
            posseGeral = st.text_input('Posse Geral:', placeholder='Ex: 40')
            posseOfensiva = st.text_input('Posse Ofensiva:', placeholder='Ex: 15')
            posseMeio = st.text_input('Posse Meio:', placeholder='Ex: 14')
            posseDefensiva = st.text_input('Posse Defensiva:', placeholder='Ex: 11')
        
        with column6:
            passeCerto = st.text_input('Passes Certos:', placeholder='Ex: 180')
            finalizacaoOrg = st.text_input('Finalização Organizada:', placeholder='Ex: 90')
            finalizacaoTR = st.text_input('Finalização Transição:', placeholder='Ex: 30')
            finalizacaoBP = st.text_input('Finalização Bola Parada:', placeholder='Ex: 60')

    with tab3:
        st.subheader('Cadastrar Informações Adversário', divider='gray')
        column7, column8, column9 = st.columns(3)
        with column7:
            posseGeralADV = st.text_input('Posse Geral ADV:', placeholder='Ex: 40')
            posseOfensivaADV = st.text_input('Posse Ofensiva ADV:', placeholder='Ex: 15')
            posseMeioADV = st.text_input('Posse Meio ADV:', placeholder='Ex: 14')
            posseDefensivaADV = st.text_input('Posse Defensiva ADV:', placeholder='Ex: 11')
            golADV = st.text_input('Gols ADV:', placeholder='Ex: 1')
            finaGeralADV = st.text_input('Finalizações ADV:', placeholder='Ex: 90')
        
        with column8:
            finaGolADV = st.text_input('Finalização no Gol ADV:', placeholder='Ex: 10')
            chanceClaraADV = st.text_input('Chance Clara ADV:', placeholder='Ex: 15')
            cruzaCertoADV = st.text_input('Cruzamentos ADV:', placeholder='Ex: 10')
            cruzaErradoADV = st.text_input('Cruzamentos Errados ADV:', placeholder='Ex: 25')
            passeCertoADV = st.text_input('Passes Certos ADV:', placeholder='Ex: 150')
            passeErradoADV = st.text_input('Passes Errados ADV:', placeholder='Ex: 80')
            
        with column9:
            passeLongoADV = st.text_input('Passes Longos Certos ADV:', placeholder='Ex: 18')
            passeLongoErradoADV = st.text_input('Passes Longos Errados ADV:', placeholder='Ex: 30')
            finalizacaoOrgADV = st.text_input('Finalização Organizada ADV:', placeholder='Ex: 90')
            finalizacaoTRADV = st.text_input('Finalização Transição ADV:', placeholder='Ex: 30')
            finalizacaoBPADV = st.text_input('Finalização Bola Parada ADV:', placeholder='Ex: 60')

    st.divider()

    button_dadosJogo = st.button("Cadastrar Jogo")
    infoADV = [posseGeralADV, posseDefensivaADV, posseMeioADV, posseOfensivaADV, golADV, finaGeralADV, finaGolADV, chanceClaraADV, cruzaCertoADV, 
               cruzaErradoADV, passeLongoADV, passeLongoErradoADV, passeCertoADV, passeErradoADV, finalizacaoOrgADV, finalizacaoTRADV, finalizacaoBPADV]
    infoJogo = [adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo]
    infoColetivo = [posseGeral, posseOfensiva, posseMeio, posseDefensiva, passeCerto,  finalizacaoOrg,
                     finalizacaoTR, finalizacaoBP]

    if button_dadosJogo:

        #cadastrarColetivo.cadastrarColetivo(infoJogo, listaAtletasFiltered, infoColetivo, df)
        #cadastrarADV.cadastrarADV(infoJogo, infoADV)
        
        #try:
            with st.status("Cadastrando Jogo..."):
                filtrarDataFrame.filtrarDataFrame(infoJogo, infoColetivo, listaAtletasFiltered, listaGoleiros, df)

            st.success(f"Cadastro de {adversarioData}, concluído!")

        #except Exception as e:
        #    st.error("Ocorreu um erro durante o cadastro, Contate seu Desenvolvedor.")
            
def limparVariaveis():
    clickButtonKey = 'clickButton'
    session_state.listaPosicao = []
    st.session_state[clickButtonKey] = 0


