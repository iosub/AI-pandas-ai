"""Example of using PandasAI with a CSV file."""
import os
from dotenv import load_dotenv

from pandasai import Agent
#from pandasai.connectors import PostgreSQLConnector
from pandasai.connectors import SQLConnector

load_dotenv()
tables=["T_FACTURA","CLIENTE"]
conn_str = "mssql+pyodbc://gg:ostia@lenovo12/iatest?driver=ODBC+Driver+17+for+SQL+Server"
#from sqlalchemy.engine import URL
#connection_string = "DRIVER={SQL Server Native Client 10.0};SERVER=dagger;DATABASE=test;UID=user;PWD=password"
#connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

#engine = create_engine(connection_url)
#pp= SQLConnector()  .from_uri(conn_str,include_tables=tables,lazy_table_reflection=True  )#,custom_table_info=table_info2)
#sql_connector = SQLConnector(
   # config={
   #/     "dialect": "pyodbc",
    #    "driver": "mssql",
   #     "host": "lenovo12",
      #  "port": 3306,
  #      "database": "iatest",
    #    "username": "gg",
   #     "password": "ostia",
   #     "table": "T_FACTURA",
    #    "where": [
    #            /#
            # this is optional and filters the data to
            # reduce the size of the dataframe
    #        ["loan_status", "=", "PAIDOFF"],
    #    ],
   # }
 #  pip install sqlalchemy-pyodbc-mssql -U  
#sqlalchemy.dialects:pyodbc.mssq
# pip install sqlalchemy-dialects-pyodbc-mssql   
#conn_str = "mssql+pyodbc://gg:ostia@lenovo12/iatest?driver=ODBC+Driver+17+for+SQL+Server"
conn_str = "mssql+pyodbc://gg:ostia@lenovo12/iatest?driver=ODBC+Driver+17+for+SQL+Server"
#f=SQLConnector(conn_str)

import pyodbc
import pandas as pd
import sqlalchemy as sal
from sqlalchemy import create_engine
from pandasai import SmartDataframe
from pandasai.llm.local_llm import LocalLLM
from sqlalchemy import text

#https://github.com/Sinaptik-AI/pandas-ai/blob/main/docs/llms.mdx
ollama_llm = LocalLLM(api_base="http://localhost:11434/v1", model="Dolphin-llama3:8b",temperature=0)
#ollama_llm = LocalLLM(api_base="http://localhost:11434/v1", model="llama3", temperature=0)#, max_tokens=32768)

#ollama_llm = LocalLLM(api_base="http://localhost:11434/v1", model="mistral:latest")#, temperature=0)#, max_tokens=32768)

#df = SmartDataframe("data.csv", config={"llm": ollama_llm})

engine = create_engine("mssql+pyodbc://gg:ostia@lenovo12/iatest?driver=ODBC+Driver+17+for+SQL+Server")
#...     data = pd.read_sql_table("data", conn)  
with engine.connect() as conn, conn.begin():  
    queryf = text("""SELECT Id_FACTURA,Id_EMPRESA,TIPOREG,FACTURA,FECHAF,Id_CLIENTE,Total  FROM T_FACTURA""")
    facturas = pd.read_sql_query(queryf, conn)#, encoding='cp1252'
    query = text("""SELECT Id_CLIENTE, Id_EMPRESA , CODCLI , DENOMI FROM Cliente""")
    cliente = pd.read_sql_query(query, conn)
    agent1 = Agent([facturas,cliente])#, config={"direct_sql": True})
    agent2 = Agent([facturas,cliente], config={"llm": ollama_llm})

#response = agent1.chat("total de facturacion del cliente 'GRUPO MZ' agrupado por años muestrame en el resultado el nombre del cliente")
#response = agent1.chat("total de facturacion del cliente 'GRUPO MZ' agrupado por años y muestrame en la respuesta El nombre del cliente")
#Me funcionóresponse = agent1.chat("total de facturacion del cliente 'GRUPO MZ' agrupado por años. El resultado muestra También el nombre del cliente")
#response = agent1.chat("Muestra las facturas del cliente con denomi 'GRUPO MZ'  ")
#response = agent1.chat("Muestra las facturas del cliente con denomi 'GRUPO MZ'  ")
#response = agent1.chat("total de facturacion por cliente  agrupado por años Y ordenado por la mayor facturación. En El resultado muestra También el nombre del cliente")

#response = agent1.chat("total de facturacion del cliente 'GRUPO MZ' agrupado por años muestrame en el resultado el nombre del cliente")
#response = agent1.chat("total de facturacion del cliente 'GRUPO MZ' agrupado por años y muestrame en la respuesta El nombre del cliente")
q="total de facturacion del cliente 'GRUPO MZ' agrupado por años. El resultado muestra También el nombre del cliente"
#response = agent1.chat("Muestra las facturas del cliente con denomi 'GRUPO MZ'  ")
#response = agent1.chat("Muestra las facturas del cliente con denomi 'GRUPO MZ'  ")
q1="total de facturacion por cliente  agrupado por años Y ordenado por el total de  facturación. En El resultado muestra También el nombre del cliente"
q1="total de facturacion por cliente  agrupado por años. En El resultado muestra También el nombre del cliente"
q1="total de facturacion   agrupado por Cliente. En El resultado muestra También el nombre del cliente"

q=" cuál ha sido el año con más facturación"
q="Total de facturación agrupado por años "
q="Total de facturación agrupado por años y ordenado por el total"
q=" cuál ha sido el año con la mayor facturación"
q=" cuál ha sido el año con más facturación"

#response = agent1.chat(q1)

#print(response)
print("Que funcione")
response = agent1.chat(q1)

print(response)
#conn.close()
#engine.dispose()


