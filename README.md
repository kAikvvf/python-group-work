# python-group-work
Git repository for python application group work in class.

# 問題データのプロトコル
- 行のインデックスが問題番号に一致
- 行の情報は次の情報にする。
> `(問題文 : str),(所要時間の目安[分] : int),(サンプルの数 : int ),(サンプル1 : list ),(サンプル2) ...,`
- サンプルのリストの中身を以下のようにする。しかし、"|" で区切る。
> `[(入力要素数 : int),(要素1 : tupple (要素 : str , type)),(要素2) ... ,(正しい回答 : str)]`

あとでプロトコルを ['title','topic','quest_state','estimated_time','samples'] に変更