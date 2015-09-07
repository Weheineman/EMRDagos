class Tarjeta():
	def __init__(self):
		raise NotImplementedError("Tarjeta es una clase abstracta....") 

	def PagarBoleto(self, viaje):
		return

	def Recarga(self, monto):
		if(monto==196):
			self._plata+=230

		if(monto==368):
			self._plata+=460

		if(monto!=196 and monto!=368):
			self._plata+=monto

	def Saldo(self):
		return self._plata

	def ViajesRealizados(self):
		return

class TarjetaComun(Tarjeta):
	def __init__(self):
		self._viajeNormal=5.75
		self._transbordo=1.90
		self._plata=0

class TarjetaMedioBoleto(Tarjeta):
	def __init__(self):
		self._viajeNormal=2.90
		self._transbordo=0.96
		self._plata=0

class Colectivo():
	def __init__(self,empresa,linea,interno):
		self._empresa=empresa
		self._linea=linea
		self._interno=interno

	def Empresa(self):
		return self._empresa

	def Linea(self):
		return self._linea

	def Interno(self):
		return self._interno

class Viaje():
	def __init__(self):
		return
