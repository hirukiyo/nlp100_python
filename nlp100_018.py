# -*- coding: utf-8 -*-

"""
第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」の
タブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，
hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ．
（注意: 各行の内容は変更せずに並び替えよ）
確認にはsortコマンドを用いよ
（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

with open("data/hightemp.txt", encoding='utf8') as read_file:
  lines = [line.replace("\n", "").split("\t") for line in read_file]
  sorted_lines = sorted(lines, key=lambda line: float(line[2]), reverse=True)
  for line in sorted_lines:
    print("\t".join(line))
