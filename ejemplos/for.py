for nombre in ['dani','joce','sebas']:
    print('hola,{0}.'.format(nombre))
d=int(input('dame un nuemero para la tabla de multipicar'))
for i in range(1,11):
    print(d*i)
lista=(range(1,12))
m=int(input('dame el limete'))
n=int(input('dame desde que numero va comensar'))
for n in range(1,m):
   n=n*n
   print(n)
    
dato=int(input('dame el numero a verificar'))
contador=1
divisor=2
Datovalor=True
if dato==1:
    print("el dato es uno y solo es divisible por si mismo y no por ningun otro numero")
else:
    for divisor in range(2,dato) :
        print(contador)
        if dato%divisor==0:
            contador+=1
            if contador>1:
                Datovalor=False
                break
        else :
            divisor+=1               
if Datovalor==False:
    print("el dato no era primo ")        
else :
    print("el numero si es primo") 
