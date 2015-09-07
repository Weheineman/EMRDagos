from EMR import *

visa=TarjetaComun()
master=TarjetaMedioBoleto()
trole=Colectivo("Semtur","K",42)
trolo=Colectivo("Semtur","192",2342)
ahora=Time(2015,9,7,420)
desp=Time(2015,9,7,540)
visa.Recarga(196)
if (visa.PagarBoleto(trole,ahora)):
	print("Sos un gato")
print(visa.Saldo())	
if (visa.PagarBoleto(trolo,ahora)):
	print("Sos un gato")

print(visa.Saldo())
