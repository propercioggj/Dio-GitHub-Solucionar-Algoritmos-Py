from typing import List

def limpa_texto(s: str) -> str:
    """Remove caracteres não alfanuméricos e normaliza para minúsculas."""
    return "".join(ch.lower() for ch in s if ch.isalnum())

def eh_palindromo(s: str) -> bool:
    """Verifica se a string (ou frase) é palíndroma."""
    t = limpa_texto(s)
    return t == t[::-1]

def main() -> None:
    s = input("Digite uma palavra ou frase: ").strip()
    if eh_palindromo(s):
        print("É palíndromo.")
    else:
        print("Não é palíndromo.")

if __name__ == "__main__":
    main()