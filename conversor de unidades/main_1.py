import os


def voltar_ao_menu():
    """
    Aguarda o usuário pressionar uma tecla e retorna ao menu principal.

    Exibe uma mensagem solicitando uma tecla e, em seguida, chama a função
    `main` para reiniciar o menu de seleção.

    Returns
    -------
    None
    """
    input("\nDigite uma tecla para voltar ao menu de seleção: ")
    main()


def subtitulo(texto):
    """
    Limpa a tela e exibe um subtítulo formatado com separadores.

    O subtítulo é exibido entre fileiras de caracteres '=' cujo comprimento
    é igual ao comprimento do texto fornecido.

    Parameters
    ----------
    texto : str
        Texto a ser exibido como subtítulo.

    Returns
    -------
    None
    """
    os.system("cls")
    print(f"\n{'='*len(texto)}{texto}{'=' * len(texto)}\n")


def limpar_tela():
    """
    Limpa o terminal.

    Executa o comando do sistema operacional para apagar o conteúdo
    exibido no console (compatível com Windows via ``cls``).

    Returns
    -------
    None
    """
    os.system("cls")


def Tabela_de_selecao():
    """
    Exibe o menu principal de seleção de categorias de conversão.

    Imprime no console as opções disponíveis para o usuário escolher
    qual grandeza física deseja converter.

    Returns
    -------
    None
    """
    print("Conversor de unidades.")
    print("Selecione o tipo de unidade de grandeza que gostaria converter.")
    print("1 - Comprimento")
    print("2 - Massa")
    print("3 - Volume")
    print("4 - Tempo")
    print("5 - Temperatura")


def unidades_digitadas():
    """
    Solicita ao usuário as unidades de origem, destino e o valor a converter.

    Lê três entradas do console: a unidade de medida de origem, a unidade de
    medida de destino e o valor numérico a ser convertido. As unidades são
    normalizadas para letras minúsculas e sem espaços extras.

    Returns
    -------
    unidade1 : str
        Símbolo da unidade de medida de origem (ex: ``"km"``, ``"c"``).
    unidade2 : str
        Símbolo da unidade de medida de destino (ex: ``"m"``, ``"f"``).
    valor : float
        Valor numérico a ser convertido.
    """
    unidade1 = input("Digite a unidade de medida que deseja converter: ").lower().strip()
    unidade2 = input("Digite a unidade de medida para qual deseja converter: ").lower().strip()
    valor = float(input("Digite o valor que deseja converter: "))
    return unidade1, unidade2, valor


def comprimento():
    """
    Executa o fluxo interativo de conversão entre unidades de comprimento.

    Exibe as unidades disponíveis, coleta as entradas do usuário e realiza
    a conversão usando metro como unidade-base intermediária. Unidades
    suportadas: ``km``, ``hm``, ``dam``, ``m``, ``dm``, ``cm``, ``mm``.

    A conversão segue a fórmula::

        valor_convertido = (valor * fator_origem) / fator_destino

    onde cada fator representa o equivalente em metros da unidade.

    Returns
    -------
    None

    Notes
    -----
    Em caso de unidade inválida, o programa exibe uma mensagem de erro
    e retorna ao menu principal.
    """
    subtitulo("Conversor de comprimento")
    print("Unidades disponíveis:\n")
    print("Quilômetro: km")
    print("Hectômetro: hm")
    print("Decâmetro: dam")
    print("Metro: m")
    print("Decímetro: dm")
    print("Centímetro: cm")
    print("Milímetro: mm\n")

    unidade_primaria, unidade_secundaria, valor = unidades_digitadas()

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
        print(f"Resultado: {valor} {unidade_primaria} = {valor_convertido} {unidade_secundaria}.")
    else:
        print("Unidade de medida inválida. Por favor, selecione unidades válidas.")
        input("\nDigite uma tecla para voltar ao menu de seleção: ")
        voltar_ao_menu()

    voltar_ao_menu()


def massa():
    """
    Executa o fluxo interativo de conversão entre unidades de massa.

    Exibe as unidades disponíveis, coleta as entradas do usuário e realiza
    a conversão usando grama como unidade-base intermediária. Unidades
    suportadas: ``kg``, ``hg``, ``dag``, ``g``, ``dg``, ``cg``, ``mg``.

    A conversão segue a fórmula::

        valor_convertido = (valor * fator_origem) / fator_destino

    onde cada fator representa o equivalente em gramas da unidade.

    Returns
    -------
    None

    Notes
    -----
    Em caso de unidade inválida, o programa exibe uma mensagem de erro
    e retorna ao menu principal.
    """
    subtitulo("Conversor de massa")
    print("Unidades disponíveis:\n")
    print("Quilograma: kg")
    print("Hectograma: hg")
    print("Decagrama: dag")
    print("Grama: g")
    print("Decigrama: dg")
    print("Centigrama: cg")
    print("Miligrama: mg\n")

    unidade_principal, unidade_para_conversao, valor = unidades_digitadas()

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
        print(f"Resultado: {valor} {unidade_principal} = {valor_convertido} {unidade_para_conversao}.")
    else:
        print("Unidade de medida inválida. Por favor, selecione unidades válidas.")
        input("\nDigite uma tecla para voltar ao menu de seleção: ")
        voltar_ao_menu()

    voltar_ao_menu()


def temperatura():
    """
    Executa o fluxo interativo de conversão entre escalas de temperatura.

    Exibe as escalas disponíveis, coleta as entradas do usuário e aplica
    a fórmula de conversão correspondente ao par de escalas informado.
    Escalas suportadas: Celsius (``c``), Kelvin (``k``), Fahrenheit (``f``).

    As fórmulas utilizadas são:

    - Celsius → Kelvin:     ``K = C + 273``
    - Kelvin → Celsius:     ``C = K - 273``
    - Celsius → Fahrenheit: ``F = (9 * C / 5) + 32``
    - Fahrenheit → Celsius: ``C = (5 * F - 160) / 9``
    - Kelvin → Fahrenheit:  ``F = ((9 * K - 2457) / 5) + 32``
    - Fahrenheit → Kelvin:  ``K = ((5 * F - 160) / 9) + 273``

    Returns
    -------
    None

    Notes
    -----
    Em caso de escala inválida ou par não reconhecido, o programa exibe
    uma mensagem de erro e retorna ao menu principal.
    """
    subtitulo("Conversor de temperatura")
    print("Unidades disponíveis:\n")
    print("Celsius: C")
    print("Kelvin: K")
    print("Fahrenheit: F\n")

    valor1, valor2, valor = unidades_digitadas()
    valor_convertido = 0

    if valor1 == "c" and valor2 == "k":
        valor_convertido = valor + 273
        print(f"Resultado: {valor} C = {valor_convertido:.4f} K.")
    elif valor1 == "k" and valor2 == "c":
        valor_convertido = valor - 273
        print(f"Resultado: {valor} K = {valor_convertido:.4f} C.")
    elif valor1 == "c" and valor2 == "f":
        valor_convertido = ((9 * valor) / 5) + 32
        print(f"Resultado: {valor} C = {valor_convertido:.4f} F.")
    elif valor1 == "f" and valor2 == "c":
        valor_convertido = ((5 * valor) - 160) / 9
        print(f"Resultado: {valor} F = {valor_convertido:.4f} C.")
    elif valor1 == "k" and valor2 == "f":
        valor_convertido = ((9 * valor - 2457) / 5) + 32
        print(f"Resultado: {valor} K = {valor_convertido:.4f} F.")
    elif valor1 == "f" and valor2 == "k":
        valor_convertido = (((5 * valor) - 160) / 9) + 273
        print(f"Resultado: {valor} F = {valor_convertido:.4f} K.")
    else:
        print("Unidade de medida inválida. Por favor, selecione unidades válidas.")
        voltar_ao_menu()

    voltar_ao_menu()


def tempo():
    """
    Executa o fluxo interativo de conversão entre unidades de tempo.

    Exibe as unidades disponíveis, coleta as entradas do usuário e realiza
    a conversão entre horas, minutos e segundos. Unidades suportadas:
    hora (``h``), minuto (``m``) e segundo (``s``).

    Conversões disponíveis e seus fatores:

    - ``h`` → ``m``: multiplica por 60
    - ``m`` → ``s``: multiplica por 60
    - ``h`` → ``s``: multiplica por 3600
    - ``s`` → ``m``: divisão inteira por 60
    - ``m`` → ``h``: divisão inteira por 60
    - ``s`` → ``h``: divisão inteira por 3600

    Returns
    -------
    None

    Notes
    -----
    Pares de unidades não reconhecidos redirecionam automaticamente ao
    menu principal sem exibir resultado.
    """
    subtitulo("Conversor de tempo")
    print("Unidades disponíveis:\n")
    print("Hora: h")
    print("Minuto: m")
    print("Segundo: s\n")

    tempo1, tempo2, valor = unidades_digitadas()

    if tempo1 == "h" and tempo2 == "m":
        print(f"Resultado: {valor} h = {valor * 60} m.")
    elif tempo1 == "m" and tempo2 == "s":
        print(f"Resultado: {valor} m = {valor * 60} s.")
    elif tempo1 == "h" and tempo2 == "s":
        print(f"Resultado: {valor} h = {valor * 3600} s.")
    elif tempo1 == "s" and tempo2 == "m":
        print(f"Resultado: {valor} s = {valor // 60} m.")
    elif tempo1 == "m" and tempo2 == "h":
        print(f"Resultado: {valor} m = {valor // 60} h.")
    elif tempo1 == "s" and tempo2 == "h":
        print(f"Resultado: {valor} s = {valor // 3600} h.")
    else:
        print("Unidade de medida inválida. Por favor, selecione unidades válidas.")
        voltar_ao_menu()

    voltar_ao_menu()


def volume():
    """
    Executa o fluxo interativo de conversão entre unidades de volume.

    Exibe as unidades cúbicas disponíveis, coleta as entradas do usuário
    e realiza a conversão usando metro cúbico (``m³``) como unidade-base
    intermediária. Unidades suportadas: ``km``, ``hm``, ``dam``, ``m``,
    ``dm``, ``cm``, ``mm`` (todas interpretadas como cúbicas).

    A conversão segue a fórmula::

        valor_convertido = (valor * fator_origem) / fator_destino

    onde cada fator representa o equivalente em metros cúbicos da unidade.

    Returns
    -------
    None

    Notes
    -----
    Em caso de unidade inválida, o programa exibe uma mensagem de erro
    e retorna ao menu principal.
    """
    subtitulo("Conversor de volume")
    print("Unidades disponíveis:\n")
    lista_volume = {
        "km": 1000 ** 3,
        "hm": 1000 ** 2,
        "dam": 1000 ** 1,
        "m": 1,
        "dm": 1000 ** -1,
        "cm": 1000 ** -2,
        "mm": 1000 ** -3
    }

    nomes_volume = {
        "km": "Quilômetro cúbico",
        "hm": "Hectômetro cúbico",
        "dam": "Decâmetro cúbico",
        "m": "Metro cúbico",
        "dm": "Decímetro cúbico",
        "cm": "Centímetro cúbico",
        "mm": "Milímetro cúbico"
    }

    for simbolo, nome in nomes_volume.items():
        print(f"{nome}: {simbolo}³")

    print()
    volume1, volume2, valor = unidades_digitadas()

    if volume1 in lista_volume and volume2 in lista_volume:
        processo = valor * lista_volume[volume1]
        conversao = processo / lista_volume[volume2]
        print(f"Resultado: {valor} {volume1}³ = {conversao} {volume2}³.")
    else:
        print("Unidade de medida inválida. Por favor, selecione unidades válidas.")
        input("\nDigite uma tecla para voltar ao menu de seleção: ")
        voltar_ao_menu()

    voltar_ao_menu()


def selecao():
    """
    Lê a opção do usuário e despacha para o conversor correspondente.

    Solicita um número inteiro via console e utiliza um ``match``/``case``
    para chamar a função de conversão adequada. Caso o valor digitado não
    corresponda a nenhuma opção válida, exibe uma mensagem de erro e
    retorna ao menu principal.

    Mapeamento de opções:

    - ``1`` → :func:`comprimento`
    - ``2`` → :func:`massa`
    - ``3`` → :func:`volume`
    - ``4`` → :func:`tempo`
    - ``5`` → :func:`temperatura`

    Returns
    -------
    None
    """
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
    """
    Ponto de entrada principal do conversor de unidades.

    Limpa o terminal, exibe o menu de seleção de categorias e aguarda
    a escolha do usuário para iniciar o fluxo de conversão correspondente.

    Returns
    -------
    None
    """
    os.system("cls")
    Tabela_de_selecao()
    selecao()


if __name__ == "__main__":
    main()
