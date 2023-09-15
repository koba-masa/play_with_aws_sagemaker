# モデル

## 制約
- 同じ名称を付与することはできない(更新することができない)

## 圧縮形式
- `.tar.gz`

## コンテナへの反映
### 反映のタイミング
- `エンドポイントの設定`の変更を行なったタイミングで、反映される
  - S3に配置したモデルアーティファクトを更新しても、反映されない。必ず、`エンドポイントの設定`の変更が必要となる

### コンテナ上での展開先
- `/opt/ml/model`

#### 例
```sh
% ls -l sample
total 16
-rw-r--r--@ 1 koba-masa  staff  5  8  9 14:07 model.vec
-rw-r--r--@ 1 koba-masa  staff  5  8  9 14:07 model2.vec

% tar czf sample.tar.gz sample
```
上記のディレクトリ構造と手順で圧縮した場合、以下のように展開される
- `/opt/ml/model/model.vec`
- `/opt/ml/model/model2.vec`
