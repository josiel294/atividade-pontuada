import os
import csv
from dataclasses import dataclass

os.system("cls||clear")

@dataclass # Nomear a classe que está sendo utilizada 
class Funcionario:
    nome: str 
    cpf: str
    cargo: str
    salario: str

    def mostrar_dados(self): # Aparecer os dados informado na tela
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: {self.salario}")
        print()

def exibir_menu(): # Exibir as opções disponíveis
    print("\n--- Dendê Tech - Cadastro de funcionários ---")
    print("1. Cadastrar Funcionário")
    print("2. Listar Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Excluir Funcionário")
    print("5. Salvar Dados em CSV")
    print("6. Carregar Dados do CSV")
    print("7. Sair")
    print("-------------------------------------------------")

def verificar_lista_vazia(lista): #Lista vazia para adicionar os dados
    if not lista:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar(lista): # Para adicionar o funcionário na lista
    print("= Digite os dados do funcionário = ")
    funcionario = Funcionario(
        nome=input("Nome: "),
        cpf=input("CPF: "),
        cargo=input("Cargo: "),
        salario=input("Salário: ")
    )
    lista.append(funcionario)
    print("Funcionário adicionado com sucesso. ✅")

def mostrar_funcionarios(lista): # Dados salvo do funcionario na lista
    if verificar_lista_vazia(lista):
        return
    print("\n= Lista de funcionários =")
    for funcionario in lista:
        funcionario.mostrar_dados()

def atualizar(lista): # Atualizar os dados dos funcionário 
    if verificar_lista_vazia(lista):
        return

    nome_atualizar = input("Digite o nome do funcionário que deseja atualizar: ")
    encontrado = False

    for funcionario in lista:
        if funcionario.nome == nome_atualizar:
            print("= Digite os novos dados do funcionário = ")
            funcionario.nome = input("Nome: ")
            funcionario.cpf = input("CPF: ")
            funcionario.cargo = input("Cargo: ")
            funcionario.salario = input("Salário: ")
            print("Funcionário atualizado com sucesso. ✅")
            encontrado = True
            break

    if not encontrado:
        print(f"\nO funcionário com o nome '{nome_atualizar}' não foi encontrado.")

def excluir(lista): # Para excluir o dados salvo
    if verificar_lista_vazia(lista):
        return

    nome_excluir = input("Digite o nome do funcionário a ser excluído: ")
    for funcionario in lista:
        if funcionario.nome == nome_excluir:
            lista.remove(funcionario)
            print("Funcionário excluído com sucesso. ✅")
            return
    print("Funcionário não encontrado.")

def salvar_dados_csv(lista, nome_arquivo="funcionarios.csv"): # Salvar dados no arquivo 
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(['Nome', 'CPF', 'Cargo', 'Salario'])
            for funcionario in lista:
                writer.writerow([funcionario.nome, funcionario.cpf, funcionario.cargo, funcionario.salario])
        print(f"✅ Dados salvos com sucesso em '{nome_arquivo}'.")
    except IOError:
        print(f"❌ Erro ao salvar o arquivo '{nome_arquivo}'.")

def carregar_dados_csv(lista, nome_arquivo="funcionarios.csv"): # Carregar os dados ja salvo
    lista.clear()
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            reader = csv.reader(arquivo_csv)
            header = next(reader)
            if header != ['Nome', 'CPF', 'Cargo', 'Salario']:
                print(f"⚠️ Cabeçalho inesperado. Tentando carregar mesmo assim.")
            for row in reader:
                try:
                    if len(row) == 4:
                        funcionario = Funcionario(nome=row[0], cpf=row[1], cargo=row[2], salario=row[3])
                        lista.append(funcionario)
                    else:
                        print(f"⚠️ Linha inválida ignorada: {row}")
                except ValueError:
                    print(f"⚠️ Erro ao converter salário na linha: {row}")
        print(f"✅ Dados carregados com sucesso de '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"❌ O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"❌ Erro ao carregar o arquivo: {e}")

# Execução principal
lista_funcionarios = []

while True: # Lista com as opções o que o usúario quer escolher
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar(lista_funcionarios)
    elif opcao == '2':
        mostrar_funcionarios(lista_funcionarios)
    elif opcao == '3':
        atualizar(lista_funcionarios)
    elif opcao == '4':
        excluir(lista_funcionarios)
    elif opcao == '5':
        salvar_dados_csv(lista_funcionarios)
    elif opcao == '6':
        carregar_dados_csv(lista_funcionarios)
    elif opcao == '7':
        print("Saindo... 👋")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1-7).")
