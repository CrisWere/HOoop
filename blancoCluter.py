import blanco


class Blancocluter(blanco.Blanco):
    """
    Define un Blancocluter a ser detectado por un radar

    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        #TODO: completar con la inicializacion de los parametros del objeto
#	blanco.Blanco.__init__(amplitud*10, tiempo_inicial, tiempo_final)
        self.amplitud = amplitud*10
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

        pass

    def reflejar(self, senal, tiempo_inicial, tiempo_final):

        #TODO ver como se encajan los timepos del blanco y del intervalo de tiempo
        # senal.insert(self.instante, senal[instante]+self.amplitud)
        # modificar la senal conlos parametros del blanco

        
        #Amplifico toda la senal
        ret = [x*self.amplitud for x in senal]      
	return ret
	#pass
