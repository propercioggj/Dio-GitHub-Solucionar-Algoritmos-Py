from typing import Union

def calcular(a: float, b: float, op: str) -> float:
    """Realiza a operação op entre a e b. Op válidas: +, -, *, /"""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Divisão por zero.")
        return a / b
    raise ValueError(f"Operação inválida: {op}")

def main() -> None:
    try:
        a = float(input("Digite o primeiro número: ").strip())
        b = float(input("Digite o segundo número: ").strip())
    except ValueError:
        print("Entrada inválida: informe números (inteiros ou decimais).")
        return

    op = input("Escolha a operação (+, -, *, /): ").strip()
    try:
        resultado = calcular(a, b, op)
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
        return
    except ValueError as e:
        print(e)
        return

    # Mostra sem .0 quando o resultado for inteiro
    if isinstance(resultado, float) and resultado.is_integer():
        print(int(resultado))
    else:
        print(resultado)

if __name__ == "__main__":
    main()