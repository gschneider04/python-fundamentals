# ESTUDO DE CLASSES E OBJETOS EM PYTHON
# APRENDENDO A CRIAR CLASSES E OBJETOS EM PYTHON
# ENTENDO O CONCEITO DE CLASSES E OBJETOS EM PYTHON

class Bikes:
    def __init__(self, color, model, year, price):
        self.color = color
        self.model = model
        self.year = year
        self.price = price

    def bike_info(self):
        return f"Bike Model: {self.model}, Color: {self.color}, Year: {self.year}, Price: ${self.price}"
    
    def bike_Biped(self):
        print ('BEEEEEEEEEEEEEEEEEEEEEEP')
    
    def bikeRun(self):
        print('Vrummmmm')
        print ('Bike is running')

    def bikeStop(self):
        print('Brakeeeeeeeeeeeeee')
        print ('Bike is stopped')

bike1 = Bikes("Red", "Mountain", 2022, 1500)
bike2 = Bikes("Blue", "Road", 2021, 1200)

bike1.bikeRun()
bike1.bike_Biped()
bike1.bikeStop()
bike1.bikeRun()



#FUNCIONALIDADE PARA EXIBIR INFORMAÇÕES DA CLASSE
#ESSA FUNCIONALIDADE É MUITO ÚTIL PARA VERIFICAR SE AS INFORMAÇÕES ESTÃO CORRETAS
#ESTA FUNCIONALIDADE É BASEADA EM CLEAN CODE, POIS PODEMOS VER OS ITEMS DA NOSSA CLASSE_
#_E MESMO SE MODIFICARMOS A CLASSE AINDA TEREMOS UMA ATUALIZAÇÃO AUTOMÁTICA

class Bikes:
    def __init__(self, color, model, year, price):
        self.color = color
        self.model = model
        self.year = year
        self.price = price

    def bike_info(self):
        return f"Bike Model: {self.model}, Color: {self.color}, Year: {self.year}, Price: ${self.price}"
    
    def bike_Biped(self):
        print ('BEEEEEEEEEEEEEEEEEEEEEEP')
    
#ATÉ AQUI SEGUE O CÓDIGO ORIGINAL

#A PARTIR DAQUI É O CÓDIGO MODIFICADO PARA EXIBIR AS INFORMAÇÕES DA CLASSE
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"
print('exec')
