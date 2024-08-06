import mysql.connector
import Model.NotaGsm as NotaGsm
from mysql.connector import Error


# Configurações de conexão
config = {
    'user': '',
    'password': '',
    'host': '',
    'database': '',
    'raise_on_warnings': True
}

def criarConexao():
    conn = mysql.connector.connect(**config)

    # Criar um cursor para executar as consultas
    cursor = conn.cursor(dictionary=True)

    return cursor, conn

def findAll():
   
    try:
        conn = mysql.connector.connect(**config)

        # Criar um cursor para executar as consultas
        cursor = conn.cursor(dictionary=True)

        # Escrever a consulta SQL
        query = "select * from gsm_nota;"

        # Executar a consulta
        cursor.execute(query)

        resultados = cursor.fetchall()

        return resultados
    
    except Error as e:

        print(f"Erro: {e}")
        conn.rollback()



def findByTiqueteBalanca(tiqueteBalanca:int):

    try:
        conn = mysql.connector.connect(**config)

        # Criar um cursor para executar as consultas
        cursor = conn.cursor(dictionary=True)

        # Escrever a consulta SQL
        query = "select tiquete_balanca, comissao_motorista, peso, valor_frete from gsm_nota where tiquete_balanca = '"+tiqueteBalanca+"';"    
        
        # Executar a consulta
        cursor.execute(query)

        resultado = cursor.fetchone()

    except Error as e:

        print(f"Erro: {e}")
        conn.rollback()

    finally:

        if conn.is_connected():
            cursor.close()
            conn.close()

        return resultado



def CadastrarNotaGsm(nota:NotaGsm.NotaGsm):

    try:
        conn = mysql.connector.connect(**config)

        # Criar um cursor para executar as consultas
        cursor = conn.cursor(dictionary=True)

        # Escrever a consulta SQL
        query = "INSERT INTO gsm_nota (tiquete_balanca, comissao_motorista, peso, valor_frete) VALUES (%s, %s, %s, %s);"
        values = (nota.tiquete_balanca, nota.comissao_motorista, nota.peso, nota.valor_frete)

        # Executar a consulta
        cursor.execute(query,values)

        #Termina a operação no banco de dados
        conn.commit()

        return "200"


    except Error as e:

        print(f"Erro ao conectar ou inserir dados no MySQL: {e}")
        nota = "500"
        conn.rollback()

    finally:

        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexão ao MySQL encerrada")

   
