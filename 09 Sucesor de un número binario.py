from TuringMachine import TuringMachine
states={
    "q0":{"0":["R"],"1":["R"],"_":["L","q1"]},
    "q1":{"1":["w","0","L"],"0":["w","1","L","qf"],"_":["w","1","L","qf"]},
    "qf":"E"}
input="11"
start="q0"
alph=["0","1","_"]
tm=TuringMachine(states,input,start,alph)
tm.run()