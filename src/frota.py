class Carro:
    modelo : str
    marca : str
    cor : str
    odometro : 0.0
    tanque: 0.0
    consumo_medio: 0.0
    motor_on : False


    def __init__(self, modelo : str, marca : str, 
                 cor : str, odometro : float, 
                 tanque: float, consumo_medio: float,
                 motor : bool,):
        
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.odometro = odometro 
        self.tanque = tanque
        self.consumo_medio = consumo_medio
        self.motor_on = motor
       

    def ligar(self):
        if self.tanque == 0:
            x = float(input("Tanque esgotado, com quantos litros deseja abastecer?: "))
            self.tanque += x
        else:
            if not self.motor_on:
                self.motor_on = True
            else:
                raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        distancia = velocidade * tempo
        if self.motor_on:
            litros_necessarios = distancia/ self.consumo_medio
            distancia_possivel = self.tanque * self.consumo_medio
        
            if litros_necessarios <= self.tanque:
                self.tanque -= litros_necessarios
                self.odometro += distancia_possivel
                print(f"Percorreu {distancia} Km. Tanque atual: {self.tanque:.2f} litros.")
                self.motor_on = False
            else:
                self.odometro += distancia_possivel
                self.tanque = 0
                self.motor_on = False
                print(f"Tanque esgotado após percorrer {distancia_possivel:.2f} Km. Odômetro: {self.odometro:.2f} Km.")
                
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")
        

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")
    
    def reabastecer(self, litros: float):
        self.tanque += litros
        self.motor_on = True
        print(f"Reabastecido com {litros} litros. Tanque atual: {self.tanque:.2f} litros.")

            
    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.odometro} Km, '
                f'motor {self.motor_on},'
                f'tanque {self.tanque},')
        return info





