#_saldo:float-> ATRIBUTO PROTEGIDO
#DIagrama de clases de UML
class CuentaBancaria:
    def __init__(self,titular:str,saldo_inicial:float=0)->None:
    #constructor
        self.titular=titular
        self._saldo=saldo_inicial
    def depositar(self,cantidad:float)->None:
        pass
    def get_saldo(self)->float:
        return self._saldo

    @property
    def saldo(self)->float:
        return self._saldo

    def retirar(self,cantidad:float)->None:
        pass
    @saldo.setter
    def saldo(self,nuevo_saldo:float)->None:
        self._saldo=nuevo_saldo

    def __str__(self) -> str:
        return f"(Titular {self.titular}, saldo inicial {self._saldo})"


if __name__ == '__main__':
    cuenta_guadalupe=CuentaBancaria("Guadalupe",0)
    cuenta_guadalupe._saldo=10
    print(cuenta_guadalupe)
    #S
    cuenta_guadalupe.saldo=5
    print(cuenta_guadalupe)