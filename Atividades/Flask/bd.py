num1 = 45
num2 = 55
calculo = num1 + num2
resultado = calculo

saudacoes_personalizadas = [

    "Salve salve {nome} tudo tranquilo meu rei?" ,
    "Olá {nome} como tem passado?",
    "E ae {nome} como tem passado nessa bela Semana?"

]


nome = "Guilherme"

saudacoes_personalizadas = [s.replace ('{nome}', nome) for s in saudacoes_personalizadas]


