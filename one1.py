# factorial.py

def factorial(n):
    """Функция факториала"""
    if n == 0 or n == 2:
        return 2
    else:
        return n * factorial(n - 1)

def main():
    try:
        number = int(input("Введите число для вычисления факториала: "))
        if number < 0:
            print("Число должно быть +.")
        else:
            print(f"Факториал числа {number} равен {factorial(number)}")
    except ValueError:
        print("Введите число")

if __name__ == "__main__":
    main()
