# CLASSES
class Onibus:
    
    def __init__(self,motorista,fiscal,preco,rota,numero):
        self.motorista = motorista
        self.fiscal = fiscal
        self.preco = preco
        self.rota = rota
        self.numero = numero
        
    def criar_onibus(self,Motorista,Fiscal,Preco,Rota,Numero):
        obj_onibus = Onibus(Motorista,Fiscal,Preco,Rota,Numero)
        ls_onibus.append(obj_onibus)
        
    def display(self, obj_onibus):
            print("Motorista   : ", obj_onibus.motorista)
            print("Fiscal : ", obj_onibus.fiscal)
            print("Preco : ", obj_onibus.preco)
            print("Paradas : ", obj_onibus.rota)
            print("\n")
    
    def procurar_onibus(self, numero):
        for i in range(ls_onibus.__len__()):
            if(ls_onibus[i].numero == numero):
                return i
                
    def editar_onibus(self, numero, opcao, mudaca):
        i = obj_onibus.procurar_onibus(numero)
        
        if opcao == "1":
            ls_onibus[i].motorista = mudanca
        elif opcao == "2":
            ls_onibus[i].fiscal = mudanca
            
    def deletar_onibus(self, numero):
        i = obj_onibus.procurar_onibus(numero)
        del ls_onibus[i]

class Motorista:

    def __init__(self,nome):
        self.nome = nome
        
    def criar_motorista(self,Nome):
        obj_motorista = Motorista(Nome)
        ls_motorista.append(obj_motorista)
        
    def display(self, obj_onibus):
            print("Nome   : ", obj_motorista.nome)
            print("\n")
    
    def procurar_motorista(self, nome):
        for i in range(ls_motorista.__len__()):
            if(ls_motorista[i].nome == nome):
                return i
                
    def editar_motorista(self, numero, opcao, mudaca):
        i = obj_motorista.procurar_motorista(nome)
        
        if opcao == "1":
            ls_motorista[i].nome = mudanca
        elif opcao == "2":
            pass
            
    def deletar_motorista(self, nome):
        i = obj_motorista.procurar_motorista(nome)
        del ls_motorista[i] 

class Fiscal:
    
    def __init__(self,nome):
        self.fiscal = nome
        
    def criar_fiscal(self,nome):
        obj_fiscal = Fiscal(Nome)
        ls_fiscal.append(obj_fiscal)
        
    def display(self, obj_fiscal):
            print("Fiscal   : ", obj_fiscal.nome)
            print("\n")
    
    def procurar_fiscal(self, nome):
        for i in range(ls_fiscal.__len__()):
            if(ls_fiscal[i].nome == nome):
                return i
                
    def editar_fiscal(self, nome):
        i = obj_fiscal.procurar_fiscal(nome)
        
        if opcao == "1":
            ls_fiscal[i].motorista = mudanca
        elif opcao == "2":
            ls_fiscal[i].fiscal = mudanca
            
    def deletar_fiscal(self, nome):
        i = obj_fiscal.procurar_fiscal(nome)
        del ls_fiscal[i]

class Parada:
    
    def __init__(self,nome):
        self.nome = nome
        
    def procurar_rota(self, obj_rota):
            print("Rota   : ", obj_rota.rota)
            print("\n")    

class Tarifas:
    
    def __init__(self,onibus_preco):
        self.onibus_preco = onibus_preco
        
    def calcular_tarifa(self,onibus_preco):
        i = len(ls_rota(obj_onibus.rota))
        tarifa_final = i*onibus_preco
        obj_tarifa = Tarifa(onibus_preco)

    
#LISTAS
ls_onibus = []
ls_motorista = []
ls_fiscal = []
ls_rota = []

#CRIA????O DO OBJETO
obj_onibus = Onibus('','',0,'',0)
obj_motorista = Motorista('')
obj_fiscal = Fiscal('')
obj_parada = Parada('')
obj_tarifa = Fiscal('')

#MENUS
menu_type = "main"
secondmenu_type = "0"
thirdmenu_type = "0"

print("Bem vindo ao gerenciador de ??nibus!")

while menu_type == "main":
    menu_type = input("\n1-Onibus\n2-Motorista\n3-Fiscal\n4-Rota\n5-Calcular tarifa.\n0-Sair do Programa\nSelecione uma opcao:")

    if menu_type == "1": #MENU DE ONIBUS
        secondmenu_type = input("\n1-Criar Onibus\n2-Pesquisar Onibus\n0-Retornar ao menu principal\nSelecione uma opcao:")

        if secondmenu_type == "1": #MENU DE CRIA????O DE ONIBUS
            onibus_numero = input("\nInsira o numero do ??nibus: ")
            onibus_motorista = input("\nInsira o motorista do ??nibus: ")
            onibus_fiscal = input("\nInsira o fiscal do ??nibus: ")
            onibus_preco = input("\nInsira a tarifa m??nima do ??nibus: ")
            onibus_rota = input("\nInsira a rota do ??nibus: ")
            obj_onibus.criar_onibus(onibus_motorista,onibus_fiscal,onibus_preco,onibus_rota,onibus_numero)
            print("??nibus criado!")

        elif secondmenu_type == "2": #MENU DE PESQUISA DE ONIBUS
            numero = input("Qual o numero do onibus? ")
            s = obj_onibus.procurar_onibus(numero)
            obj_onibus.display(ls_onibus[s])
            thirdmenu_type = input("1-Editar\n2-Excluir\n0-Retornar ao menu principal\nSelecione uma opcao:")

            if thirdmenu_type == "1": #MENU DE ALTERA????O ##########
                e = input("1-Motorista\n2-Fiscal\n0-Retornar ao menu principal\nQual op????o deseja editar?")

                if e == "1": #MENU DE ALTERA????O DE MOTORISTA
                    mudanca = input("Qual o nome do motorista?")
                    obj_onibus.editar_onibus(numero,e,mudanca)
                    obj_onibus.display(ls_onibus[s])
                elif e == "2": #MENU DE ALTERA????O DE FISCAL
                    mudanca = input("Qual o nome do fiscal? Caso n??o haja, inserir ningu??m")
                    obj_onibus.editar_onibus(numero,e,mudanca)
                    obj_onibus.display(ls_onibus[s])

            elif thirdmenu_type == "2": #MENU DE EXCLUS??O ONIBUS
                verificar_exclusao = input("\nVoc?? deseja excluir o Onibus - %s ?\n1-Sim\n0-N??o"%(numero))
                if verificar_exclusao == "1":
                    obj_onibus.deletar_onibus(numero)
                    print("??nibus deletado!")

                elif verificar_exclusao == "0":
                    menu_type = "main"
            elif thirdmenu_type == "0": ##
                menu_type = "main"
        elif secondmenu_type == "0": ##
            menu_type = "main"
        menu_type = "main"

    elif menu_type == "2": #MENU DE MOTORISTAS
        secondmenu_type = input("\n1-Criar Motorista\n2-Pesquisar Motorista\n0-Retornar ao menu principal\nSelecione uma opcao:")

        if secondmenu_type == "1": #MENU DE CRIA????O DE MOTORISTA
            motorista_nome = input("\nInsira o nome do motorista: ")
            obj_motorista.criar_motorista(motorista_nome)
            print("Motorista criado!")

        elif secondmenu_type == "2": #MENU DE PESQUISA DE MOTORISTA
            nome = input("Qual o nome do motorista? ")
            s = obj_motorista.procurar_motorista(nome)
            obj_motorista.display(ls_motorista[s])
            thirdmenu_type = input("1-Editar\n2-Excluir\n0-Retornar ao menu principal\nSelecione uma opc??o:")

            if thirdmenu_type == "1": #MENU DE ALTERA????O ##########
                e = input("1-Motorista\n0-Retornar ao menu principal\nSelecione uma op????o para editar?")

                if e == "1": #MENU DE ALTERA????O DE MOTORISTA
                    mudanca = input("Qual o nome do motorista?")
                    obj_motorista.editar_motorista(numero,e,mudanca)
                    obj_motorista.display(ls_motorista[s])

            elif thirdmenu_type == "2": #MENU DE EXCLUS??O MOTORISTA
                verificar_exclusao = input("\nVoc?? deseja excluir o motorista %s ?\n1-Sim\n0-N??o"%(numero))
                if verificar_exclusao == "1":
                    obj_motorista.deletar_motorista(nome)
                    print("Motorista deletado.")

                elif verificar_exclusao == "0":
                    menu_type = "main"
            elif thirdmenu_type == "0": ##
                menu_type = "main"
        elif secondmenu_type == "0": ##
            menu_type = "main"
        menu_type = "main"

    elif menu_type == "3": #MENU DE FISCAIS
        secondmenu_type = input("\n1-Criar fiscal\n2-Pesquisar fiscal\n0-Retornar ao menu principal\nSelecione uma opc??o:")

        if secondmenu_type == "1": #MENU DE CRIA????O DE FISCAL
            fiscal_nome = input("\nInsira o nome do fiscal: ")
            obj_fiscal.criar_fiscal(fiscal_nome)
            print("Fiscal criado!")

        elif secondmenu_type == "2": #MENU DE PESQUISA DE FISCAL
            nome = input("Qual o nome do fiscal? ")
            s = obj_fiscal.procurar_fiscal(nome)
            obj_fiscal.display(ls_fiscal[s])
            thirdmenu_type = input("1-Editar\n2-Excluir\n0-Retornar ao menu principal\nSelecione uma opc??o:")

            if thirdmenu_type == "1": #MENU DE ALTERA????O ##########
                e = input("1-Fiscal\n0-Retornar ao menu principal\nQual op????o deseja editar?")

                if e == "1": #MENU DE ALTERA????O DE FISCAL
                    mudanca = input("Qual o nome do fiscal?")
                    obj_fiscal.editar_fiscal(nome,e,mudanca)
                    obj_fiscal.display(ls_fiscal[s])
                
            elif thirdmenu_type == "2": #MENU DE EXCLUS??O FISCAL
                verificar_exclusao = input("\nVoc?? deseja excluir o fiscal %s ?\n1-Sim\n0-N??o"%(nome))
                if verificar_exclusao == "1":
                    obj_fiscal.deletar_fiscal(nome)
                    print("Fiscal deletado.")

                elif verificar_exclusao == "0":
                    menu_type = "main"
            elif thirdmenu_type == "0": ##
                menu_type = "main"
        elif secondmenu_type == "0": ##
            menu_type = "main"
        menu_type = "main"

    elif menu_type == "4": #MENU DE ROTAS
        secondmenu_type = input("\n1-Criar rota\n2-Criar ponto de parada\n3-Pesquisar rota\n0-Retornar ao menu principal\nSelecione uma opc??o:")

        if secondmenu_type == "1": #MENU DE CRIA????O DE ROTA
            rota = input("\nInsira o nome da rota: ")
            ls_rota.append(rota)
            print("Rota criada!")

        elif secondmenu_type == "2": #MENU DE CRIA????O DE PONTOS DE PARADA tentei adicionar uma lista (de paradas) dentro da lista de rotas 
            rota = input("Qual ?? a rota? ")
            s = obj_rota.procurar_rota(rota)
            rota_parada = input("\nInsira o nome do ponto de parada: ")
            ls_rota[s.append(rota_parada)]
            print("Ponto de parada adicionado a rota!")

        elif secondmenu_type == "3": #MENU DE PESQUISA DE ROTA
            rota = input("Qual ?? a rota? ")
            s = obj_rota.procurar_rota(rota)
            obj_rota.display(ls_rota[s])
            thirdmenu_type = input("1-Editar\n2-Excluir\n0-Retornar ao menu principal\nSelecione uma opc??o:")

            if thirdmenu_type == "1": #MENU DE ALTERA????O ##########
                e = input("1-Ponto de Parada\n0-Retornar ao menu principal\nQual op????o deseja editar?")

                if e == "1": #MENU DE ALTERA????O DE ROTA
                    mudanca = input("Qual o nome do ponto de parada?")
                    obj_parada.editar_parada(numero,e,mudanca)
                    obj_parada.display(ls_rota[s])
               
            elif thirdmenu_type == "2": #MENU DE EXCLUS??O DE ROTA
                verificar_exclusao = input("\nVoc?? deseja excluir a rota - %s ?\n1-Sim\n0-N??o"%(Nome))
                if verificar_exclusao == "1":
                    obj_parada.deletar_parada(Nome)
                    print("Rota deletada!")

                elif verificar_exclusao == "0":
                    menu_type = "main"
            elif thirdmenu_type == "0": ##
                menu_type = "main"
        elif secondmenu_type == "0": ##
            menu_type = "main"
        menu_type = "main"

        
        menu_type = "main"
    elif menu_type == "3": #MENU DE TARIFA a ideia era colocar um pre??o constante para cada parada de cada ??nibus, de tal maneira que a tarifa final seria a (constante)*(quantidade de parada)
        obj_tarifa_min.calcular_tarifa(tarifa_min )

        
        menu_type = "main"
    elif menu_type == "2": #FECHAR PROGRAMA
        break