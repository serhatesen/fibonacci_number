"""
Fibonacci number

1,1,2,3,5,8,13,21,34..
"""


def fibonacci(n):
    if n <= 1:
        return n

    # İlk iki sayıyı belirle
    fib_prev, fib_curr = 1, 1

    # n-1 kez döngü yap ve sonucu hesapla
    for i in range(1, n):
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr

    return fib_curr

show_fibonacci = []

n_terms = int(input("Kaç tane Fibonacci sayısı hesaplanacak? "))

if n_terms <= 0:
    print("Lütfen pozitif bir tamsayı giriniz.")
else:
    print("Fibonacci dizisi:")
    for i in range(n_terms):
        show_fibonacci.append(fibonacci(i))

print(show_fibonacci)