dirRegistroDescargas='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/descargarLIbros/parteFinal/registroDescargas.txt'
datoAños=open(dirRegistroDescargas,'r')
añoXR=datoAños.readline()
añoYR=datoAños.readline()
conteoPaginaR=datoAños.readline()
numeroDescargasR=datoAños.readline()
datoAños.close()
añoX=int(añoXR)
añoY=int(añoYR)
conteoPagina=int(conteoPaginaR)
numeroDescargas=int(numeroDescargasR)
print(añoX,añoY,conteoPaginaR,numeroDescargas)
datoAños=open(dirRegistroDescargas,'w')
datoAños.close()
datoAños=open(dirRegistroDescargas,'r+')
datoAños.write(str(añoX))
datoAños.write(str(añoY))
datoAños.write(str(conteoPaginaR))
datoAños.write(str(numeroDescargasR))
datoAños.close()
