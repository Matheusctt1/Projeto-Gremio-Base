import pyodbc
import streamlit as st

cnxn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={st.secrets["server"]};DATABASE={st.secrets["database"]};UID={st.secrets["username"]};PWD={st.secrets["password"]};TrustServerCertificate=yes;Trusted_Connection=yes;'
)

cursor = cnxn.cursor()

def init_connection():
    return cnxn.cursor()

conn = init_connection()
