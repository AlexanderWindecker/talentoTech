from productos.gestion import menu_principal, loading
from productos.data import create_table

create_table()
# loading()
menu_principal()

# while True:
#     # Llamo la funcion del menu.

#     try:
#         print(' ')
#         opcion = int(input('Ingrese la opción deseada: ').strip())
#         print(' ')
#         gestion.clear_screen()          
#     except ValueError:
#         print('Error: La opción ingresada no es un número.')
#         continue

#     if opcion == 1:    
#         gestion.add_product()
#     elif opcion == 2:
#         gestion.view_product()
#     elif opcion == 3:
#         gestion.update_product()        
#     elif opcion == 4:
#         gestion.delete_product() 
#     elif opcion == 5:
#         gestion.range_stock()
#     elif opcion == 6:
#         gestion.clear_screen()          
#         print('Hasta luego!')
#         print('\nDesarrollado por @Alexander Windecker - 2024')
#         break
#     else:
#         print('Opción inválida.')
