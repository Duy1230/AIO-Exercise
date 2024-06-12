
import math


def is_number(n):
    try:
        float(n)

    except ValueError:
        return False
    return True


def cal_activation():
    activations = ['sigmoid', 'relu', 'elu']
    number = input("Input x= ")
    if not is_number(number):
        print("x must be a number")
        return
    number = float(number)
    function_name = input("Input activation function (sigmoid, relu, elu): ")
    if function_name not in activations:
        print(f"{function_name} is not a supported activation function")

    if function_name == 'sigmoid':
        print(f"sigmoid f({number}) = {1/(1+math.exp(-1*number))}")
    if function_name == 'relu':
        print(f"ReLu f({number}) = {max(0, number)}")
    if function_name == 'elu':
        if number <= 0:
            print(f"Elu f({number}) = {0.01*(math.exp(number)-1)}")
        else:
            print(f"Elu f({number}) = {number}")


if __name__ == "__main__":
    cal_activation()
