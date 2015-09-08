class Time():
	def __init__(self,year,month,day,time):
		self._year=year
		self._month=month
		self._day=day
		self._time=time #en minutos

	def Diferencia(self,kappa):
		if(self._year>kappa._year or self._month>kappa._month or self._day>kappa._day):
			return 10000
		return abs(self._time-kappa._time)



class Tarjeta():
	def __init__(self):
		raise NotImplementedError("Tarjeta es una clase abstracta....") 

	def PagarBoleto(self, bondi, hora):
		return

	def Recarga(self, monto):
		if(monto<0):
			return

		if(monto==196):
			self._plata+=230

		if(monto==368):
			self._plata+=460

		if(monto!=196 and monto!=368):
			self._plata+=monto

	def Saldo(self):
		return self._plata

	def ViajesRealizados(self):
		return self._viajesRealizados

class TarjetaComun(Tarjeta):
	def __init__(self):
		self._plata=0
		self._viajesRealizados=[None]*10
		self._ultimoTransbordo=Time(0,0,0,0)
		self._indexViajes=0
		self._viajesRealizados[0]=Viaje(Colectivo("Nada","nada",-1),Time(0,0,0,0),0)

	def VNormal(self):
		return 5.75

	def VTrans(self):
		return 2.90

	def PagarBoleto(self,bondi,hora):
		monto=0
		if(bondi.Linea() != (self._viajesRealizados[self._indexViajes].Colectivo()).Linea() ):
			if(hora.Diferencia( self._viajesRealizados[self._indexViajes].Horario() ) <= 60 ):
				if(hora.Diferencia( self._ultimoTransbordo ) >= 60):
					monto=self.VTrans()

		if(monto==0):
			monto=self.VNormal()

		if(self._plata<monto):
			return False

		else:
			self._plata-=monto
			viajeActual=Viaje(bondi,hora,monto)
			if(monto==self.VTrans()):
				self._ultimoTransbordo=hora
			self._indexViajes=(self._indexViajes+1)%10
			self._viajesRealizados[self._indexViajes]=viajeActual
			return True



class TarjetaMedioBoleto(TarjetaComun):

	def VNormal(self):
		return super().VNormal()/2

	def VTrans(self):
		return super().VTrans()/2

	def PagarBoleto(self,bondi,hora):
		if(hora._time<360):
			monto=0
			if(bondi.Linea() != (self._viajesRealizados[self._indexViajes].Colectivo()).Linea() ):
				if(hora.Diferencia( self._viajesRealizados[self._indexViajes].Horario() ) <= 60 ):
					if(hora.Diferencia( self._ultimoTransbordo ) >= 60):
						monto=super().VTrans()
	
			if(monto==0):
				monto=super().VNormal()
	
			if(self._plata<monto):
				return False
	
			else:
				self._plata-=monto
				viajeActual=Viaje(bondi,hora,monto)
				if(monto==super().VTrans()):
					self._ultimoTransbordo=hora
				self._indexViajes=(self._indexViajes+1)%10
				self._viajesRealizados[self._indexViajes]=viajeActual
				return True
		
		else:
			return super().PagarBoleto(bondi,hora)


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
	def __init__(self,bondi,hora,monto):
		self._colectivo=bondi
		self._horario=hora
		self._monto=monto

	def Horario(self):
		return self._horario

	def Colectivo(self):
		return self._colectivo

	def Monto(self):
		return self._monto
