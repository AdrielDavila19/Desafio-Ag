#Desafio Media aluno.

print("Bem-vindo ao sistema de media de alunos")

#Recebe dados do aluno
nomeAluno = input("Digite o nome do aluno: ") 
nota1 = float(input("digite a primeira nota do aluno: "))
nota2 = float(input("digite a segunda nota do aluno: "))
nota3 = float(input("digite a terceira nota do aluno: "))

#Calcula a media
media = (nota1 + nota2 + nota3) / 3

#Faz a verificação da media e imprime o resultado
if media >= 7:
    print("A media do aluno ", nomeAluno, "é: ", media, "O aluno foi aprovado")
elif 5 <= media <= 6.9:
    print("A media do aluno ", nomeAluno, "é: ", media, "O aluno esta em recuperação")
else:
    print("A media do aluno ", nomeAluno, "é: ", media, "O aluno foi reprovado")