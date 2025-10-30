def repeat_string(s: str, n: int) -> str:
    """Retorna a string s repetida n vezes."""
    return s * n

def main():
    s = input("Digite a string: ")
    try:
        n = int(input("Digite um número inteiro (quantas vezes repetir): "))
    except ValueError:
        print("Entrada inválida: informe um número inteiro.")
        return
    if n < 0:
        print("Informe um número inteiro não-negativo.")
        return
    print(repeat_string(s, n))

if __name__ == "__main__":
    main()