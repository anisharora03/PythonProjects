import pandas as pd
from sklearn import preprocessing
def prepareDF():
    df = pd.read_csv("stats.csv")
    df = df.sort_values(by = ["player_id", "year"])
    dfnum = df.iloc[:, 4:]
    mean = dfnum.mean()
    std = dfnum.std()
    zscore = dfnum.sub(mean).div(std)
    skew = dfnum.skew()
    kurt = dfnum.kurtosis()
    df.insert(0, "team", "")
    df.insert(1, "pa", float("NaN"))
    return df
def combine(df, df1, mean):
    for i in range(0,30):
        for x in range(1, 220):
            if(not df1.iloc[i,x] == None):
                df.loc[(df[" first_name"] == " " + df1.iat[i,x]["first_name"]) & (df["last_name"] == df1.iat[i,x]["last_name"]) & (df["year"] == int(df1.iat[i,x]["year"])), "team"] = df1.iloc[i,0]
                df.loc[(df[" first_name"] == " " + df1.iat[i,x]["first_name"]) & (df["last_name"] == df1.iat[i,x]["last_name"]) & (df["year"] == int(df1.iat[i,x]["year"])), "pa"] = int(df1.iloc[i,x]["pa"])
    df = df.sort_values(by = ["team", "year"])
    df = df.dropna(subset = ["pa"])
    df = df.fillna(value = mean)
    df = df.drop(columns= ["Unnamed: 53", "player_id", " first_name", "last_name"])
    return df
def findweightedavg(df, df4):
    for i in list(df.iloc[:,3:].columns):
        df4.insert(len(df4.columns), i, 0)
    for x in range(0,270):
        df2 = df.loc[(df["team"] == df4.iloc[x,1][0]) & (df["year"] == df4.iloc[x,0])]
        for i in list(df2.iloc[:,3:].columns):
            df2[i] = df2.pa * df2[i]
        df4.iloc[x, 3:] = (df2.iloc[:,3:].sum()/df2.pa.sum())
    df4 = df4.drop(columns = ["year", "team"])
    return df4
def process(df4):
    d = preprocessing.normalize(df4.iloc[:,1:])
    scaled_df = pd.DataFrame(d, columns=df4.iloc[:,1:].columns)
    df5 = scaled_df.insert(0, "wp", df4["wp"])
    scaled_df.to_csv("thing.csv", index = False)
if __name__ == '__main__':
    df = prepareDF()
    dfnum = df.iloc[:, 4:]
    mean = dfnum.mean()
    df1 = pd.read_json("players.json")
    df = combine(df, df1, mean)
    df4 = pd.read_json("teams.json")
    df4 = findweightedavg(df, df4)
    process(df4)
