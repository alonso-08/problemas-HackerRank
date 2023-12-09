def palabra_corta(palabra):
    resultado=[]
    letra_inicial=None
    letra_final=None
    cantidad=len(palabra)-2
    if(len(palabra)>4) and len(palabra)>=1 and len(palabra)<=100:
        for index,letra in enumerate(palabra):
            
            if (index==0):
                letra_inicial=letra
                resultado.append(letra_inicial)
            elif index==len(palabra)-1:
                resultado.append(cantidad)
                letra_final=letra
                resultado.append(letra_final)

            else:
                pass
            
        resultado=''.join(map(str,resultado))
        return resultado
    else:
        return palabra

        

        


if __name__=="__main__":
    palabra=str(input("introduce una palabra: "))
    print(palabra_corta(palabra))
