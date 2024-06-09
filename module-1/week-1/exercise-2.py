
def is_number (n) :
    try :
        float (n) 

    except ValueError :
        return False
    return True

import math
def cal_activation():
    activations = ['sigmoid', 'relu', 'elu']
    number = input("Input x= ")
    if not is_number(number):
        print("x must be a number")
        return
    number = float(number)
    function = input("Input activation function (sigmoid, relu, elu): ")
    if function not in activations:
        print(f"{function} is not a supported activation function")
    
    if function == 'sigmoid':
        print(f"sigmoid f({number}) = {1/(1+math.exp(-1*number))}")
    if  function == 'relu':
        print(f"ReLu f({number}) = {max(0,number)}")
    if function == 'elu':
        if number <= 0:
            print(f"Elu f({number}) = {0.01*(math.exp(number)-1)}")
        else:
            print(f"Elu f({number}) = {number}")

if __name__ == "__main__":
    cal_activation()