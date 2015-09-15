from EMR import *

def test_Saldo():
	comun=TarjetaComun()
	medio=TarjetaMedioBoleto()
	c1=Colectivo("Semtur","K",42)
	c2=Colectivo("Semtur","192",2342)
	t1=Time(2015,9,7,500)
	t2=Time(2015,9,7,540)
	t3=Time(2015,9,7,541)
	t4=Time(2015,9,8,200)
	t5=Time(2015,9,8,220)
	for i in range(0,10000):
		comun._plata=i
		assert i==comun.Saldo()

	for i in range(0,10000):
		medio._plata=i
		assert i==medio.Saldo()


def test_Recarga():
	comun=TarjetaComun()
	medio=TarjetaMedioBoleto()
	c1=Colectivo("Semtur","K",42)
	c2=Colectivo("Semtur","192",2342)
	t1=Time(2015,9,7,500)
	t2=Time(2015,9,7,540)
	t3=Time(2015,9,7,541)
	t4=Time(2015,9,8,200)
	t5=Time(2015,9,8,220)
	valores=[-100,-1,0,5,10,196,340,368,1000]
	resultados=[0,0,0,5,10,230,340,460,1000]
	for i in range(0,9):
		comun._plata=0
		comun.Recarga(valores[i])
		assert comun.Saldo()==resultados[i]

	for i in range(0,9):
		medio._plata=0
		medio.Recarga(valores[i])
		assert medio.Saldo()==resultados[i]	

def test_PagarBoleto():
	comun=TarjetaComun()
	medio=TarjetaMedioBoleto()
	c1=Colectivo("Semtur","K",42)
	c2=Colectivo("Semtur","192",2342)
	t1=Time(2015,9,7,500)
	t2=Time(2015,9,7,540)
	t3=Time(2015,9,7,541)
	t4=Time(2015,9,8,200)
	t5=Time(2015,9,8,220)
	comun._plata=0
	assert comun.PagarBoleto(c1,t1)==False
	comun._plata=100
	assert comun.PagarBoleto(c1,t1)==True
	assert comun.Saldo()==100-comun.VNormal()
	assert comun.PagarBoleto(c1,t1)==True
	assert comun.Saldo()==(100-comun.VNormal()-comun.VNormal())
	assert comun.PagarBoleto(c2,t2)==True
	assert comun.Saldo()==(100-comun.VNormal()-comun.VNormal()-comun.VTrans())
	assert comun.PagarBoleto(c1,t3)==True
	assert comun.Saldo()==(100-comun.VNormal()-comun.VNormal()-comun.VTrans()-comun.VNormal())
	assert comun.PagarBoleto(c2,t3)==True
	assert comun.Saldo()==(100-comun.VNormal()-comun.VNormal()-comun.VTrans()-comun.VNormal()-comun.VNormal())

	medio._plata=0
	assert medio.PagarBoleto(c1,t1)==False
	medio._plata=100
	assert medio.PagarBoleto(c1,t1)==True
	assert medio.Saldo()==100-medio.VNormal()
	assert medio.PagarBoleto(c1,t1)==True
	assert medio.Saldo()==(100-medio.VNormal()-medio.VNormal())
	assert medio.PagarBoleto(c2,t2)==True
	assert medio.Saldo()==(100-medio.VNormal()-medio.VNormal()-medio.VTrans())
	assert medio.PagarBoleto(c1,t3)==True
	assert medio.Saldo()==(100-medio.VNormal()-medio.VNormal()-medio.VTrans()-medio.VNormal())
	assert medio.PagarBoleto(c2,t3)==True
	assert medio.Saldo()==(100-medio.VNormal()-medio.VNormal()-medio.VTrans()-medio.VNormal()-medio.VNormal())

def test_MedioBoleto():
	comun=TarjetaComun()
	medio=TarjetaMedioBoleto()
	c1=Colectivo("Semtur","K",42)
	c2=Colectivo("Semtur","192",2342)
	t1=Time(2015,9,7,500)
	t2=Time(2015,9,7,540)
	t3=Time(2015,9,7,541)
	t4=Time(2015,9,8,200)
	t5=Time(2015,9,8,220)
	medio._plata=0
	assert medio.PagarBoleto(c1,t1)==False
	medio._plata=100
	assert medio.PagarBoleto(c1,t4)==True
	assert medio.Saldo()==100-comun.VNormal()
	assert medio.PagarBoleto(c2,t4)==True
	assert medio.Saldo()==100-comun.VNormal()-comun.VTrans()
	assert medio.PagarBoleto(c1,t5)==True
	assert medio.Saldo()==100-comun.VNormal()-comun.VTrans()-comun.VNormal()

def test_ViajesRealizados():
	comun=TarjetaComun()
	medio=TarjetaMedioBoleto()
	c1=Colectivo("Semtur","K",42)
	c2=Colectivo("Semtur","192",2342)
	t1=Time(2015,9,7,500)
	t2=Time(2015,9,7,540)
	t3=Time(2015,9,7,541)
	t4=Time(2015,9,8,200)
	t5=Time(2015,9,8,220)
	card.Recarga(100)
	card.PagarBoleto(c1,t1)
	lista=card.ViajesRealizados()
	assert lista[card._indexViajes].Horario()==t1
	assert lista[card._indexViajes].Colectivo()==t1
	assert lista[card._indexViajes].Monto()==t1


test_Saldo(comun)
test_Saldo(medio)
test_Recarga(comun)
test_Recarga(medio)
test_PagarBoleto(comun,c1,c2,t1,t2,t3,t4,t5)
test_PagarBoleto(medio,c1,c2,t1,t2,t3,t4,t5)
test_MedioBoleto(medio,c1,c2,t1,t2,t3,t4,t5)
#test_ViajesRealizados(com,c1,c2,t1,t2,t3,t4,t5)
#test_ViajesRealizados(med,c1,c2,t1,t2,t3,t4,t5)
