# Competitive-programming
競技プログラミングのコードをまとめる

# online-judge-toolnのインストール
1. Pythonインストール
    - `$ sudo apt install python3`
    - `$ python3 --version`
2. pipインストール
    - `$ sudo apt install python3-pip`
    - `$ pip3 --version`
4. online-judge-tool
    - `$ pip3 install online-judge-tools`
    - `$ pip3 install --user online-judge-tools` 
    - `$ sudo pip3 install online-judge-tools`
    - `$ oj --version`

# Atcoder online-judge-toolの使い方
- ex ABC 256 - A の場合
```
# download testfile
$ oj dl https://atcoder.jp/contests/abc256/tasks/abc256_a

# test for python
$ oj t -c "python3 ./B.py"
```