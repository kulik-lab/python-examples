""" modul kolo_st: zawiera klase kolo, demonstruje medody statyczne"""

class Kolo:
    """Klasa Kolo"""
    wszystkie_kola=[]
    pi=3.1415

    def __init__(self, r=1):
        """tworzy kolo o podanym promieniu"""
        self.promien = r
        #instancja dolacza do listy 'wszystie_kola'
        self.__class__.wszystkie_kola.append(self)
    def pole(self):
        """ oblicza pole kola"""
        return self.__class__.pi * self.promien * self.promien

    @staticmethod
    def suma_pol():
        """ statyczna metoda obliczenia sumy pol wszystkich kol"""
        suma = 0
        for k in Kolo.wszystkie_kola:
            suma=suma+k.pole()
        return suma
    
    
