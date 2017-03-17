# -*- coding: utf-8 -*-

"""
第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」の
タブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，
hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを
表示せよ．確認にはheadコマンドを用いよ．
"""
import argparse


def head(file, lines):
  """
  指定したファイルの先頭から指定行を表示する

  :param str file: 対象ファイルパス
  :param int lines: 出力行数
  """
  with open(file, mode="r", encoding="utf8") as read_file:
    for i in range(0, lines):
      line = read_file.readline()
      if line == "":
        break;
      print(line.replace("\n", ""))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('lines', type=int)
  parser.add_argument('file')
  args = parser.parse_args()
  head(args.file, args.lines)

