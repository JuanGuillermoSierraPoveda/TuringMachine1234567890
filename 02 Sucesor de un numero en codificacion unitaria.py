from TuringMachine import TuringMachine

if __name__ == "__main__":
    
    states = {
        "q0": {"1": ["R", "q0"], "_": ["w", "1", "L", "qf"]},
        "qf": "E"
    }

    input = "111"
    start = "q0"
    alph = ["1", "_"]

    print("Inicio: Sucesor unario")
    TuringMachine(states, input, start, alph)
