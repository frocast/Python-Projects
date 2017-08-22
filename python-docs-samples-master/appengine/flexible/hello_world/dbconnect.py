#_# coding:utf-8 #_#
import MySQLdb

def connection(host = "localhost", user = "root", passwd = "root", db = "python_test"):
    conn = MySQLdb.connect(host, user, passwd, db)
    cursor = conn.cursor()
    print "Conexion exitosa"
    return cursor, conn

def run_query(query = ''): 
 
    #conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    #cursor = conn.cursor()         # Crear un cursor 
    cursor, conn = connection()
    cursor.execute(query)          # Ejecutar una consulta 
 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
    
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 
    
    return data