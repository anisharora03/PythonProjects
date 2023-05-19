import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats import norm
import random
df = pd.read_csv("AAPL.csv", index_col = "Date")
df1 = df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis = 1)

def plot_norm(df7):
    plt.hist(df2, bins=20, density=True)
    mean = df7['Adj Close'].mean()
    std = df7['Adj Close'].std()
    x = np.arange(-7, 7, 0.1)
    plt.plot(x, norm.pdf(x, mean, std))
    plt.show()
# Press the green button in the gutter to run the script.
def plot_rollingavg(df6):
    df4 = df6.rolling(7).sum() / 7
    plt.plot(df6.iloc[6:])
    plt.plot(df4)
    plt.show()
def plot_bb(df1):
    df4 = df1.rolling(7).sum() / 7
    df3 = df1.rolling(7).std()
    dftop = df4 + 2 * df3
    dfbot = df4 - 2 * df3
    plt.plot(dftop)
    plt.plot(dfbot)
    plt.plot(df1)
    plt.show()
def states1(df):
    ser = df.squeeze()
    ser1 = ser.sort_values()
    ser2 = ser1.dropna()
    ser3 = ser.dropna()
    stepsize = int(ser2.size / 10)
    threshold = []
    for i in range(0, 10):
        threshold.append(ser2.iloc[(i + 1) * stepsize])
    holder = []
    for x in range(0, ser3.size):
        threshold.append(ser3.iloc[x])
        threshold.sort()
        holder.append(threshold.index(ser3.iloc[x]))
        holder.append(threshold.index(ser3.iloc[x]))
        holder.append(threshold.index(ser3.iloc[x]))
        threshold.remove(ser3.iloc[x])
    df1 = pd.DataFrame(data = holder)
    return df1
def retq(df1, df2, df3):
    list1 = states1(df1)
    list2 = states1(df2)
    list3 = list1 * 100 + list2
    list4 = []
    list6 = []
    for i in range(245):
        for j in range(3):
            list4.append(j)
            list6.append(df3.iloc[i,0])
    list3['1'] = list4
    list5 = []
    for i in range(735):
        list5.append(random.randrange(50, 100, 1))
    list3['2'] = list6
    list3['3'] = list5
    return list3
def qlearn(df,k, init):
    list4 = []
    for i in range(k, k+60, 3):
        list2 = []
        for j in range(3):
            list2.append(df.iloc[i + j, 3])
        list4.append(i + list2.index(max(list2)))
    list5 = []
    list5.append(init)
    for i in range(0,len(list4) - 1):
        ret = df.iloc[list4[i +1], 2] - df.iloc[list4[i], 2]
        if df.iloc[list4[i], 1] == 0:
            ret *= 2
        elif df.iloc[list4[i], 1] == 2:
            ret /= 2
        list5.append(list5[len(list5) -1] + ret)
        df.iloc[list4[i], 3] *= 0.7
        df.iloc[list4[i], 3] += 0.3 * (ret + 0.3 * (df.iloc[list4[i + 1], 2]))
    return list5
def execqlearn(list1):
    list4 = []
    init = list1.iloc[0, 2]
    for j in range(10):
        for i in range(70):
            list3 = qlearn(list1, j, init)
        init = list3[len(list3) - 1]
        list4 += list3
    df3 = pd.DataFrame(data=list4, index=df1.index[6:206])
    plt.plot(df3)
    plt.plot(df1.iloc[6:206])
    plt.show()


