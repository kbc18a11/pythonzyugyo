class NetTester:
    def __init__(self):
        self.cnt = 0
        print('通信テスターを作成しました')

    def Send(self):
        print('データを送信しました')
        self.cnt += 1

    def __enter__(self):
        print('接続を開始します')
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        print(f'接続を終了します 通信数{self.cnt}')

    def __del__(self):
        print('通信テスターを開放します')


with NetTester() as net:
    net.Send()
    net.Send()
