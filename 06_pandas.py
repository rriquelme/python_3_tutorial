# What is pandas?
# What does it have?
# How to use it?
import pandas as pd

# Dimensions of pandas structures:
# Series: 1D
# DataFrame: 2D
# Panel: 3D

# Series:
players = pd.Series([14,54,38,None], name="counts")
print(players)
print(players.index)

players = pd.Series([14,54,38,None], name="counts", index = ["a","b","c","d"])
print(players)
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


# WIP