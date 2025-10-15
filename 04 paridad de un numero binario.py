from TuringMachine import TuringMachine

if __name__ == "__main__":
    
    states = {
        
        "q0": {
            "0": ["R", "q0"],   
            "1": ["R", "q1"],   
            "_": ["w", "0", "L", "qf"]  
        },
        
        "q1": {
            "0": ["R", "q1"],   
            "1": ["R", "q0"],   
            "_": ["w", "1", "L", "qf"]  
        },
        "qf": "E"
    }

    input = "1011"
    start = "q0"
    alph = ["0", "1", "_"]

    print("Inicio: Paridad de número binario")
    TuringMachine(states, input, start, alph)
