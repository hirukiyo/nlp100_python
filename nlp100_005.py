# -*- coding: utf-8 -*-

"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""


def n_gram(target, n):
  """
  n-gramを実行する

  :param target: 解析文字列
  :type target: str or list
  :param integer n: 分割数
  :return: n-gram リスト
  :rtype: list
  """
  # できあがるlistの個数は、len(target) - (n - 1)
  list_range = len(target) - (n - 1)
  return [target[i:i+n] for i in range(list_range)]


def char_n_gram(string, n):
  """
  文字 n-gramを実行する

  :param str string: 解析文字列
  :param integer n: 分割数
  :return: n-gram リスト
  :rtype: list
  """
  s = string.replace(',', '').replace('.', '').replace(' ', '')
  return n_gram(s, n)


def word_n_gram(string, n):
  """
  単語 n-gramを実行する

  :param str string: 解析文字列
  :param integer n: 分割数
  :return: n-gram リスト
  :rtype: list
  """
  s = string.replace(',', '').replace('.', '').split(' ')
  return n_gram(s, n)

if __name__ == '__main__':
  print(char_n_gram("I am an NLPer", 2))
  print(word_n_gram("I am an NLPer", 2))
