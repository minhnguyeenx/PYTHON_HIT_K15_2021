from functools import reduce

def MyMathShower(*args):
    '''
    :param:
    input:
        nhập 1 mảng tham số tùy ý
    output:
        tổng, tích, hiệu của mảng tham số
    '''
    return sum(args), reduce((lambda x, y: x*y), args), reduce((lambda x, y: x - y), args)

a = list(map(float, input().split()))
print(MyMathShower(*a))