from clases.operaciones import Operaciones 

def main():
    op = Operaciones()
    op.leerNumeros()

    while True:
        print("\n=== MENÚ DE OPERACIONES ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Módulo (resto)")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            op.sumar()
        elif opcion == "2":
            op.restar()
        elif opcion == "3":
            op.multiplicar()
        elif opcion == "4":
            op.dividir()
        elif opcion == "5":
            op.modulo()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")
            continue

        op.mostrarResultado()

if __name__ == "__main__":
    main()
