def incomodam(n):
    if n < 1:
        return ""
    else:
        return "incomodam " + incomodam(n - 1)

def elefantes(n):
    if n < 2:
        return ""
    else:
        str1a = "Um elefante incomoda muita gente\n"
        str1b = "\n" + str(n - 1) + " elefantes incomodam muita gente\n"
        str1 = str1a if n == 2 else str1b
        str2 = str(n) + " elefantes " + incomodam(n) + "muito mais"
        return elefantes(n - 1) + str1 + str2

#print(elefantes(4))
