print('Bem vindo ao Programa de limpeza do Renan Azevedo')


# função metragem da limpeza

def metragem_limpeza():
    metragem_str = input("Qual a metragem da porção a ser limpa? ")

    try:

        metragem = int(metragem_str)

        if metragem >= 30 or metragem < 700:
            print('Não aceitamos casas menores que 30m² ou maiores que 700m²')
            metragem_limpeza()

        elif metragem > 30 or metragem < 300:
            valor_metragem = 60 + 0.3 * metragem
            print (valor_metragem)

        else:
            metragem >= 300 or metragem <= 700
            valor_metragem = 120 + 0.5 * metragem
            print (valor_metragem)

    finally:
        print('erro')



# função tipo de limpeza

def tipo_limpeza():
    tipo = input("Qual o tipo de limpeza será feita? Digite B para básica e C para completa. ")

    if tipo == "B":

        multiplicador = 1.00

    elif tipo == "C":

        multiplicador = 1.30

    else:

        tipo_limpeza()

    return multiplicador


# função adicional da limpeza

def adicional_limpeza():
    aux = 0

    print(tipos_adicional)

    while True:

        adicional = input("Digite o número do adicional que deseja. ")

        if int(adicional) == 0:

            break

        elif (adicional) in tipos_adicional:

            aux = aux + valor_adicional[int(adicional)]

        else:

            continue

    return aux


# tabela adicionais

tipos_adicional = {0: "Sem adicionais",

                   1: "Passar 10 peças de roupa",

                   2: "Limpeza de Forno/Microondas",

                   3: "Limpeza de Freezer/Geladeira"}

valor_adicional = [0, 10.00, 12.00, 20.00]

# programa

valor = metragem_limpeza()

tipo_limpeza = tipo_limpeza()

adicionais = adicional_limpeza()

total = (valor * tipo_limpeza) + adicionais

print(f"R$ {total:,.2f}")


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
