import pyodbc
import utils

def retornar_cursor_banco_dados():
  connection = pyodbc.connect(retorna_conexao_banco_dados())
  cursor = connection.cursor()
  return cursor, connection

def retorna_conexao_banco_dados():
  return(
    "DRIVER={SQL Server};"
    "SERVER=HOESQL633;"
    "DATABASE=Skillup_GGTREME;"
    "UID=SA\GGTREME;"
    "Trusted_Connection=Yes;"
  )

def select_banco(cpf):
  cursor, connection = retornar_cursor_banco_dados()
  select_query = "select * from cliente where cpf = '" + cpf + "';"
  cursor.execute(select_query)
  clientes = cursor.fetchall()
  print(clientes)
  connection.commit()

def insert_banco_dados(nome, cpf, rg, data_nascimento, cep, numero_residencia):
  cursor, connection = retornar_cursor_banco_dados()
  insert_query = """
  INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, numero_residencia)
  VALUES (?, ?, ?, ?, ?, ?);
  """
  #values = (cliente['nome'], cliente['cpf'], cliente['rg'], cliente['data_nascimento'], cliente['cep'], cliente['numero_residencia'])
  values = (nome, cpf, rg, data_nascimento, cep, numero_residencia)
  cursor.execute(insert_query, values)
  connection.commit()


def delete_banco_dados(cpf):
  cursor, connection = retornar_cursor_banco_dados()
  delete_query = "DELETE FROM cliente WHERE cpf = '" + cpf + "';"
  cursor.execute(delete_query)
  connection.commit()


def update_banco_dados():
  cursor, connection = retornar_cursor_banco_dados()
  cpf = utils.valida_cpf(input("Digite o CPF do Cliente a ser alterado: "))

  menuUpdate = """
    Qual informação será alterada?
    1 - Nome Cliente
    2 - RG Cliente
    3 - Data Nascimento Cliente
    4 - CEP Cliente
    5 - Número da Residencia Cliente
    6 - Voltar ao menu anterior)
    Digite a opçao desejada:
    """
  try:
    inputCli = int(input(menuUpdate))

    if inputCli == 1:
      nome = input("Nome atualizado: ")
      update_query = ("UPDATE cliente  SET nome = '" + nome + "'  WHERE cpf = '" + cpf + "';")
      cursor.execute(update_query)
      connection.commit()
      print("Valor Atualizado.")
    elif inputCli == 2:
      rg = utils.valida_rg(input("RG atualizado: "))
      update_query = ("UPDATE cliente  SET rg = '" + rg + "'  WHERE cpf = '" + cpf + "';")
      cursor.execute(update_query)
      connection.commit()
      print("Valor Atualizado.")
    elif inputCli == 3:
      data_nascimento = utils.valida_data_nascimento()
      update_query = ("UPDATE cliente  SET data_nascimento = '" + data_nascimento + "'  WHERE cpf = '" + cpf + "';")
      cursor.execute(update_query)
      connection.commit()
      print("Valor Atualizado.")
    elif inputCli == 4:
      cep = utils.buscar_cep(input("CEP atualizado: "))
      update_query = "UPDATE cliente  SET cep = '" + cep['CEP'] + "'  WHERE cpf = '" + cpf + "';"
      cursor.execute(update_query)
      connection.commit()
      print("Valor Atualizado para "+ cep['Logradouro']+ ".")
    elif inputCli == 5:
      numero_residencia = input("Número da residencia atualizado: ")
      update_query = ("UPDATE cliente  SET numero_residencia = " + numero_residencia + "  WHERE cpf = '" + cpf + "';")
      cursor.execute(update_query)
      connection.commit()
      print("Valor Atualizado.")
    elif inputCli == 6:
      return
    else:
          print("Opçao incorreta")
  except Exception as e:
            print("Não foi possível atualizar esse cliente, erro!")
            print(f"Exception: {str(e)}")

update_banco_dados()