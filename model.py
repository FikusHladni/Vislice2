STEVILO_DOVOLJENIH-_NAPAK = 10
PRAVILNA_CRKA ="+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"

ZMAGA = "w"
PORAZ = "l"

#kons z velikimi
#razred s katerim opišemo stanje igre
class Igra:
    def __init__(self,geslo,crke=[]):
        self.geslo = geslo
        self.crke = crke

    def pravilne_crke(self):
        return[crka for crka in self.crke if crka in self.geslo]

    def napacne_crke(self):
        return[crka for crka in self.crke if crka not  in self.geslo]
    
    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for i in self.geslo:
            if i not in pravilne_crke:
                return False
        return True
    
    def poraz(self):
        return( self.stevilo_napak > STEVILO_DOVOLJENIH_NAPAK)

    def pravilni_del_gesla(self):
        izpis = ""
        for crka in self.geslo:
            if crka in pravilne_crke:
                izpis+= i
            else:
                izpis += "_"
        return seznam

    def nepravilni_ugibi(self):
         return " ".join(self.napacne_crke)   

    def ugibaj(self,crka):
        crka = crka.upper()
        if crka in self.crke
            return PONOVLJENA_CRKA
        self.crke.append(crka)
        if self.zmaga():
            return ZMAGA
        if self.poraz():
            return PORAZ
        else:
            if crka in self.pravilne_crke():
                return PRAVILNA_CRKA
            if crka in self.napacne_crke():
                return NAPACNA_CRKA
                


    

