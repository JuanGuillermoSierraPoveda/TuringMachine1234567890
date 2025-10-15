from TuringMachine import TuringMachine  # importa tu clase base

if __name__ == "__main__":
    # Ejercicio 6: Copiar una cadena
    states = {
        "q0": {
            "a": ["R", "q0"],
            "b": ["R", "q0"],
            "c": ["R", "q0"],
            "_": ["L", "q1"]
        },
        "q1": {
            "a": ["w", "A", "R", "q2"],
            "b": ["w", "B", "R", "q2"],
            "c": ["w", "C", "R", "q2"],
            "X": ["L", "q1"],
            "_": ["R", "qf"]
        },
        "q2": {
            "a": ["R", "q2"],
            "b": ["R", "q2"],
            "c": ["R", "q2"],
            "_": ["w", "_", "R", "q3"]
        },
        "q3": {
            "a": ["R", "q3"],
            "b": ["R", "q3"],
            "c": ["R", "q3"],
            "_": ["w", "a", "L", "q4"],
            "A": ["w", "a", "L", "q4"],
            "B": ["w", "b", "L", "q4"],
            "C": ["w", "c", "L", "q4"]
        },
        "q4": {
            "a": ["L", "q4"],
            "b": ["L", "q4"],
            "c": ["L", "q4"],
            "_": ["R", "q1"]
        },
        "qf": "E"
    }

    
    input = "abc_"
    alph = ["a", "b", "c", "A", "B", "C", "X", "_"]
    start = "q0"

    print("Inicio: Copia de cadena\n")
    TuringMachine(states, input, start, alph)
