import os
import time
from .data import insert_data, get_all_products, get_product_by_name, update_product_in_db, delete_product_by_db, stock_product, product_exist
from colorama import init, Fore

#Inicia colorama
init(autoreset=True)

#Funcion de cargando
def loading():
    for i in range(10):
        print(f"{Fore.CYAN}Cargando programa, aguarde un momento por favor...{Fore.RESET}", end='\r')
        time.sleep(0.5)

        
# Limpiar consola
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Header de productos
def view_header():
    print("\n" + "=" * 114)
    print("{:^114}".format("🌟 LISTA DE PRODUCTOS 🌟"))
    print("=" * 114)
    print(f"| {'ID':^5} | {'Nombre':^25} | {'Descripcion' :^25} | {'Precio':^10} | {'Cantidad':^10} | {'Categoría':^20} |")
    print("=" * 114)

#Menu principal    
def menu_principal():

    while True:    
        print("\n" + "=" * 50)
        print("{:^50}".format("🌟 MENÚ PRINCIPAL 🌟"))  
        print("=" * 50)
        print("{:<5} ➤ {:<30}".format("1.", " Agregar un producto"))
        print("{:<5} ➤ {:<30}".format("2.", " Mostrar productos"))
        print("{:<5} ➤ {:<30}".format("3.", " Actualizar un producto"))
        print("{:<5} ➤ {:<30}".format("4.", " Eliminar un producto"))
        print("{:<5} ➤ {:<30}".format("5.", " Control de Stock"))
        print("{:<5} ➤ {:<30}".format("6.", " Buscar producto"))
        print("{:<5} ➤ {:<30}".format("7.", " Salir"))
        print("=" * 50 + "\n")
        try:
            print(' ')
            opcion = int(input('Ingrese la opción deseada: ').strip())
            print(' ')
        except ValueError:
            print('Error: La opción ingresada no es un número.')
            continue

        if opcion == 1:    
            add_product()
        elif opcion == 2:
            view_product()
        elif opcion == 3:
            update_product()        
        elif opcion == 4:
            delete_product() 
        elif opcion == 5:
            range_stock()
        elif opcion == 6:
            search_product()
        elif opcion == 7:
            clear_screen()          
            print('Hasta luego!')
            print('\nDesarrollado por @Alexander Windecker - 2024')
            break
        else:
            print('Opción inválida.')

#Imprimir productos    
def print_prod(prod):    
    return f"| {prod['id']:^5} | {prod['name']:^25} | {prod['description']:<25} | {prod['price']:^10.2f} | {prod['quantity']:^10} | {prod['category']:^20} |"
       
    
#Agregar producto
def add_product():
    while True:
        name = input("\nIngrese el nombre del producto: ").strip().title()
        if name:
            break 
        
    if product_exist(name):
        print(Fore.RED + f"\nError, El producto {name} ya existe en la base de datos")
        return
    
    description = input("\nIngrese una breve descripcion del producto: ")    
    
    while True: 
        try:
            price = float(input("\nPrecio del producto: ").strip())
            break
        except ValueError:
            print(Fore.RED + "\nError: El precio debe ser un númerico.")
        
    while True: 
        try:
            quantity = int(input("\nCantidad del producto: ").strip())
            break
        except ValueError:
            print(Fore.RED + "\nError: La cantidad debe ser un número.")
        
    while True:
        category = input("\nCategoría del producto: ").strip().title()
        if category.isalpha() or " " in category:
            break  
        else:
            print(Fore.RED + "\nError: La categoria NO es valida. Debe contener solo letras y espacios.")
   
    insert_data(name, description, price, quantity, category)
    print(Fore.GREEN + f"\nProducto '{name}' agregado con éxito.")
    
#Mostrar productos    
def view_product(): 
    products = get_all_products()
    loading()    
    if products:  # Verifico si hay productos
        view_header()
        for prod in products:
            print(print_prod(prod))
    else:
        print(Fore.RED + " No hay productos para mostrar. ")

#Actualizar producto        
def update_product():
    products = get_all_products()
    if not products:
        print(Fore.RED + "\nNo hay productos disponibles para actualizar.")
        return

    while True:
        name = input("\nIngrese el nombre del producto a actualizar (o presione Enter para salir): ").strip().title()
        
        if not name:  
            break

        producto_existente = get_product_by_name(name)

        if producto_existente:
            new_name = input(f"\nNuevo nombre para '{name}' (presiona Enter para mantener el mismo): ").strip().title()
            if not new_name:
                new_name = producto_existente['name']
                
            new_description = input(f"\nNueva descripcion para '{new_name}' (presiona Enter si desea conservar la descripcion): ").strip().title()
            if not new_description:
                new_description = producto_existente['description']
            
            new_price_input = input(f"\nNuevo precio para '{new_name}' (presiona Enter para mantener el mismo): ").strip()
            if new_price_input:
                try:
                    new_price = float(new_price_input)
                except ValueError:
                    print(Fore.RED + "\nError: El precio debe ser un número.")
                    new_price = producto_existente['price']
            else:
                new_price = producto_existente["price"]
                
            new_quantity_input = input(f"\nNueva cantidad para '{new_name}' (presiona Enter para mantener el mismo): ").strip()
            if new_quantity_input:
                try:
                    new_quantity = int(new_quantity_input)
                except ValueError:
                    print(Fore.RED + "\nError: La cantidad debe ser un número.")
                    new_quantity = producto_existente['quantity']
            else:
                new_quantity = producto_existente["quantity"]

            new_category = input(f"\nNueva categoría para '{new_name}' (presiona Enter para mantener la misma): ").strip().title()
            if not new_category:
                new_category = producto_existente['category']
            
            update_product_in_db(
                producto_existente['id'], 
                new_name, 
                new_description, 
                new_price, 
                new_quantity, 
                new_category
                )            
            
            print(Fore.GREEN + f"\nProducto '{new_name}' actualizado exitosamente.")
            break  

        else:
            print(Fore.RED + f"\nEl producto '{name}' no existe. Intente nuevamente.")
            
#Eliminar producto           
def delete_product():
    products = get_all_products()
    if not products:
        print(Fore.RED + "\nNo hay productos registrados para eliminar.")
        return
    
    name = input("\nNombre del producto a eliminar: ").strip()    
       
    for prod in products:
        if prod["name"].lower() == name.lower():
            confirmation = input(f"\nEstas seguro de eliminar el producto {name}: \nIngrese 1 para SI \nIngrese 2 para NO \nOpcion ingresada: ").strip()
            if confirmation == "1":
                delete_product_by_db(prod['name'])
                print(Fore.GREEN + f"\nProducto '{name}' eliminado con éxito.")
                return
            elif confirmation == "2":
                print(f"\nEliminación del producto '{name}' cancelada.")
            else:
                print("\nOpcion incorrecta, la eliminacion a sido cancelada")
            return    
            
    print(Fore.RED + f"\nNo se encontró un producto con el nombre '{name}'.")

#Mostrar por stock min y max    
def range_stock():
    try:
        stock_min = int(input('\nIngrese el stock minimo deseado: '))
        stock_max = int(input('\nIngrese el stock maximo deseado: '))
        
        product_in_range = stock_product(stock_min, stock_max)       
    
        if product_in_range:
            view_header()
            for prod in product_in_range:
                print(print_prod(prod))
                
        else:
            print(Fore.RED + f"\nNo hay productos en el rango especificado")
            
       
    except ValueError:
        print(Fore.RED + '\nPor favor ingrese valores numericos')
    
#Buscar producto
def search_product():
    products = get_all_products()
    if not products:
        print(Fore.RED + "\nNo hay productos registrados para buscar.")
        return
    name = input("\nNombre del producto a buscar: ").strip()
    
    for prod in products:
        if prod["name"].lower() == name.lower():
            view_header()
            print(print_prod(prod))