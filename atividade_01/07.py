def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

# Solicita o valor limite da sequência de Fibonacci
limite = int(input("Digite um valor para o limite da sequência de Fibonacci: "))

if limite < 0:
    print("O valor deve ser não negativo.")
else:
    fibonacci_seq = fibonacci_sequence(limite)
    print("Sequência de Fibonacci até", limite, ":", fibonacci_seq)
