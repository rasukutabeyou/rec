# rec
企業提出用

## DPマッチングを用いた音声認識
- 動的帰納法を用いた音声認識、正解データと一致する確率が最も高いデータを出力します。
- `DP_matching.py`,`DPmatching_back.py`が実装。
- `city011`,`city012`,`city021`,`cityo22`は音声データを整列させたものです。
　それぞれ百単語の音声が格納されています。
- `resualt`には認識結果が格納されています。

## 実行
- `DP_matching.py`,`DPmatching_back.py`が実装、`python`を用いて」実行してください。
- 実行例
```
$python DP_matching.py
////////////////////
city011_095.txt
city012_095.txt
////////////////////
city011_096.txt
city012_096.txt
////////////////////
city011_097.txt
city012_097.txt
////////////////////
city011_098.txt
city012_098.txt
////////////////////
city011_099.txt
city012_099.txt
////////////////////
city011_100.txt
city012_100.txt
////////////////////
認識確率は 97 %
```


© 2025 Kouta Sakai
