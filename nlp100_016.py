# -*- coding: utf-8 -*-

"""
第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」の
タブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，
hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位で
N分割せよ．同様の処理をsplitコマンドで実現せよ．
"""
import argparse
import os
import math


def split(file, n):
  """
  指定したファイルを行単位でN分割する

  :param str file: 対象ファイルパス
  :param int n: 分割数
  """
  with open(file, mode="r", encoding="utf8") as read_file:
    # read_fileを行で一旦全部読み込み総行数を取得
    total_line = 0
    for line in read_file:
      total_line += 1
    line_count = math.ceil(total_line / n)

    # 生成するファイル名情報
    name, ext = os.path.splitext(os.path.basename(file))

    # ファイル分割開始
    read_file.seek(0)
    for i in range(n):
      output_file_path = "out/{0}_{1:03d}{2}".format(name, i, ext)
      with open(output_file_path, mode="w", encoding="utf8") as write_file:
        for j in range(line_count):
          line = read_file.readline()
          if line == "":
            break
          write_file.write(line)
    return

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('n', type=int)
  parser.add_argument('file')
  args = parser.parse_args()
  split(args.file, args.n)

