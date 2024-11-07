

# def count_calls(func):
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         # print(f'Функция {func.__name__} была вызвана {wrapper.calls} раз(а)')
#         return func(*args, **kwargs)
#     wrapper.calls = 0
#     return wrapper

def log_func_use(functor):
    def decorate(val):
        print('func is called')
        #functor()
        result = functor(val)
        print(f'func is done. Result {result}')
        return result
    return decorate

@log_func_use
def inc(old_value):
    return old_value + 1


def main():
    exp = 6
    print(exp)
    # log_func_use(inc)(exp)
    # #exp = inc(exp)
    # print(exp)
    # exp = log_func_use(inc)(exp)
    exp = inc(exp)
    print(exp)


if __name__ == '__main__':
    main()


