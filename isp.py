# インタフェース分離の原則(Interface Segregation Principle)の効能を感じるためのデモ

# クライアント（iPhone, Macbook）にのバックエンド処理（OS アップデートなど）があるが，
# クライアントごとにインタフェースを作成しよう。
# iPhone が使わないメソッド(change_keytype(), update_osx)は，インタフェースに含めるべきではない

# ❌ ISP に違反するインタフェース
class DeviceManager:
    def __init__(self):
        pass

    # iPhone の OS バージョンアップデート用
    def update_ios(self):
        pass

    # Macbook の OS バージョンアップデート用 
    def update_osx(self):
        pass

    # Macbook の キータイプ変更用
    def change_keytype(self):
        pass

# ✅ 以下の2クラスは ISP に合致するインタフェース
class iPhoneManger:
    def __init__(self):
        pass

    def update_ios(self):
        pass

class MacbookManager:
    def __init__(self):
        pass

    def update_osx(self):
        pass

    def change_keytype(self):
        pass

if __name__ == '__main__':
    # ❌ iPhone, Macbook は異なるクライアントなのに同じインタフェース使ってる
    iphone_dm = DeviceManager()
    macbook_dm = DeviceManager()

    iphone_dm.update_ios()
    macbook_dm.update_osx()

    # ✅ クライアントそれぞれにインタフェースを持たせて疎結合に
    iphone_dm = iPhoneManger()
    macbook_dm = MacbookManager()

    iphone_dm.update_ios()
    macbook_dm.update_osx()