def numero_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primeiro_numero = int(input())
segundo_numero = int(input())

resultado_soma= primeiro_numero + segundo_numero
resultado_sub= primeiro_numero - segundo_numero
resultado_mult= primeiro_numero * segundo_numero
resultado_div= primeiro_numero // segundo_numero

print(resultado_soma)
print(resultado_sub)
print(resultado_mult)
print(resultado_div)

for i, n in enumerate([primeiro_numero, segundo_numero], start=1):
    if n % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

    if numero_primo(n):
        print("É número Primo")
    else:
        print("Não é número Primo")