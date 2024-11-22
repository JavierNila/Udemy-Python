class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} \n Numero de cuenta: {self.numero_cuenta} \n Balance: ${self.balance}"

    def depositar(self,deposito):
        self.balance += deposito
        print(f"Deposito realizado")

    def retirar(self,retiro):
        if self.balance >= retiro:
            self.balance -= retiro
            print(f"Retiro realizado")
        else:
            print("No cuenta con saldo suficiente para retirar")


def crear_cliente():
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        num_cta = input("Ingrese su numero de cuenta: ")
        mi_cliente = Cliente(nombre,apellido,num_cta)
        return mi_cliente


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    operacion = 0

    while operacion != 'salir':
        operacion = input("Indique su operacion: ")
        if operacion == 'deposito':
            monto_deposito = int(input("Cuanto desea depositar: "))
            mi_cliente.depositar(monto_deposito)

        elif operacion == 'retiro':
            monto_retiro = int(input("Cuanto desea retirar: "))
            mi_cliente.retirar(monto_retiro)
        print(mi_cliente)
    print("Operacion finalizada, vuelva pronto")


inicio()