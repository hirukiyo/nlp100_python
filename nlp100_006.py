# -*- coding: utf-8 -*-

"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれXとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

import nlp100_005 as n_gram

# bi-gramを取得
X = n_gram.char_n_gram("paraparaparadise", 2)
Y = n_gram.char_n_gram("paragraph", 2)
print("bi-gram X: ", X)
print("bi-gram Y: ", Y)

SX = set(X)  # Xの集合
SY = set(Y)  # Yの集合
print("Xの集合 SX: ", SX)
print("Yの集合 SY: ", SY)

# 課題回答
print("XとYの和集合: ", SX.union(SY))
print("XとYの積集合: ", SX.intersection(SY))
print("XとYの差集合: ", SX.difference(SY))
print("'se'がXに含まれるか？: ", "Yes" if "se" in X else "No")
print("'se'がYに含まれるか？: ", "Yes" if "se" in Y else "No")
