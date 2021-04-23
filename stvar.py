class Stvar(object):

        stvari=set()
        def __init__(self,stvar):
            self.stvar=stvar
            Stvar.stvari.add(stvar)
        @staticmethod
        def __del__(self,stvar):
            Stvar.stvari.remove(stvar) 
        @staticmethod
        def broj_stvari():
            return len(Stvar.stvari)
        
            
        
s1=Stvar("Stolica")
s2=Stvar("Klupa")
print(Stvar.broj_stvari())        
s3=s2
print(Stvar.broj_stvari())  
