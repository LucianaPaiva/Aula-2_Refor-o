alunos = []

for i in range(5): 
    nome = input("Informe o nome do aluno: ")
    idade = int(input("Informe a idade do aluno: "))
    turma = input("Informe a turma do aluno: ")
    cpf = input("Informe o CPF do aluno: ")

    aluno = {"Nome": nome, "Idade": idade, "Turma": turma, "CPF": cpf}
    alunos.append(aluno)

for aluno in alunos:
    print(f"Nome: {aluno['Nome']}, Idade: {aluno['Idade']}, Turma: {aluno['Turma']}, CPF: {aluno['CPF']}")