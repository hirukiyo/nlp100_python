# -*- coding: utf-8 -*-

"""
第3章: 正規表現

Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gz
がある．

1行に1記事の情報がJSON形式で格納される
各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納
され，そのオブジェクトがJSON形式で書き出される
ファイル全体はgzipで圧縮される
以下の処理を行うプログラムを作成せよ．

22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""
import json
import re


def get_uk_record():
  with open("data/jawiki-country.json", encoding='utf8') as read_file:
    records = [json.loads(line, encoding='utf8') for line in read_file]
  uk_records = [record for record in records if record["title"] == "イギリス"]
  return uk_records[0]


def main():
  uk_record = get_uk_record()
  pattern = re.compile(r'\[\[Category:(.*)\]\]')
  matches = pattern.findall(uk_record["text"])
  print(*matches, sep="\n")


if __name__ == '__main__':
  main()
