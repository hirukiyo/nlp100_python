# -*- coding: utf-8 -*-

"""
第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」の
タブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，
hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを
表示せよ．確認にはtailコマンドを用いよ．
"""
import argparse
import io


def tail(file, lines):
  """
  指定したファイルの末尾から指定行を表示する

  :param str file: 対象ファイルパス
  :param int lines: 出力行数
  """
  # with open(file, mode="r", encoding="utf8") as read_file:
  with open(file, mode="rb") as read_file:
    buf = b""
    line = 0
    size = read_file.seek(0, io.SEEK_END)
    for i in range(1, size):
      read_file.seek(-1 * i, io.SEEK_END)
      b = read_file.read(1)
      if b == b"\n":
        print(buf.decode('utf8'))
        buf = b""
        line += 1
        if line >= lines:
          break
      elif b != b"\r":
        buf = b + buf


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('lines', type=int)
  parser.add_argument('file')
  args = parser.parse_args()
  tail(args.file, args.lines)

