class Carro:
    modelo : str
    marca : str
    cor : str
    __odometro : 0.0
    __tanque: 0.0
    consumo_medio: 0.0
    __motor_on : False


    def __init__(self, modelo : str, marca : str, 
                 cor : str, odometro : float, 
                 tanque: float, consumo_medio: float,
                 motor : bool,):
        
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro 
        self.__tanque = tanque
        self.consumo_medio = consumo_medio
        self.__motor_on = motor
       
    def get_odometro(self):
        return self.__odometro
    
    def get_tanque(self):
        return self.__tanque

    
    def ligar(self):
        if self.__tanque == 0:
            x = float(input("Tanque esgotado, com quantos litros deseja abastecer?: "))
            self.__tanque += x
        else:
            if not self.__motor_on:
                self.__motor_on = True
            else:
                raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        distancia = velocidade * tempo
        litros_necessarios = distancia/ self.consumo_medio
        distancia_possivel = self.__tanque * self.consumo_medio
        if self.__motor_on:
            if litros_necessarios <= self.__tanque:
                self.__tanque -= litros_necessarios
                self.__odometro += distancia
                print(f"Percorreu {distancia} Km. Tanque atual: {self.__tanque:.2f} litros.")
                self.__motor_on = False
            else:
                self.__odometro += distancia_possivel
                self.__motor_on = False
                print(f"Tanque esgotado após percorrer {distancia_possivel:.2f} Km. Odômetro: {self.__odometro:.2f} Km.")
                
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")
        

    def desligar(self):
        if self.__motor_on:
            self.__motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

            
    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__motor_on},'
                f'tanque {self.__tanque}, consumo {self.consumo_medio}')
        return info
    

    def __repr__(self):
        return f"Carro(modelo='{self.modelo}',marca='{self.marca}', cor='{self.cor}', odometro='{self.__odometro}',tanque='{self.__tanque}', consumo_medio='{self.consumo_medio}',motor_on='{self.__motor_on}'"                                               





