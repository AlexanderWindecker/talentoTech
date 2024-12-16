import sqlite3 #Importo el modulo a trabajar

#print('SQLite version:', sqlite3.sqlite_version) # Vemos la version

def connect_db():
    conn = sqlite3.connect('inventario.db') #Como conectar la conexion
    return conn                             
    
#Creamos una tabla (si no existe)
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        quantity REAL NOT NULL,
        category TEXT NOT NULL
        
    )
    """)

#Inserta datos en DB    
def insert_data(name,description,price, quantity, category):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (name, description, price, quantity, category) VALUES (?, ?, ?, ?, ?)", (name, description, price, quantity, category))
    conn.commit()
    
def product_exist(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM product WHERE name = ?", (name, ))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0
    
#Traer todos los productos de base de datos    
def get_all_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()  
    conn.close()

    product_list = []
    for prod in products:
        product_list.append({
            'id': prod[0],
            'name': prod[1],
            'description': prod[2],
            'price': prod[3],
            'quantity': prod[4],
            'category': prod[5]
        })
        
    return product_list

# Traer productos de base de datos por nombre
def get_product_by_name(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE name = ?", (name,))
    product = cursor.fetchone()
    conn.close()
    if product:
        return {
            'id': product[0],
            'name': product[1],
            'description': product[2],
            'price': product[3],
            'quantity': product[4],
            'category': product[5]
        }
    return None

#Actualizar producto de base de datos
def update_product_in_db(product_id, new_name=None, new_description=None, new_price=None, new_quantity=None, new_category=None):
    conn = connect_db()
    cursor = conn.cursor()
    
    if new_name:
        cursor.execute("UPDATE product SET name = ? WHERE id = ?", (new_name, product_id))
    if new_description:    
        cursor.execute("UPDATE product SET description = ? WHERE id = ?", (new_description, product_id))
    if new_price:
        cursor.execute("UPDATE product SET price = ? WHERE id = ?", (new_price, product_id))
    if new_quantity is not None:
        cursor.execute("UPDATE product SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    if new_category:
        cursor.execute("UPDATE product SET category = ? WHERE id = ?", (new_category, product_id))
    
    conn.commit()
    conn.close()

# Eliminar producto de base de datos    
def delete_product_by_db(product_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE name = ? ", (product_name,))
    conn.commit()
    conn.close()

# Trae stock de productos ordenados en manera ascendente    
def stock_product(stock_min, stock_max):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE quantity BETWEEN ? AND ? ORDER BY quantity ASC", (stock_min, stock_max))
    products = cursor.fetchall()
    conn.commit()
    conn.close()
    
    
    product_list = []
    for prod in products:
        product_list.append({
            'id': prod[0],
            'name': prod[1],
            'description': prod[2],
            'price': prod[3],
            'quantity': prod[4],
            'category': prod[5]
        })
        
    return product_list


    
    

# Maneja 5 tipos de datos:
# NULL: para valores sin datos,como un campo vacio
# INTEGER: para numeros enteros,como contadores o identificadores
# REAL: para numeros decimales,como precios o mediciones
# TEXT: para almacenar texto,como nombres o descripciones
# BLOB: para datos binarios,como imagenes o archivos


#confirma los cambios, es importante porque confirma y guarda los cambios
#conn.commit()

#Cerrar la conexion
#conn.close()

#insertar valores
# cursor.execute("INSERT INTO clientes (name, ) VALUES ('')")

# conn.commit()


#insertar multiples de valores
# clientes = [
#     ('Juan', 'juan@gmail.com'),
#     ('Pedro', 'pedro@gmail.com'),
#     ('Maria', 'maria@gmail.com'),
    
# ]

# cada tupla representa una fila de datos a insertar en la tabla
#y cada valor dentro de la tupla corresponde a una columna de la tabla
# cursor.executemany("INSERT INTO clientes (nombre, correo) VALUES (?, ?)", clientes)

#confirmamos los cambios
# conn.commit()

#si trabajamos con un diccionario
#lista de diccionarios

# clientes_tuplas = []
# for cliente in clientes:
#     clientes_tuplas.append((cliente['nombre'], cliente['correo']))
    
# cursor.executemany("INSERT INTO clientes (nombre, correo) VALUES (?, ?)", clientes_tuplas)

# conn.commit()

#Accedemos a los valores
#consulta de datos
# cursor.execute("SELECT * FROM clientes")
#El SELECT es necesario apra obtener los registros que deseas recuperar, ya que es el comando SQL,
#que especifica que datos quieres consultar desde las tablas de la base de datos

#fetchone():
#Retorna la primera fila de la consulta, como una tupla. Si no hay filas devuelve None

#ejemplo
# fila = cursor.fetchone()
# print(fila)

# if fila:
#     cliente = {'id': fila[0], 'name': fila[0], 'correo': fila[0]}
    
# print(cliente)
# fetchmany(n):
# Devuelve las siguientes n filas del resultado de la consulta, como una lista de tuplas. Si no hay suficientes filas, devuelve tantas como haya.

# fetchall():
# Devuelve todas las filas del resultado de la consulta como una lista de tuplas.