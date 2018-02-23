

print ("请输入销售额")

# class K1(object):
#     def foo(self):
#         print ("K1-foo")
# class K2(object):
#     def foo(self):
#         print ("K2-foo")
#     def bar(self):
#         print ("K2-bar")
# class K3(object):
#     def foo(self):
#         print ("K3-foo")
# class K4(object):
#     def foo(self):
#         print ("K4-foo")
#     def bar(self):
#         print ("K4-bar")

# class J1(K1, K2):
#     pass
# class J2(K3, K4):
#     def bar(self):
#         print ("J2-bar")



# class C(J1, J2):
#     pass
# c=J2()
# print(isinstance(c,K3))
# # if __name__ == "__main__":
# #     print (C.__mro__ )
# m = C()
# m.foo()
# m.bar()






# coding=utf-8
# __metaclass__ = type
# class StaticMethod:
#     @staticmethod
#     def foo():
#         print ("This is static method foo().")
# class ClassMethod:
#     @classmethod
#     def bar(cls):
#         print ("This is class method bar().")
#         print ("bar() is part of class:", cls.__name__)

# if __name__ == "__main__":
#     static_foo = StaticMethod()
#     #实例化
#     static_foo.foo()
#     #实例调用静态方法
#     StaticMethod.foo()
#     #通过类来调用静态方法
#     print ("********")
#     class_bar = ClassMethod()
#     class_bar.bar()
#     ClassMethod.bar()


# class Spring():
#     season = "this is spring"
#     def tree(self,x):
#         self.x=x
#         return self.x
#     def wind(y):
#         season=y

# # print(Spring.__dict__)
# # print(Spring.__dict__['season'])
# spring=Spring()

# print(spring.season)
# print(spring.__dict__)
# spring.season = "that is spring!"
# # del spring.season
# print(spring.__dict__)
# # print(spring.season)
# Spring.flower="peach"
# print(Spring.__dict__)


# class Spring():
#     __slots__ =("tree","flower")
# class Summer(Spring):
#     pass
# print(dir(Spring))
# print(dir(Summer))
# print(dir(object))
# print(Spring.__slots__)
# t=Spring()
# print(t.__slots__)
# # print(dir(t.__dict__))
# # Spring.flower="mulberrybush"
# # print(Spring.tree)
# # t=Spring()
# # t.tree="willow" #不允许再赋值
# # t.flower="water lily"
# t.tree=tree2
# print(t.tree())



# class A():
#     def __getattr__(self,name):
#         print( "getattr")
#     def __setattr__(self,name,value):
#         print ("setattr")
#         self.__dict__[name]=value
#     # def __getattribute__(self,name):
#         # print ("__getattribute")
#         # return self.__getattribute__(self,name)

# a=A()
# # a.x=5
# # print (a.x)
# print(dir(a))
# print(a.__dict__)
