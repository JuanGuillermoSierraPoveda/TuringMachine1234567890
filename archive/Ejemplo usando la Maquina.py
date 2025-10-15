from TuringMachine import TuringMachine
if __name__ == "__main__":
    estados = ["q0", "qf"]
    alfabeto_inicial = ["0", "1"]
    alfabeto_cinta = ["0", "1", "_"]
    transicion = {("q0", "0"): ("qf", "0", "R"),
                   ("q0", "1"): ("qf", "1", "R")}
    
    tm = TuringMachine(cinta="1011",
                       espacio_en_blanco="_",
                       estados=estados,
                       alfabeto_inicial=alfabeto_inicial,
                       alfabeto_cinta=alfabeto_cinta,
                       transicion=transicion,
                       estado_inicial="q0",
                       estado_final=["qf"])
    
    result, estado_final = tm.run()
    print("Resultado:", result)
    print("Estado final:", estado_final)
"Este es un ejemplo de la máquina de Turing que no cambia la cadena de entrada y se detiene inmediatamente."