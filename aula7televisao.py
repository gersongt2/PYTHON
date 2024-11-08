class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1

    def Power(self):
        
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    
    def aumentacanal(self):
        self.canal += 1 

    def diminuicanal(self):
        self.canal -= 1 

if __name__ == '__main__':
    televisao = Televisao()
    print("Televisao esta ligada: {}".format(televisao.ligada))
    televisao.Power()
    print("Televisao esta ligada: {}".format(televisao.ligada))
    televisao.Power()
    print("Televisao esta ligada: {}".format(televisao.ligada))
    televisao.Power()
    print("Canal: {}".format(televisao.canal))
    televisao.aumentacanal()
    televisao.aumentacanal()
    televisao.aumentacanal()
    televisao.aumentacanal()
    print("Canal: {}".format(televisao.canal))
    televisao.diminuicanal()
    televisao.diminuicanal()
    print("Canal: {}".format(televisao.canal))
   
