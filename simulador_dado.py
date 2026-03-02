import random

def lanzar_dado():
    return random.randint(1, 6)

def mostrar_menu():
    print("\n--- SIMULADOR DE LANZAMIENTO DE DADO ---")
    print("1. Lanzar dado una vez")
    print("2. Lanzar dado múltiples veces")
    print("3. Salir")

def simulacion_multiple():
    try:
        cantidad = int(input("¿Cuántas veces deseas lanzar el dado? "))
        
        if cantidad <= 0:
            print("Debes ingresar un número mayor que cero.")
            return
        
        resultados = []
        
        for i in range(cantidad):
            resultado = lanzar_dado()
            resultados.append(resultado)
        
        print("\nResultados obtenidos:")
        print(resultados)
        
        print("\nFrecuencia de cada número:")
        for numero in range(1, 7):
            print(f"Número {numero}: {resultados.count(numero)} veces")
        
        promedio = sum(resultados) / len(resultados)
        print(f"\nPromedio obtenido: {promedio:.2f}")
        
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            resultado = lanzar_dado()
            print(f"\nEl resultado fue: {resultado}")
        
        elif opcion == "2":
            simulacion_multiple()
        
        elif opcion == "3":
            print("Gracias por usar el simulador. ¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
