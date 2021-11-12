# Minicondaの使い方

作成日：February 21th, 2021  
更新日：-

---
## 目次
[インストール](#インストール)  
[仮想環境の使用方法](#仮想環境の使用方法)  
[condaコマンドの使用方法](#condaコマンドの使用方法)  
[リンク](#リンク)  

---
## インストール

### Windows10
step1. [Miniconda official](https://docs.conda.io/en/latest/miniconda.html)から**Windows installers**からEXEファイルをダウンロード.

step2. デフォルト設定でインストール。

step3. スタートメニューのAnaconda(64-bit) -> Anaconda Prompt (miniconda3)から  コマンドプロンプトを起動.

step4. 初期化コマンドを実行.
```sh
conda init
```

step5. PowerShellからcondaを利用するためにスクリプト実行許可を与える.PowerShellプロンプトから以下を実行.

```PowerShell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```


### Ubuntu
step1. [Miniconda official](https://docs.conda.io/en/latest/miniconda.html)から**Linux installers**から.shファイルをダウンロード。

step2. ダウンロードしたファイルを実行。基本はすべてYES.
```sh
bash Miniconda3-latest-Linux-x86_64.sh
```

step3. 端末起動時に自動で仮想環境に入らないようにする.
```sh
conda config --set auto_activate_base false
```

仮想環境の有効化
```sh
$ conda activate <name>
```

---
## 仮想環境の使用方法

### 仮想環境のリスト
```sh
$ conda info -e
```

### 仮想環境の有効化
```
$ conda activate <name>
```

### 仮想環境の終了
```
$ conda deactivate
```

### 仮想環境の作成
```
$ conda create -n <name> python=<version>
```

### 仮想環境の削除
```
$ conda remove -n <name> --all
```


### 仮想環境のエクスポート
```
$ conda env export > env.yaml
```

### 仮想環境のインポート
```sh
$ conda env create -f env.yaml
```

---
## condaコマンドの使用方法

### condaのアップグレード

```sh
$ conda update conda
```

### インストールされているパッケージの表示
```
$ conda list
```

### パッケージの検索
```
$ conda search <keyword>
```

### パッケージ情報の表示
```
$ conda search -i <package>
```

### パッケージのインストール
```
$ conda install <package>
```

```
$ conda install <package>=<version>
```


### パッケージのインストール(仮想環境を指定)
```
$ conda install -n <name> <package>
```

### パッケージのアップデート
```
$ conda update <package>
```

### 全てのパッケージのアップデート
```
$ conda update --all
```

### パッケージのアンインストール
```
$ conda remove <package>
```

### 不要なパッケージやキャッシュを削除
```
$ conda clean --all
```

---
## リンク
[Miniconda official](https://docs.conda.io/en/latest/miniconda.html)
