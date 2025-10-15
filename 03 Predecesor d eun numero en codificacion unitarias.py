from TuringMachine import TuringMachine

if __name__ == "__main__":
    # Ejercicio 3: Predecesor en codificación unaria
    states = {
        "q0": {"1": ["R", "q0"], "_": ["L", "q1"]},
        "q1": {"1": ["w", "_", "L", "qf"]},
        "qf": "E"
    }

    input = "1111"
    start = "q0"
    alph = ["1", "_"]

    print("Inicio: Predecesor unario")
    TuringMachine(states, input, start, alph)
