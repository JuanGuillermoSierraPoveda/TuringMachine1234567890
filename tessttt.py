def replacement(input,index,val):
    ninp=""
    added=""
    if index<0:
        for y in range(0,abs(index)):
            print(y)
            if y==0:
                ninp=val
            else:
                added=added+"_"
        ninp=val+added
        index=index-len(input)
            
    elif index>(len(input)-1):
        for y in range(0,(index-(len(input)-1))):
            if y==(index-(len(input))):
                ninp=val
            else:
                added=added+"_"
        ninp=added+ninp
    for x in range(0,len(input)):#input 1001, etc
        try:
            vo=input[index]
        except IndexError:
            if index<0:
                ninp=ninp+input
                return ninp
            elif index>(len(input)-1):
                ninp=input+ninp
                return ninp
        else:
            print("nofallo",input[x])
            if x==index:
                ninp=ninp+val
            else:
                ninp=ninp+input[x]
    return ninp

def blankswap(input,dat1):#input es el dato inicial, dat1 es el indice actual
    if dat1<0:
        dat1=dat1-len(input)-1
    else:
        try:
            input[dat1]
        except IndexError:
            datoactual="_"
        else:
            datoactual=input[dat1]
    return datoactual #retorna el dato actualmente usado





input="001"
index=5
val="3"
input=replacement(input,index,val)
print(input)