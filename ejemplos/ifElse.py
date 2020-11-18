a = int(input('hola como vas dame un numero'))
b= int (input('dame otro numero para la magia'))
c= int (input('no te aburras dame el ultimo'))
if a>b and a>c:
    print("el dato mas grade es a")
else: 
    if b>a and b>c:
        print("el dato mas grande es b")
    else:
        if c>a and c>b :       
            print("el dato mas grande es c")

