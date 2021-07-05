# What is pandas?
# What does it have?
# How to use it?
import pandas as pd
import sys
# Dimensions of pandas structures:
# Series: 1D
# DataFrame: 2D
# Panel: 3D

# Series:
players = pd.Series([14,54,38,None], name="counts")
print(players.size)
print(players.index)

players = pd.Series([14,54,38,None], name="counts", index = ["a","b","c","d"])
print(players.count())
print(players.std())
sc = players
x= int(sc.count())/int(sc.size) * 100
print(x)
print(players.index)
print(players["a"])
print(players.count()) # doesnt not cound NaN 
players["b"] = 55
print(players.mean())

print(players[players >30]) # Boolean filter same as numpy
for x in players:
    print(x)
print(14 in players)
print("a" in players)
print(14 in players.values)

for i,v in players.iteritems():
    print(i,v)

print(players.iloc[1]) # To work similar as a list

players["e"] =18

print(players)

del players["d"]
print(players)

print(players.is_unique) # To review if index are duplicated or not

# loc and iloc to access to the data in a optimized way
print(players.iloc[0])
print(players.loc["c"])
print(players.iloc[[0,1]])

# at and iat return single values... not used too much...
print(players.iat[1])
print(players.at["c"])

# + - / * same as 
players = pd.Series([14,54,38,None], name="counts", index = ["a","b","c","d"])

print(players.fillna(0))
print(players)

#useful for inspect 
print(players.count())
print(players.unique())
print(players.duplicated())
print(players.drop_duplicates())
print(players.dropna())

print(players.append(players))
# Sort values
print(players.sort_values())
print(players.sort_index(ascending=False))

# Using lambda function, recommendation use always apply...
print(players.map(lambda x:x+2))
print(players.apply(lambda x:x+2))
# to save .to_csv
# to read .read_csv

# DataFrames: each column is a series
# list of dic
ex = pd.DataFrame([{"a":1, "b":2},{"a":5,"b":9}],index=["z","y"])
print(ex)
# dic of lists
ex2 = pd.DataFrame({"a":[1,2,3,4,5,6],"b":[4,5,6,7,8,9]})
print(ex2)

# To join dataframes
print(ex.append(ex2))
print(pd.concat([ex,ex2]))
ex["x"] = pd.Series([1,2], index = ["z","y"])
print(ex)
# to drop a column use pop, and to delete a row use drop
print(ex.drop("y"))
print(ex.pop("a"))
# first elements .head
# lasts elements .tails 
print("---")
print(ex)
# To acces index like it is there, use loc, to access like list use iloc
print(ex.loc["y"])
print(ex.iloc[1])

# The Values and the indexes can be sorted: 
#  sort_values
#  sort_index
#  describe()

# concat preserve index
# you can ignore_index = True
# to align by index duplicating columns if needed axis = 1
# merge
# join

