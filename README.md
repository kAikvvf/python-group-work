# python-TechFul
> 2025年前期 情報処理 アプリ開発課題

## プログラムの内容
- app.py
    > このファイルを実行することでアプリが立ち上がる。
- scripts/loginPad.py
    > ログインの処理をしている。
- scripts/main.py
    > ログインした後にアプリを立ち上げるプログラム。
- scripts/revenge.py
    > 問題のリストを表示するプログラム。この中の処理で問題を解くページを開いたり、回答状況を確認したりできる。
- scripts/kotone.py
    > 問題を解くページのプログラムをまとめている。タブの切り替えの処理をしている。
- scripts/samplePage.py
    > 実行時にサンプルケース・模範解答・実行結果を表示するプログラム。kotone.py 内で使用。
- scripts/scoringPage.py
    > 採点時のサンプルケースごとの正誤の表示・すべてのサンプルケースが正解の時のスコア計算と表示をするプログラム。kotone.py 内で使用。
- scripts/prompt.py
    > エディターのプログラム。デバッグ・実行結果取得・シンタックスハイライトを主にしている。
- scripts/questDataHandler.py
    > 問題のデータのハンドラ。関数で問題文・サンプルケース・模範解答などが抽出できる
- scripts/userDataHandler.py
    > ユーザーの回答状況などを抽出するハンドラ。
- scripts/run_temp/runProg{n}.py
    > サンプル実行時に n 番目のサンプルケースでの実行プルグラムを格納。
- scripts/debugTerminal.txt
    > sys でこのファイルにターミナルを移して実行している。
- data/questDict.csv
    > 問題のデータを保存してあるファイル。
- data/.user-list.txt
    > ユーザーのユーザー名とパスワードを保存してあるファイル。
- data/.{username}.csv
    > ユーザー名ごとの回答状況を保存するファイル。
- scripts/questMaker.py
    > 問題を作成するプログラム。実行時に出てくるウィンドウに問題文・サンプルケースなどを記入後、模範のプログラムを書いて実行。もし実行結果があっていれば、書き込み。書き込み先は 'data/questDict.csv'