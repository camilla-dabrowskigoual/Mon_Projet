#initialisation

initial_amount = 2000
rate =  1
print("gain = (initial_amount*rate)/100")

#augmentatation du capital

initial_amount = initial_amount + 5000
rate = rate + 2
gain = (initial_amount*rate)/100
print(gain)

#montant final de l'investissement

initial_amount = initial_amount - ((10*initial_amount)/100) 
rate = rate - 1
print(initial_amount)
gain = (initial_amount*rate)/100
print(gain)
