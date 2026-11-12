"""
案例：
    演示PyTorch中如何创建线性和随机张量.

涉及到的函数：
    torch.arange() 和 torch.linspace()函数可以创建线性张量
    torch.initial_seed() 和 torch.manual_seed()函数可以设置随机种子
    torch.rand() 和 torch.randn()函数可以创建随机浮点类型张量
    torch.randint(low,high,size=())函数可以创建随机整数类型张量

要掌握的函数：
    arrange(),linspace(),manual_seed(),randint()
"""

#导包
import torch

#1.定义函数,演示：创建线性张量.
def dm01():
    #场景1：创建指定范围的线性张量
    #参1：起始值
    #参2：终止值
    #参3：步长
    t1 = torch.arange(0,10,2)
    print(f't1:{t1},type:{type(t1)}')
    print('-'*30)

    #场景2：创建指定范围的线性张量->等差数列
    #参1：起始值
    #参2：终止值
    #参3：元素个数
    t2 = torch.linspace(0,10,5)
    print(f't2:{t2},type:{type(t2)}')

#2.定义函数,演示：创建随机张量.
def dm02():
    # step1：设置随机种子
    torch.manual_seed(42)
    print(f'当前随机种子：{torch.initial_seed()}')

    # step2：创建随机浮点张量
    t3 = torch.rand(3, 4)
    t4 = torch.randn(3, 4)
    print(f't3:{t3},type:{type(t3)}')
    print(f't4:{t4},type:{type(t4)}')
    print('-' * 30)

    # step3：创建随机整数张量
    t5 = torch.randint(0, 10, (3, 4))
    print(f't5:{t5},type:{type(t5)}')

#3.测试函数.
if __name__ == '__main__':
    #创建线性张量
    #dm01()
    #创建随机张量
    dm02()