# -*- coding: utf-8 -*-

"""
第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」の
タブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，
hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""

with open("data/hightemp.txt", encoding='utf8') as read_file:
  lines = [line.replace("\n", "").split("\t") for line in read_file]
  col1_counts = {}
  for line in lines:
    if line[0] in col1_counts:
      col1_counts[line[0]] += 1
    else:
      col1_counts[line[0]] = 1
  print(col1_counts)
  sorted_lines1 = sorted(lines, key=lambda line: line[0], reverse=True)
  sorted_lines2 = sorted(
    sorted_lines1, key=lambda line: col1_counts[line[0]], reverse=True)
  for line in sorted_lines2:
     print("\t".join(line))
