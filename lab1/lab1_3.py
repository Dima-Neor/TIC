import math
import tkinter as tk
import matplotlib.pyplot
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def CalculateList(n: int, k: int, m: int) -> dict:         
    kList = []
    piList = []
    N = min(m, k) + 1

    # стандартных деталей нет, этропия = 0 
    if (k == 0):
        kList.append(0)
        piList.append(1)
        return kList, piList

    # все детали стандартные, этропия = 0 
    if (k == n):
        for i in range(N):
            kList.append(i)
            piList.append(0)
        
        kList[N-1] = N-1
        piList[N-1] = 1
        return kList, piList


    for i in range(N):
        pi = math.comb(k, i) * math.comb(n - k, m - i) / math.comb(n, m)
        kList.append(i)
        piList.append(pi)
    '''
    Гипергеометрическое распределение
    p = math.comb(k, i) * math.comb(n - k, m - i) / math.comb(n, m)
    '''

    return kList, piList

def h(x):
    if x == 0 : return x
    else : return math.log2(x) * x

# Энропия
def entropy(pArray):
    sum = 0
    for i in pArray :
        sum += h(i)
    return -sum

# Обработчик кнопки, вычисление энтропии
def calculate ():
    n = int(inN_ent.get())
    k = int(inK_ent.get())
    m = int(inM_ent.get())
    if (n < 0):
        print("Ошибка")
    elif (k > n):
        print("Ошибка")
    elif (m > n):
        print("Ошибка")
    else:
        pList = []
        kList = []

        kList, pList = CalculateList(n, k, m)
 
        kStr = "k \t"
        pStr = "p \t"
        for i in range(len(kList)):
            kStr += f"{kList[i]} \t"
            pStr += f"{pList[i]:.3f} \t"
        outK_lbl.configure(text=kStr)
        outP_lbl.configure(text=pStr)
        
        # Находим и выводим энтропию
        entr = 0
        if (k != 0 or k != n):
            entr = entropy(pList)

        outEntropy_lbl.configure(text=f"Энтропия: {entr:.3f}")

        # Находим энтропию на всем промежутке p
        probList = [0]
        entropyList = [0]
        for i in range(1, n+1):
            kList, piList = CalculateList(n, i, m)

            entr2 =  entropy(piList)
            probList.append(i)
            entropyList.append(entr2)

        clonEntropyList = entropyList.copy()
        del clonEntropyList[-1]
        del clonEntropyList[0]
        

        print(f"entropyList -> {entropyList}")
        outMin_lbl.configure(text=f"Минимум: {min(clonEntropyList):.3f}")
        outMax_lbl.configure(text=f"Максимум: {max(clonEntropyList):.3f}")

        plt.clear() # удаление предыдущего графика
        plt.plot(probList, entropyList)
        plt.grid()      # включение отображение сетки

        canvas.draw()

        canvas.get_tk_widget().pack()


window = tk.Tk()

# Создаем форму для заполнения
frame1 = tk.Frame(master=window, borderwidth=3)
frame1.pack(fill=tk.X, side=tk.TOP)

space_frm = tk.Frame(master=frame1, width= 20) # Разделитель
space_frm.pack(side=tk.LEFT)

inN_lbl = tk.Label(master=frame1, text="Введите общее кол-во (n):")
inN_lbl.pack(side=tk.LEFT)
inN_ent = tk.Entry(master=frame1)
inN_ent.pack(side=tk.LEFT)

space_frm = tk.Frame(master=frame1, width= 20) # Разделитель
space_frm.pack(side=tk.LEFT)

inK_lbl = tk.Label(master=frame1, text="Введите кол-во стандартных (k):")
inK_lbl.pack(side=tk.LEFT)
inK_ent = tk.Entry(master=frame1)
inK_ent.pack(side=tk.LEFT)

space_frm2 = tk.Frame(master=frame1, width= 20) # Разделитель
space_frm2.pack(side=tk.LEFT)

inM_lbl = tk.Label(master=frame1, text="Введите кол-во выбраных (m):")
inM_lbl.pack(side=tk.LEFT)
inM_ent = tk.Entry(master=frame1)
inM_ent.pack(side=tk.LEFT)

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

canvas = FigureCanvasTkAgg(fig, master=frame3)

window.mainloop()