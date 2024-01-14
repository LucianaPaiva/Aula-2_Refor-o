lista = ["Banana", "Maça", "Uva"]

nome_fruta = str(input("Digite o nome da fruta: "))
quantidade_fruta = int(input("Digite a quantidade de frutas no estoque: "))
preco_fruta = float(input("Digite o preço da fruta: "))

lista2 = [
    {
    "Nome": nome_fruta,
    "Quantidade": quantidade_fruta,
    "Preço": preco_fruta,
    },
    {
    "Nome": str(input("Digite o nome da fruta: ")),
    "Quantidade": int(input("Digite a quantidade de frutas no estoque: ")),
    "Preço": float(input("Digite o preço da fruta: "))
    },
    {
    "Nome": None,
    "Quantidade": None,
    "Preço": None
    }
 ]

lista2[2]["Nome"] = str(input("Digite o nome da fruta: "))
lista2[2]["Quantidade"] = int(input("Digite a quantidade de frutas no estoque: "))
lista2[2]["Preço"] = float(input("Digite o preço da fruta: "))


novo_item = {
    "Nome": str(input("Digite o nome da fruta: ")),
    "Quantidade": int(input("Digite a quantidade de frutas no estoque: ")),
    "Preço": float(input("Digite o preço da fruta: "))
}
lista2.append(novo_item)


