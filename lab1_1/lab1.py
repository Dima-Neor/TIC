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

# Создаем форму для заполнения
frame1 = tk.Frame(master=window, bg="red", borderwidth=3)
frame1.pack(fill=tk.X, side=tk.TOP)

inN_lbl = tk.Label(master=frame1, text="Введите n:")
inN_lbl.pack(side=tk.LEFT)
inN_ent = tk.Entry(master=frame1)
inN_ent.pack(side=tk.LEFT)

space_frm = tk.Frame(master=frame1, width= 20, bg="blue") # Разделитель
space_frm.pack(side=tk.LEFT)

inP_lbl = tk.Label(master=frame1, text="Введите p:")
inP_lbl.pack(side=tk.LEFT)
inP_ent = tk.Entry(master=frame1)
inP_ent.pack(side=tk.LEFT)

# Создаем кнопку для вычисления значений
enter_btn = tk.Button( master=window, text="Вычислить")
enter_btn.pack(side=tk.TOP)

# Создаем форму для вывода результата
frame2 = tk.Frame(master=window, bg="green", borderwidth=3)
frame2.pack(fill=tk.X, side=tk.TOP)

outK_lbl = tk.Label(master=frame2, text="k = ...")
outK_lbl.pack(side=tk.TOP)
outP_lbl = tk.Label(master=frame2, text="p = ...")
outP_lbl.pack(side=tk.TOP)
outEntropy_lbl = tk.Label(master=frame2, text="Энтропия = ...")
outEntropy_lbl.pack(side=tk.TOP)
outMax_lbl = tk.Label(master=frame2, text="Максимум = ...")
outMax_lbl.pack(side=tk.TOP)
outMin_lbl = tk.Label(master=frame2, text="Минимум = ...")
outMin_lbl.pack(side=tk.TOP)

# Создаем форму для вывода графика
frame3 = tk.Frame(master=window, height= 20, bg="yellow", borderwidth=3)
frame3.pack(fill=tk.X, side=tk.TOP)

window.mainloop()