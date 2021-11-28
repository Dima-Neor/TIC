import math
import tkinter as tk

n = 0
p = 0

def h(x):
    if x == 0 : return x
    else : return math.log2(x) * x

# Энропия
def entropy(pArray):
    sum = 0
    for i in pArray :
        sum += h(i)
    return sum

# Формула Бернули
def bern (p, n, k):
    # math.comb = n! / (k! * (n - k)!)
    # p**k = возведение в степень 
    return math.comb(n, k) * (p**k) * ((1 - p)**(n - k))

window = tk.Tk()
window.mainloop()