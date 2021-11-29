import math
import tkinter as tk
import matplotlib.pyplot
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def h(x):
    if x == 0 : return x
    else : return math.log2(x) * x

# Энропия
def entropy(pArray):
    sum = 0
    for i in pArray :
        sum += h(i)
    return -sum

# Формула Бернули
def bern (p, n, k):
    # math.comb = n! / (k! * (n - k)!)
    # p**k = возведение в степень 
    return math.comb(n, k) * (p**k) * ((1 - p)**(n - k))

# Обработчик кнопки, вычисление энтропии
def calculate ():
    p = float(inP_ent.get())
    n = int(inN_ent.get())
    if (p > 1 or p < 0):
        print("Ошибка")
    else:
        pList = []
        kList = []
        for k in range(n+1):
            pi = bern(p, n, k)
            pi = float(f"{pi:.3f}")
            kList.append(k)
            pList.append(pi)
 
        kStr = "k \t"
        pStr = "p \t"
        for i in range(len(kList)):
            kStr += f"{kList[i]} \t"
            pStr += f"{pList[i]} \t"
        outK_lbl.configure(text=kStr)
        outP_lbl.configure(text=pStr)
        # Находим и выводим энтропию
        entr = 0
        if (p != 0 or p != 1):
            entr = entropy(pList)
        else:
            entr = 0
        outEntropy_lbl.configure(text=f"Энтропия: {entr:.3f}")

        # Находим энтропию на всем промежутке p
        probList = [0]
        entropyList = [0]
        curr_prob = 0.01
        while (curr_prob < 1.01):
            piList = []
            for k in range(n+1):
                pi = bern(curr_prob, n, k)
                pi = float(f"{pi:.3f}")
                piList.append(pi)
            entr2 =  entropy(piList)
            probList.append(curr_prob)
            entropyList.append(entr2)
            curr_prob += 0.01

        clonEntropyList = entropyList.copy()
        del clonEntropyList[0]
        del clonEntropyList[-1]

        outMin_lbl.configure(text=f"Минимум: {min(clonEntropyList):.3f}")
        outMax_lbl.configure(text=f"Максимум: {max(clonEntropyList):.3f}")

        plt.clear() # удаление предыдущего графика
        plt.plot(probList, entropyList)

        canvas.draw()

        canvas.get_tk_widget().pack()


window = tk.Tk()

# Создаем форму для заполнения
frame1 = tk.Frame(master=window, borderwidth=3)
frame1.pack(fill=tk.X, side=tk.TOP)

inN_lbl = tk.Label(master=frame1, text="Введите n:")
inN_lbl.pack(side=tk.LEFT)
inN_ent = tk.Entry(master=frame1)
inN_ent.pack(side=tk.LEFT)

space_frm = tk.Frame(master=frame1, width= 20) # Разделитель
space_frm.pack(side=tk.LEFT)

inP_lbl = tk.Label(master=frame1, text="Введите p:")
inP_lbl.pack(side=tk.LEFT)
inP_ent = tk.Entry(master=frame1)
inP_ent.pack(side=tk.LEFT)

# Создаем кнопку для вычисления значений
enter_btn = tk.Button( master=window, text="Вычислить", command=calculate)
enter_btn.pack(fill=tk.X, side=tk.TOP)

# Создаем форму для вывода результата
frame2 = tk.Frame(master=window, borderwidth=3)
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
frame3 = tk.Frame(master=window, height= 20, borderwidth=3)
frame3.pack(fill=tk.X, side=tk.TOP)

fig = Figure(figsize=(4,4), dpi = 100)
plt = fig.add_subplot(111)
plt.grid()      # включение отображение сетки

canvas = FigureCanvasTkAgg(fig, master=frame3)

window.mainloop()