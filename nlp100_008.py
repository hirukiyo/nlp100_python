# -*- coding: utf-8 -*-

"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def cipher(target):
  """
  文字列を暗号化する

  :param str target: 対象文字列
  :return: 暗号化後文字列
  :rtype: str
  """
  res = "".join(c if c < "a" or "z" < c else chr(219 - ord(c)) for c in target)
  print(res)

if __name__ == '__main__':
  s = "Now I need a drink, alcoholic of course, after the heavy lectures " \
      + "involving quantum mechanics."
  cipher(s)
