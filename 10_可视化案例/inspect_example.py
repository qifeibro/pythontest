"""
使用 inspect 模块可以检查函数的签名, 并获取参数的信息。
下面是一个演示如何使用 inspect 模块查看函数参数类型的示例
"""
import inspect

def my_function(x, y, z="hello", *args, **kwargs):
    pass

signature = inspect.signature(my_function)

# 打印参数类型
for param in signature.parameters.values():
    print(param.name, param.annotation)

def my_function1(x: int, y: float, z: str="hello", *args: tuple, **kwargs: dict) -> bool:
    pass

signature = inspect.signature(my_function1)

# 打印参数类型
for param in signature.parameters.values():
    print(param.name, param.annotation)