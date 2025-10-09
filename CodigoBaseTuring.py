import sys
def TuringMachine(states,input,start,alph):
    i=0
    actval=input[i]
    insidealph(actval,alph)
    lop=True
    count=len(states[start][actval])
    change=True
    while lop:
        if states[start]=="E":
                print(input)
                sys.exit(0)
        print("iteracion")
        input,start,actval,i=TuringLoop(states,input,start,alph,actval,i)



            
def TuringLoop(states,input,start,alph,actval,i):
    actval1=""
    for x in range(0,len(states[start][actval])):#start es el estado ejecutando, actval el valor activo
        print(input,start,actval,x,i)

        if states[start][actval][x] in states:
            start=states[start][actval][x]
            actval=actval1

        if states[start][actval][x]=="w":
            #print("w",states[start][actval][x+1])
            input=replacement(input,i,states[start][actval][x+1])
            #print(input)
            insidealph(actval,alph)
            actval=blankswap(input,i)
            
        elif states[start][actval][x]=="R":
            print("r")
            if states[start][actval][x]==states[start][actval][-1]:
                i=i+1
                insidealph(actval,alph)
                actval=blankswap(input,i)

        elif states[start][actval][x]=="L":
            print("l")

            if states[start][actval][x]!=states[start][actval][-1]:# Si L Q1
                i=i-1
                insidealph(actval,alph)
                actval1=blankswap(input,i)
            else:#Si L
                i=i-1
                insidealph(actval,alph)
                actval=blankswap(input,i)
            

    return input,start,actval,i

def blankswap(input,dat1):#input es el dato inicial, dat1 es el indice actual
    if dat1<0:
        datoactual="_"
    else:
        try:
            input[dat1]
        except IndexError:
            datoactual="_"
        else:
            datoactual=input[dat1]
    return datoactual #retorna el dato actualmente usado

def insidealph(value,alph):
    if value in alph:
        return
    else:
        print("El valor no esta en el alfabeto")
        sys.exit(0)

def replacement(input,index,val):
    ninp=""
    for x in range(0,len(input)):
        if x==index:
            ninp=ninp+val
        else:
            ninp=ninp+input[x]
    return ninp

states={
    "q0":{"0":["R"],"1":["R"],"_":["L","q1"]},
    "q1":{"1":["w","0","L"],"0":["w","1","L","qf"],"_":["w","1","L","qf"]},
    "qf":"E"}
input="011"
start="q0" 
alph=["0","1","_"]
print("inicio")
TuringMachine(states,input,start,alph)
