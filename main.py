# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi("12")
    a = 7
    print(a)
    minute = 60
    hour = 60
    result = minute * hour
    print("一小时时长："+str(result))
    seconds_per_hour = result * 24
    print("一天有多少秒："+str(seconds_per_hour))

    # 列表[]
    weekdays = ["Monday", "Tuesday", "Wednesday"]
    print("日期："+str(weekdays))
    birthday = "1/2/1995"
    day = birthday.split("/")
    print("日期："+str(day))
    a1 = ["1", "2", "3"]
    a2 = ["11", "12", "13"]
    a3 = ["21", "22", "23"]
    a = [a1, a2, a3]
    print("列表中的列表："+str(a))
    print("a1中的列表元素："+str(a1))
    a1.append("5")
    print("追加后a1的列表元素："+str(a1))
    a1.extend(a2)
    print("合并列表："+str(a1))

    # 元组()
    t = ("a", "b", "c")
    print("元组元素："+str(t))

    # 字典{}
    dict = {"name": "kit", "age": "7"}
    print("字典："+str(dict))
    print("字典的键："+str(dict.keys()))

    # 集合{}
    numbers = {"1", "2", "3"}
    print("集合："+str(numbers))

    # 代码结构
    # if/else应用
    disaster = True
    if disaster:
        print("yes")
    else:
        print("no")

    furry = False
    small = True
    if furry:
        if small:
            print("furry is True, small is True.")
        else:
            print("furry is True, small is False.")
    else:
        if small:
            print("furry is False, small is True")
        else:
            print("furry is False, small is False.")

    # elif应用
    color = "pure"
    if color == "red":
        print("it's red")
    elif color == "blue":
        print("it's blue")
    elif color == "pure":
        print("it's pure")
    else:
        print("I have never heard of the color")

    # while循环应用
    count = 1
    while count <= 5:
        print(count)
        count += 1

    # for迭代应用
    names = ["peter", "cat", "tom"]
    for name in names:
        print(name)

    number_list = list(range(1, 6))
    print(number_list)

    # 函数的应用
    def make_a_sound():
        print("quite")
    make_a_sound()

    def agree():
        return True
    if agree():
        print("it's agree.")
    else:
        print("it's disagree.")

    def answer():
        print(42)

    def run_something(func):
        func()
    run_something(answer)

    animal = "fruitbat"

    def print_global():
        print("inside print_global:", animal)

    print_global()

    def change_and_print_global():
        global animal
        animal = "wombat"
        print("inside change_and_print_global:", animal)

    change_and_print_global()
    print_global()

    # 异常处理
    short_list = [1, 2, 3]
    position = 5
    try:
        short_list[position]
    except:
        print("exception")

    print(sum(range(1, 101)))

    # 生成器
    def my_range(first=0, last=10, step=1):
        number = first
        while number < last:
            yield number
            number += step

    ranger = my_range(1, 5, 2)
    for x in ranger:
        print(x)

    # 命名空间和作用域
    animal = "fruitbat"
    def change_local():
        animal = "wombat"
        print("local", locals())

    change_local()
    print(animal)
    print("globals:", globals())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
