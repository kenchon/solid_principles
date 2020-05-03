# リスコフの置換原則（Liskov's Substitution Principles）の効能を感じるためのデモ

# 抽象クラスで (log_message, date) を引数にとるログ出力機能を宣言。
# iPhone クラスは辞書型を引数にとるため LSP 違反
# Macbook クラスは OK

# 抽象クラス
class device:
    def __init__(self, version:str, color:str):
        pass
    
    def push_log(self, log_message:str, date:str):
        print(f"{date}: {log_message}")

# 派生クラス（LSP違反）
class iPhone(device):
    def __init__(self, version:str, color:str):
        self.version = version
        self.color = color

    # LSPに違反するメソッド。抽象クラスと異なる引数を持つため
    def push_log(self, log_json:dict):
        print(f"{log_json['date']}: {log_json['log_message']}")

# 派生クラス（LSP合致）
class Macbook(device):
    def __init__(self, version:str, color:str):
        self.version = version
        self.color = color

    # LSP合致。派生型の振る舞い
    def push_log(self, log_message:str, date:str):
        print(f"{date}: Macbook {log_message}")

# LSP違反クラス，LSP合致クラスの動作確認
if __name__ == '__main__':
    # LSP違反
    my_iphone = iPhone(version='11.0.0', color='black')
    log_json = {'date': '2020/04/20', 'log_message': 'iPhone started'}
    my_iphone.push_log(log_json)

    # LSP合致
    my_macbook = Macbook(version='10.0.0', color='gray')
    my_macbook.push_log(date='2020/04/21', log_message='macbook started')