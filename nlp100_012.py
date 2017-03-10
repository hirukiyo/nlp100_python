# -*- coding: utf-8 -*-

"""
第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」の
タブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，
hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものを
col2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""


with open("data/hightemp.txt", encoding="utf8") as read_file:
  with open("out/col1.txt", mode="w", encoding="utf8") as write_file_1:
    with open("out/col2.txt", mode="w", encoding="utf8") as write_file_2:
      for line in read_file:
        cols = line.split("\t")
        write_file_1.write(cols[0] + "\n")
        write_file_2.write(cols[1] + "\n")
