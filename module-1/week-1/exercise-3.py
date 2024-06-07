import math
import random

def mae(y_pred, y_true):
    return abs(y_pred - y_true)

def mse(y_pred, y_true):
    return (y_true - y_pred)**2

def cal_loss(loss, y_pred, y_true):
    if loss == 'mae':
        return mae(y_pred, y_true)
    if loss == 'mse':
        return mse(y_pred, y_true)


def exercise_3():
    num_sample = input("Input number of samples: ")
    if not num_sample.isnumeric():
        print("Number of samples must be a positive integer")
        return
    if int(num_sample) == 0:
        print("Number of samples must be a positive integer")
        return

    num_sample = int(num_sample)
    
    loss = input("Input loss function (mae, mse): ")
    if loss not in ['mae', 'mse']:
        print(f"{loss} is not a supported loss function")
        return
    
    total = 0
    for i in range(num_sample):
        predict = random.uniform(1, 10)
        true = random.uniform(1, 10)
        total += cal_loss(loss, predict, true)
        print(f"{loss.upper()}, sample: {i}, predict: {predict}, target: {true}, loss: {cal_loss(loss, predict, true)}")

    print(f"Final {loss.upper()} loss: {total/num_sample}")
if __name__ == "__main__":
    exercise_3()