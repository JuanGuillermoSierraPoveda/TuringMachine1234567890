from TuringMachine import TuringMachine
if __name__ == "__main__":
    estados = ["q0", "qf"]
    alfabeto_inicial = ["0", "1"]
    alfabeto_cinta = ["0", "1", "_"]
    transicion = {
        ("q0", "0"): ("q0", "1", "R"),
        ("q0", "1"): ("q0", "0", "R"),
        ("q0", "_"): ("qf", "_", "R")
    }
    
    tm = TuringMachine(cinta="10101",
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