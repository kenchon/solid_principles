# Single Responsibility Principles の効能を示すデモ
class iPhone:
    def __init__(self, version: str, color: str):
        self.version = version
        self.color = color

    def get_version(self):
        return self.version

    def get_color(self):
        return self.color

    # ログを送信する
    def push_log(self, log_message: str):
        print(f'MSG: {log_message},\t VER: {self.version}')

# ログ管理のためのクラス
class Logger:
    def __init__(self, device: iPhone):
        self.device = device
    
    # ログを送信する。
    def push_log(self, log_message: str):
        print(f'MSG: {log_message},\t VER: {self.device.version}')

if __name__ == '__main__':
    device = iPhone(version='11.0.0', color='red')
    device.push_log(log_message='Device Started w/o SRP')

    logger = Logger(device)
    logger.push_log(log_message='Device Started w/ SRP')