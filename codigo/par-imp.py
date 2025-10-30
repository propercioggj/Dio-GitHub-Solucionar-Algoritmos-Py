def eh_par(n: int) -> bool:
    """Retorna True se n for par, False caso contrário."""
    return n % 2 == 0

def main() -> None:
    try:
        num = int(input("Digite um número inteiro: ").strip())
    except ValueError:
        print("Entrada inválida: informe um número inteiro.")
        return

    if eh_par(num):
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")

if __name__ == "__main__":
    main()