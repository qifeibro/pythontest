import json

var_1 = json.loads('{"name": "zhangsan"}')  # type: dict[str, str]

def func():
    return 10

var_2 = func()  # type: int