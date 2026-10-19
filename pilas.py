def menu_pila():
    pila = []
    
    while True:
        print("\n" + "="*35)
        print("          MENÚ DE PILA (LIFO)")
        print("="*35)
        print("1. Insertar en pila (Push)")
        print("2. Borrar en pila (Pop)")
        print("3. Listar pila")
        print("4. Salir al menú principal")
        print("="*35)
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            try:
                num = float(input("\nIngrese el número a agregar a la pila: "))
                pila.append(num)
                print(f"-> ¡Éxito! El número {num} ha sido colocado en la cima de la pila.")
            except ValueError:
                print("-> Error: Debe ingresar un valor numérico válido.")
                
        elif opcion == "2":
            if len(pila) == 0:
                print("\n-> La pila está vacía. No hay elementos para desapilar.")
            else:
                eliminado = pila.pop()  # LIFO: Remueve el último elemento ingresado
                print(f"-> ¡Éxito! Se removió el último elemento ingresado (Cima): {eliminado}")
                
        elif opcion == "3":
            print("\n--- ESTADO ACTUAL DE LA PILA ---")
            if len(pila) == 0:
                print("La pila se encuentra VACÍA.")
            else:
                print("CIMA")
                for elem in reversed(pila):
                    print(f" | {elem} |")
                print("BASE")
                print(f"Total de elementos: {len(pila)}")
                
        elif opcion == "4":
            print("\nSaliendo de la gestión de la pila...")
            break
        else:
            print("-> Opción inválida. Por favor, elija un número entre 1 y 4.")

def main():
    while True:
        menu_pila()
        
        # Pregunta de repetición
        respuesta = input("\n¿Desea ejecutar nuevamente el programa de Pilas? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n¡Gracias por utilizar el sistema! Hasta luego.")
            break

if __name__ == "__main__":
    main()