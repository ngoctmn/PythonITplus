class Film():
    def __init__(self, author, type):
        self.author = author
        self.type = type

    def show_info(self):
        print('Tac gia: ', self.author)
        print('Loai phim: ', self.type)
        