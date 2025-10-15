# Ejercicio 5: Contador unario de {a,b,c}

cinta = list("abc_")  
indice = 0            
estado = "q0"         
iteracion = 0

print("Inicio: Contador unario de {a,b,c}\n")


while True:
    valor = cinta[indice]

    print(f"{''.join(cinta)} {estado} valor {valor} iteracion {iteracion} indice {indice}")
    iteracion += 1

    
    if estado == "q0":
        if valor in ["a", "b", "c"]:
            cinta[indice] = "X"  
            estado = "q1"        
            indice += 1
        elif valor == "_":
            
            cinta[indice] = "1"
            print("\nMáquina finalizada correctamente ✅")
            break

    
    elif estado == "q1":
        if valor in ["a", "b", "c", "X"]:
            indice += 1
        elif valor == "_":
            cinta[indice] = "1"  
            estado = "q2"        
            indice -= 1

    elif estado == "q2":
        if valor in ["X", "a", "b", "c"]:
            indice -= 1
        elif valor == "_":
            indice += 1
            estado = "q0"

    if indice < 0 or indice >= len(cinta) + 10:
        print("\n Se detectó un movimiento fuera de la cinta. ")
        break


print("\nResultado final de la cinta:")
print("".join(cinta))
