# FactCheckSentenceNLI-FCSNLI-
本データセットはファクトチェック支援を想定した含意関係認識システムの訓練・評価を目的に構築したデータセットです。

データセットはtsv形式で、各行はタブ区切りで
- \<index>
- <gold_label (正解ラベル)>
- <sentence1 (前提文・リソース文)>
- <sentence2 (仮説文・疑義言説文)>

で構成されています。

```
1	contradiction	茶色 の ドレス を 着た 女性 が ベンチ に 座って い ます 。	女性 が 畑 で 踊って い ます 。
```
本データセットの訓練データは```train```ディレクトリ内の3つのデータセットから構成されます。
```jsnli_train.tsv```は[JSNLI](http://nlp.ist.i.kyoto-u.ac.jp/index.php?%E6%97%A5%E6%9C%AC%E8%AA%9ESNLI%28JSNLI%29%E3%83%87%E3%83%BC%E3%82%BF%E3%82%BB%E3%83%83%E3%83%88)
の訓練データを使用しており、
```unrelated_dataset.tsv```はJSNLIの訓練データと[livedoorニュースコーパス](https://www.rondhuit.com/download.html#ldcc) を基に構築しています。

### 使用方法
以下のように結合したいトレーニングデータを指定してご利用ください。3つ以上のファイルでも結合可能です。
indexは自動で正規化されます。
 
(入力するデータは、上述の形式に準じます。)
 
```$ python merge_training_dataset.py [file1.tsv] [file2.tsv]```
 
 
## ライセンス
このデータセットのライセンスはJSNLIと同じく[CC BY-SA 4.0 ](https://creativecommons.org/licenses/by-sa/4.0/) に従います。
 
 
## 参考文献
栗原 健太郎, 河原 大輔: ファクトチェック支援のための含意関係認識システム, 言語処理学会第27回年次大会(NLP2021), (2021.3).
