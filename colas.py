
def menu_cola():
    cola = []
    
    while True:
        print("\n" + "="*35)
        print("          MENÚ DE COLA (FIFO)")
        print("="*35)
        print("1. Insertar en cola (Enqueue)")
        print("2. Borrar en cola (Dequeue)")
        print("3. Listar cola")
        print("4. Salir al menú principal")
        print("="*35)
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            try:
                num = float(input("\nIngrese el número a insertar en la cola: "))
                cola.append(num)
                print(f"-> ¡Éxito! El número {num} ha sido agregado al final de la cola.")
            except ValueError:
                print("-> Error: Debe ingresar un valor numérico válido.")
                
        elif opcion == "2":
            if len(cola) == 0:
                print("\n-> La cola está vacía. No hay elementos para eliminar.")
            else:
                eliminado = cola.pop(0)  # FIFO: Remueve el primer elemento
                print(f"-> ¡Éxito! Se eliminó el primer elemento ingresado: {eliminado}")
                
        elif opcion == "3":
            print("\n--- ESTADO ACTUAL DE LA COLA ---")
            if len(cola) == 0:
                print("La cola se encuentra VACÍA.")
            else:
                print("Frente ->", end=" ")
                for elem in cola:
                    print(f"[{elem}]", end=" <- ")
                print("Final")
                print(f"Total de elementos: {len(cola)}")
                
        elif opcion == "4":
            print("\nSaliendo de la gestión de la cola...")
            break
        else:
            print("-> Opción inválida. Por favor, elija un número entre 1 y 4.")

def main():
    while True:
        menu_cola()
        
        # Pregunta de repetición
        respuesta = input("\n¿Desea ejecutar nuevamente el programa de Colas? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n¡Gracias por utilizar el sistema! Hasta luego.")
            break

if __name__ == "__main__":
    main()