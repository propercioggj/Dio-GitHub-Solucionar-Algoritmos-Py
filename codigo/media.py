from typing import List

def calcular_media(notas: List[float]) -> float:
    """Retorna a média aritmética das notas fornecidas."""
    return sum(notas) / len(notas)

def main() -> None:
    notas: List[float] = []
    for i in range(1, 4):
        try:
            valor = float(input(f"Digite a {i}ª nota: ").strip())
        except ValueError:
            print("Entrada inválida: informe um número (ex.: 7.5).")
            return
        notas.append(valor)

    media = calcular_media(notas)
    print(f"Média: {media:.2f}")

if __name__ == "__main__":
    main()