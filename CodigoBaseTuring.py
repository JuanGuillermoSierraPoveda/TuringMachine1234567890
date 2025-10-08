import sys
def TuringMachine(states,input,start,alph):
    i=0
    actval=input[i]
    insidealph(actval,alph)
    lop=True
    change=True
    while lop:
        if states[start]=="E":
                print(input)
                sys.exit(0)

        for x in range(0,len(states[start][actval])):#start es el estado ejecutando, actval el valor activo
            print(input,actval,i)
            print(x, "indice")

            if states[start][actval][x]=="w":
                print("w","entro",states[start][actval][x+1])
                input=replacement(input,i,states[start][actval][x+1])
                if len(states[start][actval])>x+2:
                    x=x+2
                    change=False
                insidealph(actval,alph)
                actval=blankswap(input,i)
            
            if states[start][actval][x]=="R":
                print("r")
                try:
                    print(states[start][actval][x+1])
                except IndexError:
                        i=i+1
                        insidealph(actval,alph)
                        actval=blankswap(input,i)

                else:
                    if ((states[start][actval][x+1]) in states) and change:
                        i=i+1
                        start=states[start][actval][x+1]                        
                        insidealph(actval,alph)
                        actval=blankswap(input,i)
                    else:
                        i=i+1
                        insidealph(actval,alph)
                        actval=blankswap(input,i)
                        if not change:
                            x=x-2
                            change=True

            elif states[start][actval][x]=="L":
                print("l")
                try:
                    vol=states[start][actval][x+1]
                except IndexError:
                        i=i-1
                        print(i,"error")
                        insidealph(actval,alph)
                        actval=blankswap(input,i)
                else:
                    if (states[start][actval][x+1]) in states and change:
                        i=i-1
                        start=states[start][actval][x+1]
                        insidealph(actval,alph)
                        actval=blankswap(input,i)
                        print(start,"estado cam")
                    else:
                        i=i-1
                        print(i,"noer")
                        insidealph(actval,alph)
                        actval=blankswap(input,i)
                        if not change:
                            x=x-2
                            change=True


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
input="0001"
start="q0" 
alph=["0","1","_"]
print("inicio")
TuringMachine(states,input,start,alph)
