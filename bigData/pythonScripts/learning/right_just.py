
def right_justify(data):
    string = data[::-1]
    for info in range(1,70-len(data)):
        string = string + " "

    print string[::-1]

right_justify("Zubair")
right_justify("Zubair Ahmed")
right_justify("Zubair Ahmed is working in Saggezza Inc")
right_justify("Ahmed Saggezza Inc")
right_justify("Zubair")
right_justify("Zubair")
right_justify("Zubair")
