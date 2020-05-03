# Single Responsibility Principles の効能を感じるためのデモ
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
    # SRP 使わない場合: iPhone クラスの push_log で ログ送信。
    device = iPhone(version='11.0.0', color='red')
    device.push_log(log_message='Device Started w/o SRP')

    # SRP 使う場合: Logger クラスの push_log でログ送信。iPhone と Logger は独立
    device = iPhone(version='11.0.0', color='red')
    logger = Logger(device)
    logger.push_log(log_message='Device Started w/ SRP')