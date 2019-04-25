class A: pass


class B: pass


class C: pass


class M(A,B): pass


class N(B,C): pass


class K(N,M,C): pass


print(K.mro())
