from EMR import *

comun=TarjetaComun()
medio=TarjetaMedioBoleto()
c1=Colectivo("Semtur","K",42)
c2=Colectivo("Semtur","192",2342)
t1=Time(2015,9,7,500)
t2=Time(2015,9,7,540)
t3=Time(2015,9,7,541)
t4=Time(2015,9,8,200)
t5=Time(2015,9,8,220)

def test_Saldo(card):
	for i in range(0,10000):
		card._plata=i
		assert i==card.Saldo()

def test_Recarga(card):
	valores=[-100,-1,0,5,10,196,340,368,1000]
	resultados=[0,0,0,5,10,230,340,460,1000]
	for i in range(0,9):
		card._plata=0
		card.Recarga(valores[i])
		assert card.Saldo()==resultados[i]

def test_PagarBoleto(card):
	card._plata=0
	assert card.PagarBoleto(c1,t1)==False
	card._plata=100
	assert card.PagarBoleto(c1,t1)==True
	assert card.Saldo()==100-card.VNormal()
	assert card.PagarBoleto(c1,t1)==True
	assert card.Saldo()==(100-card.VNormal()-card.VNormal())
	assert card.PagarBoleto(c2,t2)==True
	assert card.Saldo()==(100-card.VNormal()-card.VNormal()-card.VTrans())
	assert card.PagarBoleto(c1,t3)==True
	assert card.Saldo()==(100-card.VNormal()-card.VNormal()-card.VTrans()-card.VNormal())
	assert card.PagarBoleto(c2,t3)==True
	assert card.Saldo()==(100-card.VNormal()-card.VNormal()-card.VTrans()-card.VNormal()-card.VNormal())

def test_MedioBoleto(card):
	card._plata=0
	assert card.PagarBoleto(c1,t1)==False
	card._plata=100
	assert card.PagarBoleto(c1,t4)==True
	assert card.Saldo()==100-comun.VNormal()
	assert card.PagarBoleto(c2,t4)==True
	assert card.Saldo()==100-comun.VNormal()-comun.VTrans()
	assert card.PagarBoleto(c1,t5)==True
	assert card.Saldo()==100-comun.VNormal()-comun.VTrans()-comun.VNormal()

def test_ViajesRealizados(card):
	return


test_Saldo(comun)
test_Saldo(medio)
test_Recarga(comun)
test_Recarga(medio)
test_PagarBoleto(comun)
test_PagarBoleto(medio)
test_MedioBoleto(medio)
test_ViajesRealizados(comun)
#test_ViajesRealizados(medio)
