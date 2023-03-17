"""
面向对象封装特性课后习题第49页
设计带有私有成员的手机
"""

class Phone:
    """
    设计一个类，用来描述手机
    """
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭, 使用4g网络")

    def call_by_5g(self):
        """
        提供公开成员方法: call_by_5g()
        """
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
