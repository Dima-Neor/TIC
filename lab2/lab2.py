import math
import tkinter as tk
from collections import Counter

def h(x):
    if x == 0 : return x
    else : return math.log2(x) * x

# Энропия
def entropy(pArray):
    sum = 0
    for i in pArray :
        sum += h(i)
    return -sum

# Вычисление H(Y|X) - Количество информации, которое несет появление первой буквы о второй
def entropyYX(arrx: dict, arrxy: dict, k: int):
    entropy = 0
    for el1 in arrx:
        el1Count = arrx[el1]
        w1 = el1Count / k
        for el2 in arrxy:
            if (el2[0] == el1):
                el2Count = arrxy[el2]
                w2 = el2Count / k
                entropy += w2 * math.log2(w2 / w1)
    return -entropy

# Обработчик кнопки, вычисление энтропии
def calculate ():
    text = inTxt_ent.get()
    # длина сообщения
    k = len(text)

    # двух буквенные сочетания
    txtArr = []
    for i in range(k-1):
        tmp = text[i] + text[i+1]
        txtArr.append(tmp)

    # Количество символов в сообщении
    case = Counter(text)
    # Кол-во пар символов в сообщении
    case2 = Counter(txtArr)

    # Массив вероятностей
    earr = []

    strI = ''
    strX = ''
    addxy = ''
    strN = ''
    strW = ''

    arrx = []
    arrxy = []

    strI += f"№\t| "
    strX += f"X\t| "
    strN += f"N\t| "
    strW += f"W\t| "

    j = 1
    for i in case.keys():
        # Считаем wi
        l = case[i]/k
        earr.append(l)
        strI += f"{j} \t| "
        arrx.append(l)
        strX +=  f"{i} \t| "
        strN += f"{case[i]} \t| "
        strW += f"{l:.3f} \t| "
        j += 1

    outNum_lbl.configure(text=strI)
    outX_lbl.configure(text=strX)
    outN_lbl.configure(text=strN)
    outW_lbl.configure(text=strW)

    e1 = entropy(earr)
    outH_lbl.configure(text="H(X) =" + f"{e1:.3f}")

    strI = f"№\t| "
    strX = f"X\t| "
    strN = f"N\t| "
    strW = f"W\t| "

    # Массив вероятностей 2-х буквенных
    earr2 = []
    j = 1
    for i in case2.keys():
        # Считаем wi
        l = case2[i]/(k-1)
        earr2.append(l)
        strI += f"{j} \t| "
        arrxy.append(l)
        strX += f"{i} \t| "
        strN += f"{case2[i]} \t| "
        strW += f"{round(l, 3)} \t| "
        j += 1

    outNum2_lbl.configure(text=strI)
    outXY_lbl.configure(text=strX)
    outN2_lbl.configure(text=strN)
    outW2_lbl.configure(text=strW)

    e2 = entropy(earr2)
    outH2_lbl.configure(text=f"H(XY) = {e2:.3f}")
    e3 = entropyYX(case, case2, k)
    outH3_lbl.configure(text=f"H(X|Y) = {e3:.3f}")
    outI_lbl.configure(text=f"I(X,Y) = {(e1 - e3):.3f}")

    # Длина кода
    codeLength = math.ceil(math.log2(len(case)))
    outL_lbl.configure(text=f"Длина кода (l) = {codeLength}")

    dp = 1 - e1 / codeLength
    ds = 1 - e3 / e1
    d = dp + ds - dp * ds
    outD_lbl.configure (text=f"Dp = {dp:.3f}\tDs = {ds:.3f}\tD = {d:.3f}")
    

window = tk.Tk()

# Создаем форму для заполнения
frame1 = tk.Frame(master=window, borderwidth=3)
frame1.pack(fill=tk.X, side=tk.TOP)

inTxt_lbl = tk.Label(master=frame1, text="Введите текст:")
inTxt_lbl.pack(side=tk.LEFT)
inTxt_ent = tk.Entry(master=frame1)
inTxt_ent.pack(fill=tk.X)

# Создаем кнопку для вычисления значений
enter_btn = tk.Button( master=window, text="Вычислить", command=calculate)
enter_btn.pack(fill=tk.X, side=tk.TOP)

# Создаем форму для вывода результата
frame2 = tk.Frame(master=window, borderwidth=3)
frame2.pack(fill=tk.X, side=tk.TOP)

outNum_lbl = tk.Label(master=frame2, text="№ | ...", bg="#E6E6FA")
outNum_lbl.pack(side=tk.TOP)
outX_lbl = tk.Label(master=frame2, text="X | ...", bg="#E6E6FA")
outX_lbl.pack(side=tk.TOP)
outN_lbl = tk.Label(master=frame2, text="n | ...", bg="#E6E6FA")
outN_lbl.pack(side=tk.TOP)
outW_lbl = tk.Label(master=frame2, text="w | ...", bg="#E6E6FA")
outW_lbl.pack(side=tk.TOP)
outH_lbl = tk.Label(master=frame2, text="H(X) = ...", borderwidth=3)
outH_lbl.pack(side=tk.TOP)

space_frm = tk.Frame(master=window, height= 20) # Разделитель
space_frm.pack(side=tk.TOP)

# Создаем форму для вывода результата
frame3 = tk.Frame(master=window, borderwidth=3)
frame3.pack(fill=tk.X, side=tk.TOP)

outNum2_lbl = tk.Label(master=frame3, text="№ | ...", bg="#E6E6FA")
outNum2_lbl.pack(side=tk.TOP)
outXY_lbl = tk.Label(master=frame3, text="XY | ...", bg="#E6E6FA")
outXY_lbl.pack(side=tk.TOP)
outN2_lbl = tk.Label(master=frame3, text="n | ...", bg="#E6E6FA")
outN2_lbl.pack(side=tk.TOP)
outW2_lbl = tk.Label(master=frame3, text="w | ...", bg="#E6E6FA")
outW2_lbl.pack(side=tk.TOP)
outH2_lbl = tk.Label(master=frame3, text="H(XY) = ...", borderwidth=3)
outH2_lbl.pack(side=tk.TOP)

outH3_lbl = tk.Label(master=frame3, text="H(X\Y) = ...", borderwidth=3)
outH3_lbl.pack(side=tk.TOP)
outI_lbl = tk.Label(master=frame3, text="I(X,Y) = ...")
outI_lbl.pack(side=tk.TOP)
outL_lbl = tk.Label(master=frame3, text="Длина кода (l) = ...")
outL_lbl.pack(side=tk.TOP)
outD_lbl = tk.Label(master=frame3)
outD_lbl.pack(side=tk.TOP)


window.mainloop()
