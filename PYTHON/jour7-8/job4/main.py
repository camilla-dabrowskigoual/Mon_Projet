alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
message = ["a", "n", "n", "e", "m", "z"]
message_code =[]
decalage = 3

def code (message, decalage):
    for i in range(len(message)) :
        if message[i] == "a":
            message_code.append(alphabet[(0+decalage)%26])
        elif message[i] == "b":
            message_code.append(alphabet[(1+decalage)%26])
        elif message[i] == "c":
            message_code.append(alphabet[(2+decalage)%26])
        elif message[i] == "d":
                message_code.append(alphabet[(3+decalage)%26])
        elif message[i] == "e":
                message_code.append(alphabet[(4+decalage)%26])
        elif message[i] == "f":
                message_code.append(alphabet[(5+decalage)%26])
        elif message[i] == "g":
                message_code.append(alphabet[(6+decalage)%26])
        elif message[i] == "h":
                message_code.append(alphabet[(7+decalage)%26])
        elif message[i] == "i":
                message_code.append(alphabet[(8+decalage)%26])
        elif message[i] == "j":
                message_code.append(alphabet[(9+decalage)%26])
        elif message[i] == "k":
                message_code.append(alphabet[(10+decalage)%26])
        elif message[i] == "l":
                message_code.append(alphabet[(11+decalage)%26])
        elif message[i] == "m":
                message_code.append(alphabet[(12+decalage)%26])
        elif message[i] == "n":
                message_code.append(alphabet[(13+decalage)%26])
        elif message[i] == "o":
                message_code.append(alphabet[(14+decalage)%26])
        elif message[i] == "p":
                message_code.append(alphabet[(15+decalage)%26])
        elif message[i] == "q":
                message_code.append(alphabet[(16+decalage)%26])
        elif message[i] == "r":
                message_code.append(alphabet[(17+decalage)%26])
        elif message[i] == "s":
                message_code.append(alphabet[(18+decalage)%26])
        elif message[i] == "t":
                message_code.append(alphabet[(19+decalage)%26])
        elif message[i] == "u":
                message_code.append(alphabet[(20+decalage)%26])
        elif message[i] == "v":
                message_code.append(alphabet[(21+decalage)%26])
        elif message[i] == "w":
                message_code.append(alphabet[(22+decalage)%26])
        elif message[i] == "x":
                message_code.append(alphabet[(23+decalage)%26])
        elif message[i] == "y":
                message_code.append(alphabet[(24+decalage)%26])
        elif message[i] == "z":
                message_code.append(alphabet[(25+decalage)%26])
    print(*message_code, sep="")

code(message,decalage)