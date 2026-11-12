"""
案例：
    演示张量点乘和矩阵乘法操作

点乘：
    要求：两个张量的维度必须相同
    API:
        t1*t2
        t1.mul(t2)

矩阵乘法：
    要求：两个张量的维度必须满足矩阵乘法的要求
    API:
        t1@t2
        t1.matmul(t2)
        t1.dot(t2) 只针对一维张量
"""
#导包
import torch

#1.定义函数,演示：张量点乘
def dm01():
    #1.创建两个张量,两行三列
    t1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
    print(f't1 :{t1},type:{type(t1)}')

    #2.创建两个张量,两行三列
    t2 = torch.tensor([[10, 20, 30], [40, 50, 60]])
    print(f't2 :{t2},type:{type(t2)}')

    #3.进行点乘操作
    result = t1 * t2
    print(f'点乘结果 :{result}')

    pass


#2.定义函数,演示：张量矩阵乘法
def dm02():
    #1.创建两个张量
    t1 = torch.tensor([[1, 2], [3, 4]])
    print(f't1 :{t1},type:{type(t1)}')

    t2 = torch.tensor([[5, 6], [7, 8]])
    print(f't2 :{t2},type:{type(t2)}')

    #2.进行矩阵乘法操作
    result = t1 @ t2
    print(f'矩阵乘法结果 :{result}')

#3.测试
if __name__ == '__main__':
    #dm01()
    dm02()
    pass