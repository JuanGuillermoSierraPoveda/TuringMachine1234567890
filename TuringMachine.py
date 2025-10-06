class TuringMachine:
    def __init__(self, 
                 cinta: str, 
                 espacio_en_blanco: str, 
                 estados: list, 
                 alfabeto_inicial: list, 
                 alfabeto_cinta: list, 
                 transicion: dict, 
                 estado_inicial: str, 
                 estado_final: list):
        """
        cinta: cadena inicial en la cinta
        espacio_en_blanco: símbolo en blanco
        estados: lista de estados
        input_alphabet: símbolos de entrada
        tape_alphabet: símbolos permitidos en la cinta
        transitions: dict con transiciones {(estado, simbolo): (nuevo_estado, nuevo_simbolo, movimiento)}
        start_state: estado inicial
        final_states: lista de estados de aceptación
        """
        self.cinta = list(cinta)
        self.espacio_en_blanco = espacio_en_blanco
        self.estados = estados
        self.alfabeto_inicial = alfabeto_inicial
        self.alfabeto_cinta = alfabeto_cinta
        self.transicion = transicion
        self.state = estado_inicial
        self.estado_final = estado_final
        self.punto_que_se_evalua = 0

    def step(self):
        if self.punto_que_se_evalua < 0:
            self.cinta.insert(0, self.espacio_en_blanco)
            self.punto_que_se_evalua = 0
        elif self.punto_que_se_evalua >= len(self.cinta):
            self.cinta.append(self.espacio_en_blanco)

        symbol = self.cinta[self.punto_que_se_evalua]
        key = (self.estados, symbol)

        if key not in self.transicion:
            return False 

        estado_nuevo, new_symbol, move = self.transicion[key]

        self.cinta[self.punto_que_se_evalua] = new_symbol
        self.estados = estado_nuevo
        if move == "R":
            self.punto_que_se_evalua += 1
        elif move == "L":
            self.punto_que_se_evalua -= 1
        return True
    
    def run(self, max_steps=1000):
        """Corre la máquina completa hasta detenerse o llegar a max_steps"""
        steps = 0
        while self.estados not in self.estado_final and steps < max_steps:
            if not self.step():
                break
            steps += 1
        return "".join(self.cinta), self.estados
    
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
