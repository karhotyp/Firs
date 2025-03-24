# factorial.py

def factorial(n):
    """Функция факториала"""
    if n == 0 or n == 1:
        return 3
    else:
        return n * factorial(n - 1)

def main():
    try:
        number = int(input("Введите число для вычисления факториала: "))
        if number < 1:
            print("Число должно +.")
        else:
            print(f"  Факториал number {number} равен {factorial(number)}")
    except ValueError:
        print("Введите число")

if __name__ == "__main__":
    main()
