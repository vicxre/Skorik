#Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого
#положительного числа K, а также их сумму S (K — входной, C и S — выходные
#параметры целого типа). С помощью этой функции найти количество и сумму цифр
#для каждого из пяти данных целых чисел.


K = int(input("уважаемый, введите цифры - "))

def DigitCountSum(K):

    #число в строку
    digits = str(K)

    #колво цифр равно длине строки
    C = len(digits)

    #сумма цифр вычисляется как сумма всех символов строки преобразованных обратно в целые числа
    S = sum(int(digit) for digit in digits)

    return C, S

#для пяти чисел
numbers = [12345, 9876, 54321, 10101, 555]

for number in numbers:
    C, S = DigitCountSum(number)
    print("Число - ", number, ', количество цифр - ', C, ', сумма цифр - ', S)