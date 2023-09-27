import banco_dados
import utils

def menu_principal():
    menuPrincipal = """
    Seja bem vindo(a) ao sistema de gerenciamento de carteira de açoes. Selecione uma opçao abaixo:
    1 - Cliente
    2 - Ordem
    3 - Realizar análise da carteira
    4 - Imprimir relatório da carteira
    5 - Sair
    Digite a opçao desejada:
    """
    inputPrinc = int(input(menuPrincipal))
    print("Voce escolheu: ", inputPrinc)
    return inputPrinc



def menu_cliente():
    menuCliente = """
    Menu Cliente
    1 - Cadastrar Cliente
    2 - Alterar Cliente
    3 - Buscar Cliente
    4 - Deletar Cliente
    5 - Listar Clientes
    6 - Voltar ao menu anterior)
    Digite a opçao desejada:
    """
    inputCli = int(input(menuCliente))
    print ("Voce escolheu a opçao: ", inputCli)
    
    if inputCli == 1:
        cadastrar_cliente()
    elif inputCli == 2:
        banco_dados.update_banco_dados()
    elif inputCli == 3:
        cpf = input("Digite o CPF a ser procurado (xxx.xxx.xxx-xx): ")
        try:
            print ("Seu Cliente com cpf ",cpf,":")
            result = banco_dados.select_banco(cpf)
            return
        except:
            print("Não foi possível selecionar esse cpf, erro!")
    elif inputCli == 4:
        cpf = input("Digite o CPF sem pontuação a ser deletado: ")
        try:
            banco_dados.delete_banco_dados(cpf)
            print ("CPF deletado com sucesso!")
            return
        except:
            print("Não foi possível deletar esse cpf, erro!")
    elif inputCli == 5:
        print(lista_cliente)
    elif inputCli == 6:
        return
    return



def cadastrar_cliente():
    print ("Por Favor inclua as informaçoes abaixo:")
    cliente_dicionario = {
        "nome" : input("Nome: "),
        "cpf" : utils.valida_cpf(input ("CPF (xxx.xxx.xxx-xx): ")),
        "rg" : utils.valida_rg(input ("RG (x.xxx.xxx-x): ")),
        "data_nascimento" : utils.valida_data_nascimento(),
        "cep" : utils.buscar_cep(input("CEP: ")),
        "numero_residencia" : int(input("Número da residencia: "))
    }
    cep_final = cliente_dicionario['cep']
    print("\n Suas informaçoes estao corretas? S/N"
          "\n Nome: ", cliente_dicionario['nome'],
          "\n CPF: ", cliente_dicionario['cpf'],
          "\n RG: ", cliente_dicionario['rg'],
          "\n Data de Nascimento: ", cliente_dicionario['data_nascimento'],
          "\n CEP: ", cep_final['CEP'],
          "\n Número da Residencia: ", cliente_dicionario['numero_residencia']
    )
    resp = input()
    respUpper = resp.upper()
    if respUpper == "S":
        try:
            banco_dados.insert_banco_dados(cliente_dicionario['nome'], cliente_dicionario['cpf'], cliente_dicionario['rg'], cliente_dicionario['data_nascimento'], cep_final['CEP'], cliente_dicionario['numero_residencia'])
            print("Cliente inserido com sucesso!")
            return
        except Exception as e:
            print("Não foi possível inserir esse cliente, erro!")
            print(f"Exception: {str(e)}")
    else:
        print ("Voltando para a tela de inicio.")



### Inicio Programa

validador_menu = True
lista_cliente = []
while validador_menu:
    inputPrinc = menu_principal()
    if inputPrinc == 1:
        menu_cliente()
    elif inputPrinc == 2:
        print ("A ser implementado, obrigado!")
    elif inputPrinc == 3:
        print ("A ser implementado, obrigado!")
    elif inputPrinc == 4:
        print ("A ser implementado, obrigado!")
    elif inputPrinc == 5:
        print("Encerrando a execuçao do programa.")
        validador_menu = False
    else:
        print("Opçao incorreta")
