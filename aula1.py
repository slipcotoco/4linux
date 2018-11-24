#nome = input("Nome")
#print("Ola seja bem-vindo", nome.title())

#lista
'''
letras = ['a','b','c','d']
print(letras)
print(letras[0])

letras.insert(0, 'Z')
print (letras)

#dicionario

suporte = {'raspberry': 'leo', 'estoque': 'matheus'}
'''
n1 = float (input('Digite uma nota   :'  ))
n2 = float (input('Digite uma nota   :'))

media  = (n1+n2)/2

if n1 or n2 > 10: 
    print('O valor de nota nao pode ser maior que 10')
elif media >=7: 
    print('Aprovado')
elif media >3:
    print('Recuperacao')
else:
    print('Reprovado')