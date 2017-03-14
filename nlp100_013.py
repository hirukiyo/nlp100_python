# -*- coding: utf-8 -*-

"""
第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」の
タブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，
hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目を
タブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""


# with open("data/hightemp.txt", encoding='utf8') as fp:
#   print(sum(1 for line in fp))

with open("data/col1.txt", mode="r", encoding="utf8") as read_file_1:
  with open("data/col2.txt", mode="r", encoding="utf8") as read_file_2:
    with open("out/013.txt",  mode="w", encoding="utf8") as write_file_1:
      while True:
        col1 = read_file_1.readline()
        col2 = read_file_2.readline()
        if len(col1) == 0 and len(col2) == 0:
          break
        write_file_1.write(
          col1.replace("\n", "") + "\t" + col2.replace("\n", "") + "\n")
