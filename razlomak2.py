class Razlomak(object):
    '''Klasa razlomak'''
    
    def __init__(self, brojnik, nazivnik = 1):
        if nazivnik == 0: raise Exception('Nazivnik ne moze biti 0')
        self._brojnik = brojnik
        self._nazivnik = nazivnik
    def __str__(self):
        return '%d|%d' % (self._brojnik, self._nazivnik)
    
    @staticmethod
    def inverz():
        return '%d|%d' % (Razlomak.borjnik, Razlomak.nazivnik)
    

   
   
r1=Razlomak(314,100)
print(r1)
r2=Razlomak.inverz(r1)

