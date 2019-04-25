# Tạo lớp English có hàm greting()
class English:
    def greeting(self):
        print ("Hello!")


# Tạo lớp Vietnamese cũng có hàm greting()
class Vietnamese:
    def greeting(self):
        print ("Xin chao!")
# Tạo hàm showIntro để hiển thị lời chào


def show_intro(language):
    language.greeting()

# Khởi tạo 2 đối tượng tương ứng với English và Vietnamese
en = English()
vn = Vietnamese()

# Gọi đến 2 hàm showIntro của 2 đối tượng Enlish và Vietnamese
show_intro(en)
show_intro(vn)

