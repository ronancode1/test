coin = 0
print("You Have 0 Coins")
print("To Get Coins You Have To Answer Questions About Python")

def Coin_Gain(C):
    coin = C + 1
    print(coin)

def Coin_Loss(C):
    coin = C - 1
    print(coin)

def Question_1():    
    answer = input("What Is A List? A, B, C, or D \nA. A List Is A Collection Of Items\nB. A List Is A Collection Of Numbers\nC. A List Is A Collection Of Strings\nD. A List Is A Collection Of Integers\n")
    if answer == "A":
        print("Correct")
        Coin_Gain(coin)
        
def Question_2():    
    answer = input("What Is A Variable? A, B, C, or D \nA. A Variable Is A Collection Of Items\nB. A Variable Is A Collection Of Numbers\nC. A Variable Is A Value That Can Change\nD. A Variable Is A Value That Cannot Change\n")
    if answer == "C":    
        print("Correct")
        Coin_Gain(coin)

def Question_3():    
    answer = input("What Is A Function? A, B, C, or D \nA. A Function Is A Collection Of Items\nB. A Function Is A Collection Of Numbers\nC. A Function Is A Value That Can Change\nD. A Function Is A Block Of Code That Only Runs When It Is Called\n")
    if answer == "C":    
        print("Correct")
        Coin_Gain(coin)
        
def Question_4():    
    answer = input("What Is A String/str? A, B, C, or D \nA. A String Is A Collection Of Items\nB. A String Is A Collection Of Numbers\nC. A String Is A Value That Can Change\nD. A String Is A Collection Of Characters\n")
    if answer == "C":    
        print("Correct")
        Coin_Gain(coin)
        
def Question_4():    
    answer = input("What Is A Integer/int? A, B, C, or D \nA. A Integer Is A Collection Of Items\nB. A Integer Is A Collection Of Numbers\nC. A Integer Is A Value That Can Change\nD. A Integer Is A Whole Number\n")
    if answer == "C":    
        print("Correct")
        Coin_Gain(coin)


    

    