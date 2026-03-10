num = []
contador = 0
acima_media = []
for n in range(6):
    num.append(float(input("Digite um número: ")))
lista = len(num)
maior = max(num)
menor = min(num)
media = sum(num) / len(num)
for numero in num:
        contador+=1
        acima_media.append(num[c])
print(f"Existe {contador} números acima da média!")
print(f"Número acima da média: {acima_media}")
print(f"A lista é: {num}")
print(f"o maior é {maior} e o menor é {menor}")
print(f"A lista tem {lista} números")
print(f"A média dos números na lista é {media:.2f}")