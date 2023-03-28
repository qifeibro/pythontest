class Phone:
    IMEI = None         # 序列号
    producer = "ITCAST" # 厂商

    def call_by_5g(self):
        print("父类的5g通话")

class MyPhone(Phone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        # 方法1调用父类成员
        print(f"父类的品牌是: {Phone.producer}")
        Phone.call_by_5g(self)
        
        # 方法2调用父类成员
        print(f"父类的品牌是: {super().producer}")
        # super().call_by_5g()
        
        print("子类的5g通话")

phone = MyPhone()
Phone.call_by_5g(self=MyPhone)  # 父类的5g通话
Phone.call_by_5g(self=Phone)    # 父类的5g通话
print(Phone.producer)           # ITCAST
MyPhone.call_by_5g(self=MyPhone)
# MyPhone.call_by_5g(self=Phone)
print("*********")
phone.call_by_5g()
print("*********")
print(phone.producer)           # ITHEIMA
print(MyPhone.producer)         # ITHEIMA
