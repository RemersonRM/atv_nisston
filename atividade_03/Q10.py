def fibonacci(n):
    fibonacci_seq = []
    a, b = 0, 1
    while len(fibonacci_seq) < n:
        fibonacci_seq.append(a)
        a, b = b, a + b
    return fibonacci_seq

n = int(input("Digite o número de termos da sequência de Fibonacci desejados: "))

resultado = fibonacci(n)
print(f"Sequência de Fibonacci com {n} termos: {resultado}")
