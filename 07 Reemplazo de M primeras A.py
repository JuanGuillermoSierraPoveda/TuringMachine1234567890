from TuringMachine import TuringMachine
print("jue")
states={
    "q0":{"1":["w","_","R","q6"],"A":["L","qf"],"B":["L","qf"]},
    "q1":{"1":["R","q2"],"A":["L"],"B":["L"],"_":["R","qf"]},
    "q2":{"A":["R"],"B":["R"],"1":["R"],"_":["R","q3"]},
    "q3":{"A":["L"],"B":["L"],"1":["L"],"_":["R","q4"]},
    "q4":{"_":["R"],"1":["w","_","R","q5"]},
    "q5":{"1":["R"],"B":["R"],"A":["w","B","R","q1"]},
    "q6":{"0":["R"],"1":["R"],"A":["w","B","R","q7"]},
    "q7":{"A":["L"],"B":["L"],"1":["R","q1"]},
    "qf":"E"}
input="111AAAAB"
start="q0"
alph=["0","1","A","B","_"]
tm=TuringMachine(states,input,start,alph)
tm.run()