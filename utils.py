from datetime import datetime
import requests
from validate_docbr import CPF
import re


def valida_cpf(cpf_digitado):
  cpf = CPF()

  while True:

    cpf_digitado = re.sub('[-.]', '',cpf_digitado)

    resultado = cpf.validate(cpf_digitado)
    if resultado:
      cpf_formatado = f"{cpf_digitado[:3]}.{cpf_digitado[3:6]}.{cpf_digitado[6:9]}-{cpf_digitado[9:]}"
      return cpf_formatado
    else:
      cpf_digitado = input("CPF inválido. Digite novamente: ")



def valida_rg(rg_input):
  
  # RG: 11.111.111.-x
  # RG nao valido: 11.111.11x-x
  padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'

  while True:

    rg_input = re.sub('[-.]','', rg_input)

    rg_input = f'{rg_input[:2]}.{rg_input[2:5]}.{rg_input[5:8]}-{rg_input[8:]}'

    if re.match(padrao_rg, rg_input):
      return rg_input
    else:
      rg_input = input("RG inválido. Digite novamente: ")



def valida_data_nascimento():

# enquanto -> condicao -> verdadeira
  while True:

    data_nascimento_input = input("Digite a data de nascimento (MM-DD-YYYY): ")
    try:
      data_convertida = datetime.strptime(data_nascimento_input, '%m-%d-%Y').date()
      data_atual = datetime.now().date()
      

      if data_convertida < data_atual:
        return data_convertida.strftime("%m-%d-%Y")
        #26/08/1972
    
      else:
        print("Data inválida. A sua data de nascimento deve ser menor que a data atual ")
    
    except ValueError as e:
      print("Formato de data inválido. Você recebeu o erro: ", e, ". Tente novamente.")



def buscar_cep(cep_input):
    url = f'https://viacep.com.br/ws/{cep_input}/json/'

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()

        endereco = {
            "CEP": data['cep'],
            "Logradouro": data['logradouro'],
            "Bairro": data['bairro'],
            "Cidade": data['localidade'],
            "Estado": data['uf'],
        }
        return endereco
