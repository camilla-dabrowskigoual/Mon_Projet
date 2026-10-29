#informations du produit

name_product = "ito"
price = 10
stock_number = 4
print(name_product, price, stock_number)
print("le nom du produit est", name_product, "son prix est de", price, "euros", "il en reste", stock_number, "en stock")
print(f"le nom du produit est {name_product}, son prix est de {price} euros, il en reste {stock_number} en stock")

#ajout de produits au stock

stock_number = stock_number + 5
print(stock_number)
print(f"le nouveau nombre de produits en stock est de {stock_number}")

#mise à jour du stock

user = input("quantité achetée par le consommateur :")
stock_number = stock_number - 4
print(f"la nouvelle quantité en stock après achat de l'utilisateur est de {stock_number} produits.")

#nouveau prix après inflation de 10%

price = price*(10/100)+price
print(price)
print(f"le nouveau prix du produit après inflation de 10% est de {price} euros")

#toutes les informations sur le produit

print(name_product, price,stock_number)

