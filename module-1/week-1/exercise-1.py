def exercise1(tp, fp, fn):
    if not type(tp) == int:
        print("tp must be an integer")
        return
    if not type(fp) == int:
        print("fp must be an integer")
        return
    if not type(fn) == int:
        print("fn must be an integer")
        return
    
    if tp == 0 or fp == 0 or fn == 0:
        print("tp, fp, and fn must all be greater than 0")
        return
    
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    print(f"Precision is: {precision}")
    print(f"Recall is: {recall}")
    print(f"F1 is: {(2*precision*recall)/(precision+recall)}")

if __name__ == "__main__":
    exercise1(2, 3, 0)