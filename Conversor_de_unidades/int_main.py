import os


def voltar_ao_menu():
    input("\nDigite uma tecla para voltar ao menu de seleção: ")
    main()

def subtitulo(texto):
    os.system("cls")
    print(f"\n{'='*len(texto)}{texto}{'=' * len(texto)}\n")


def limpar_tela():
    os.system("cls")


def Tabela_de_selecao():
    print("Conversor de unidades.")
    print("Selecione o tipo de unidade de grandeza que gostaria converter.")
    print("1 - Comprimento")
    print("2 - Massa")
    print("3 - Volume")
    print("4 - Tempo")
    print("5 - Temperatura")

def unidades_digitadas():

    unidade1 = input("Digite a unidade de medida que deseja converter: ").lower().strip()
    unidade2 = input("Digite a unidade de medida para qual deseja converter: ").lower().strip()
    valor = float(input("Digite o valor que deseja converter: "))
    return unidade1,unidade2,valor



def comprimento():

    subtitulo("Conversor de comprimento.")
    print("Unidades de medida de comprimento:\n")
    print("Quilômetro: km")
    print("Hectômetro : hm ")
    print("Decâmetro: dam ")
    print("Metro: m ")
    print("Decímetro: dm ")
    print("Centímetro: cm ")
    print("Milímetro: mm\n")

    unidade_primaria,unidade_secundaria,valor = unidades_digitadas()

    unidades = {
        "km": 1000,
        "hm": 100,
        "dam": 10,
        "m": 1,
        "dm": 0.1,
        "cm": 0.01,
        "mm": 0.001
    }

    if unidade_primaria in unidades and unidade_secundaria in unidades:
        valor_em_metros = valor * unidades[unidade_primaria]
        valor_convertido = valor_em_metros / unidades[unidade_secundaria]
        print(f"{valor} {unidade_primaria} é igual a {valor_convertido} {unidade_secundaria}.")
    else:
        print("Unidade de medida inválida. Por favor, selecione unidades válidas.")
        input("\nDigite uma tecla para voltar ao menu de seleção: ")
        voltar_ao_menu()

    voltar_ao_menu()

def massa():

    subtitulo("Conversor de massa")
    print("Unidades de medida de massa.\n")
    print("Quilograma: kg")
    print("Hectograma: hg")
    print("Decagrama: dag")
    print("Grama: g")
    print("Decigrama: dg")
    print("Centigrama: cg")
    print("Miligrama: mg\n")
    
    unidade_principal,unidade_para_conversao,valor = unidades_digitadas()

    unidades = {
        "kg": 1000,
        "hg": 100,
        "dag": 10,
        "g": 1,
        "dg": 0.1,
        "cg": 0.01,
        "mg": 0.001
    }

    if unidade_principal in unidades and unidade_para_conversao in unidades:

        valor_real = valor * unidades[unidade_principal]
        valor_convertido = valor_real / unidades[unidade_para_conversao]
        print(f"{valor} {unidade_principal} é igual a {valor_convertido} {unidade_para_conversao}.")
    else:

        print("Unidade de medida inválida. Por favor, selecione unidades válidas.")
        input("\nDigite uma tecla para voltar ao menu de seleção: ")
        voltar_ao_menu()

    voltar_ao_menu()


def temperatura():

    subtitulo("Conversor de temperatura")
    print("celsius (C)")
    print("Kelvin(K)")
    print("Fahrenheit(F)")

    valor1,valor2,valor = unidades_digitadas()
    valor_convertido = 0

    if valor1 == "c" and valor2 == "k":
        valor_convertido = valor + 273
        print(f"A temperatura : {valor} C para kelvin é {valor_convertido:.4f} K")
    elif valor1 == "k" and valor2 == "c":
        valor_convertido = valor - 273
        print(f"A temperatura : {valor} K para celsius é {valor_convertido:.4f} C")
    elif valor1 == "c" and valor2 == "f":
        valor_convertido = ((9*valor)/5) + 32
        print(f"A temperatura : {valor} C para fahrenheit é {valor_convertido:.4f} F")
    elif valor1 == "f" and valor2 == "c":
        valor_convertido = ((5*valor) - 160)/9
        print(f"A temperatura : {valor} F para celsius é {valor_convertido:.4f} C")
    elif valor1 == "k" and valor2 == "f":
        valor_convertido = ((9*valor-2457)/5)+32
        print(f"A temperatura : {valor} K para fahrenheit é {valor_convertido:.4f} F")
    elif valor1 == "f" and valor2 == "k":
        valor_convertido = (((5*valor)-160)/9)+273
        print(f"A temperatura : {valor} F para kelvin é {valor_convertido:.4f} K")
    else:
        print("unidade digitada incorreta!")
        voltar_ao_menu()

    voltar_ao_menu()
    

def tempo():

    subtitulo("Conversor de tempo")
    print("Hora: h")
    print("Minutos: m")
    print("segundos: s")

    tempo1,tempo2,valor = unidades_digitadas()

    if tempo1 == "h" and tempo2 == "m":
        print(f"{valor}H convertido para minutos é {valor*60}m")
    elif tempo1 == "m" and tempo2 == "s":
         print(f"{valor}M convertido para segundos é {valor*60}s")
    elif tempo1 == "h" and tempo2 == "s":
        print(f"{valor}h convertido para segundos é {valor*3600}s")

    elif tempo1 == "s" and tempo2 == "m":
        print(f"{valor}s convertido para minutos é {valor//60}m")
    elif tempo1 == "m" and tempo2 == "h":
        print(f"{valor}m convertido para horas é {valor//60}h")
    elif tempo1 == "s" and tempo2 == "h":
        print(f"{valor}s convertido para horas é {valor//3600}h")
    else:
        voltar_ao_menu()

    voltar_ao_menu()

        

def volume():

    subtitulo("Conversor de volume")
    print("Unidades de medida volume")
    lista_volume = {

        "km":1000**3,
        "hm":1000**2,
        "dam":1000**1,
        "m": 1,
        "dm":1000**-1,
        "cm": 1000**-2,
        "mm": 1000**-3

    }

    for dados in lista_volume.keys():
        print(f"{dados}^3")

    

    volume1,volume2,valor = unidades_digitadas()

    if volume1 in lista_volume and volume2 in lista_volume:
        processo = valor * lista_volume[volume1]
        conversao = processo / lista_volume[volume2]
        print(f"{valor} {volume1} é igual a {conversao} {volume2}.")
    else:

        print("Unidade de medida inválida. Por favor, selecione unidades válidas.")
        input("\nDigite uma tecla para voltar ao menu de seleção: ")
        voltar_ao_menu()




    voltar_ao_menu()





    

    






def selecao():
    
    opcao = int(input("Selecione a conversão que deseja realizar: "))

    match opcao:

        case 1:
            comprimento()
        case 2:
            massa()
        case 3:
            volume()
        case 4:
            tempo()
        case 5: 
            temperatura()
        case _:
            print("Opção inválida. Por favor, selecione uma opção válida.")
            voltar_ao_menu()
            
        
    







def main():
    os.system("cls")
    Tabela_de_selecao()
    selecao()



if __name__ == "__main__":
    main()



