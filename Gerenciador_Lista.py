class Tela:
    def __init__(self, polegadas, tipo):
        self.polegadas=polegadas
        self.tipo=tipo

    def __str__(self):
        return f"{self.polegadas} polegadas , tipo: {self.tipo}"
        
class Celulares:
    def __init__(self,marca, modelo, versao,preco, tela: Tela):
        self.marca=marca
        self.versao=versao
        self.modelo=modelo
        self.preco=preco
        self.tela=tela

    def __str__(self):
        return f"{self.marca} {self.modelo} Versao {self.versao} Preco:{self.preco:.2f}MZN | tela:{self.tela}"
    
class Gerenciaar:
    def __init__(self):
        self.lista=[]

    def cadastrar(self):
        marca=input("Digite a marca do celular:")
        modelo=input("Digite o modelo:")
        versao=float(input("Digite a versao do Celular: "))
        preco=float(input("Digite o preco do celular: "))
        polegadas=float(input("Digite o tamanho da tela: "))
        tipo=input("Digite o tipo de tela: ")

        tela=Tela(polegadas , tipo)
        celular=Celulares(marca,modelo,versao,preco,tela)
        self.lista.append(celular)

        print("\n Celular cadastrado com sucesso......")

    def listar_cell(self):
        if not self.lista:
            print("\n Nenhum celular cadastrado......")
            return
        for i , celular in enumerate(self.lista, start=1):
            print(f"{i}. {celular}")
        print()
    def eliminar_celular(self):
        if not self.lista:
            print("Nenhum celular para eliminar")
            return 
        self.listar_cell()
        indice=int(input("Digite o numero do celular que deseja eliminar: "))
        if 1<=indice <=len(self.lista):
            removido=self.lista.pop(indice-1)
            print(f"\nCelular '{removido.marca} {removido.modelo}' removido com sucesso")
        else:
            print("\n Numero invalido..")

def menu():
    Gerenciaar_cell=Gerenciaar()

    while True:
        print ("++MENU++")
        print("1.Cadastrar celular ")
        print("2.Listar celular")
        print("3.Eliminar celular")
        print("4.Sair")

        op=input("Escoljha a opcao: ")

        if op=="1":
            Gerenciaar_cell.cadastrar()
        elif op=="2":
            Gerenciaar_cell.listar_cell()
        elif op=="3":
            Gerenciaar_cell.eliminar_celular()
        elif op=="4":
            print("saindo....")
            break
        else:
            print("Escolha Invalida....\n")

if  __name__=="__main__":
    menu()
