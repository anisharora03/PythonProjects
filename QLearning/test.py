from main import retq
from main import df1
from main import execqlearn
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import random
def actions(list1):
    list3 = []
    for i in range(600, 734, 3):
        leng = len(list3)
        for j in range(0, 600, 3):
            if list1.iloc[i, 0] == list1.iloc[j, 0]:
                list2 = []
                for k in range(3):
                    list2.append(list1.iloc[j + k, 3])
                list3.append(list2.index(max(list2)))
                break
        if leng == len(list3):
            list3.append(1)
    return list3
def createPortfolio(list5):
    shares = 100
    list4 = []
    for i in range(len(list5)):
        if list5[i] == 0:
            list4.append(shares)
            shares += 10
        elif list5[i] == 2:
            list4.append(shares)
            shares -= 10
        else:
            list4.append(shares)
    portfolio = []

    for j in range(600, 734, 3):
        portfolio.append(list1.iloc[j, 2] * list4[int((j - 600) / 3)])
    return portfolio
def tester(list3):
    list5 = [0,1,2]
    list6 = random.choices(list5, k = len(list3))
    list4 = createPortfolio(list6)
    portfolio = createPortfolio(list3)
    df2 = pd.DataFrame(data = list4, index = df1.index[206:])
    df3 = pd.DataFrame(data=portfolio, index=df1.index[206:])
    plt.plot(df3, "-b", label="Q table")
    plt.plot(df2, "-r", label="Random")
    plt.legend(loc="upper left")
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value")
    plt.show()
if __name__ == '__main__':
    df4 = df1.rolling(7).sum() / 7
    adjra = df1 / df4
    risk = df1.rolling(7).std()
    list1 = retq(adjra, risk, df1.iloc[6:])
    matplotlib.use('TkAgg')
    execqlearn(list1)
    list3 = actions(list1)
    tester(list3)