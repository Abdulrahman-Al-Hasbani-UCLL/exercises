# Write your code here
from abc import ABC, abstractmethod

class A(ABC):
    def a(self):
        self.b()

    def e(self):
        self.c()

    @abstractmethod
    def b():
        ...
    @abstractmethod
    def c():
        ...

class B(A):
    def b(self):
        self.a()

    def c(self):
        self.e()

class C(B):
    def f(self):
        pass

class F(ABC):
    def a(self):
        self.b()
        self.f()
    
    @abstractmethod
    def b():
        ...
    @abstractmethod
    def f():
        ...


class D(A):
    def b(self):
        self.f()
        
    @abstractmethod
    def f():
        ...


class E(D):
    def c(self):
        self.a()

    def f(self):
        self.e()

    def g(self):
        self.f()
