# Single Responsibility Principles の効能を示すデモ
from abc import ABC, abstractmethod

# デバイス情報取得のためのインタフェースの抽象基底クラス
class DeviceInfoFetcher(ABC):
    @abstractmethod
    def get_name(self):
        pass

    def get_version(self):
        pass

    def get_color(self):
        pass

class iPhone(DeviceInfoFetcher):
    def __init__(self, name: str, version: str, color: str):
        self.name = name
        self.version = version
        self.color = color

    def get_name(self):
        return self.name

    def get_version(self):
        return self.version

    def get_color(self):
        return self.color

class Macbook(DeviceInfoFetcher):
    def __init__(self, name: str, version: str, color: str, keytype: str):
        self.name = name
        self.version = version
        self.color = color
        self.keytype = keytype # e.g. JIS, US

    def get_name(self):
        return self.name

    def get_version(self):
        return self.version
    
    def get_color(self):
        return self.color

    def get_keytype(self):
        return self.keytype

# デバイス情報表示モジュール
class DeviceInfo():
    def __init__(self, device_info_fetcher: DeviceInfoFetcher):
        self.dif = device_info_fetcher
    
    # デバイス情報を表示する
    def print_device_info(self):
        print(
            f'name: {self.dif.get_name()},\t'\
            f'ver: {self.dif.get_version()},\t'\
            f'color: {self.dif.get_color()}'
        )

if __name__ == '__main__':
    # デバイスのインスタンス化
    my_iphone =  iPhone(name='ken_iPhone', version='11.0.1', color='red')
    my_macbook = Macbook(name='ken_macbook', version='10.4', color='space_gray', keytype='US')

    # インタフェースのインスタンス化
    dif_iphone = DeviceInfo(my_iphone)
    dif_macbook = DeviceInfo(my_macbook)

    # インタフェースの利用
    dif_iphone.print_device_info()
    dif_macbook.print_device_info()