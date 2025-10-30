def concat_strings(a: str, b: str) -> str:
    return a + b

def main():
    a = input("Digite a primeira string: ")
    b = input("Digite a segunda string: ")
    print(concat_strings(a, b))

if __name__ == "__main__":
    main()