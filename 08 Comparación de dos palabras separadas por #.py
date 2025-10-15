from TuringMachine import TuringMachine
states={
    "q0":{"0":["R"],"1":["R","q1"],"_":["R","qf"]},
    "q1":{"0":["R","q2"],"1":["R","q0"],"#":["R"]},
    "q2":{"0":["R","q1"],"1":["R"],"#":["R"]},
    "qf":"E"}
input="101#101"
start="q0"
alph=["0","1","_","#"]
tm=TuringMachine(states,input,start,alph)
tm.run()