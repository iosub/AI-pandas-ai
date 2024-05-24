
query = text("""SELECT [Id_CLIENTE], [Id_EMPRESA] , [CODCLI] , [DENOMI] FROM Cliente""")

conn=engine.connect()

cliente = pd.read_sql_query(query, conn)#, encoding='cp1252')
queryf = text("""SELECT Id_FACTURA,Id_EMPRESA,TIPOREG,FACTURA,[FECHAF],[Id_CLIENTE],[Total]  FROM T_FACTURA""")
facturas = pd.read_sql_query(queryf, conn)#, encoding='cp1252'
agent = Agent(
    [facturas,cliente], 
    config={"direct_sql": True}
)
response = agent.chat("total de facturacion del cliente 'GRUPO MZ' agrupado por años")
print(response)
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql_query.html#pandas-read-sql-query
# Id_FACTURA,Id_EMPRESA,TIPOREG,FACTURA,[FECHAF],[Id_CLIENTE],[Total]
#>>> from sqlalchemy import create_engine  
#>>> engine = create_engine("sqlite:///database.db")  
#>>> with engine.connect() as conn, conn.begin():  
#...     data = pd.read_sql_table("data", conn)  
with engine.connect() as conn, conn.begin():  
    queryf = text("""SELECT Id_FACTURA,Id_EMPRESA,TIPOREG,FACTURA,[FECHAF],[Id_CLIENTE],[Total]  FROM T_FACTURA""")
    facturas = pd.read_sql_query(queryf, conn)#, encoding='cp1252'
    query = text("""SELECT [Id_CLIENTE], [Id_EMPRESA] , [CODCLI] , [DENOMI] FROM Cliente""")
    cliente = pd.read_sql_query(query, conn)
    agent1 = Agent([facturas,cliente])#, config={"direct_sql": True})

response = agent1.chat("total de facturacion del cliente 'GRUPO MZ' agrupado por años")
print(response)   

sdf = SmartDataframe(facturas)#, config={"llm": ollama_llm})
response = sdf.chat("al invoices")
print(response)
agent = Agent(
    [facturas,cliente],
    config={"direct_sql": True},
)
response = agent.chat("total de facturacion del cliente 'GRUPO MZ' agrupado por años")
print(response)

with engine.begin() as conn:
    query = text("""SELECT [Id_CLIENTE], [Id_EMPRESA] , [CODCLI] , [DENOMI] FROM Cliente""")
    cliente = pd.read_sql_query(query, conn)#, encoding='cp1252')

#https://stackoverflow.com/questions/46000191/utf-8-codec-cant-decode-byte-0x92-in-position-18-invalid-start-byte
agent = Agent(
    [facturas, cliente],
    config={"direct_sql": True},
)
response = agent.chat("give me a list of invoices")

response = agent.chat("total de facturacion del cliente 'GRUPO MZ' agrupado por años")
print(response)

DB = {'servername': 'lenovo12',
      'database': 'iatest'}
# create the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['servername'] + ';DATABASE=' + DB['database'] + ';Trusted_Connection=yes')
df = pd.read_sql_query('SELECT * FROM T_FACTURA',conn)

facturas = SQLConnector(
    config={
        "dialect": "mssql",
        "driver": "pyodbc",
        "host": "lenovo12",
        "port": 1433,
        "database": "iatest",
        "username": "gg",
        "password": "ostia",
        "table": "T_FACTURA",
     
        
    }
)
cliente = SQLConnector(
    config={
        "dialect": "pyodbc",
        "driver": "mssql",
        "host": "lenovo12",
      #  "port": 3306,
        "database": "iatest",
        "username": "gg",
        "password": "ostia",
        "table": "CLIENTE"
    }
)


#conn_str = "mssql+pyodbc://gg:ostia@lenovo12/iatest?driver=ODBC+Driver+17+for+SQL+Server"
#sql_connector = SQLConnector(




# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
#os.environ["PANDASAI_API_KEY"] = "your-api-key"
