import math

def C(n, k):
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))


class Solver:

    def __init__(self, a, b, n):
        assert a > 0 and a < 1 and b > 0 and b < 1 and n >= 1
        self.a = a
        self.b = b
        self.inA = 1 - a
        self.inB = 1 - b
        self.n = n
        self.count = 0
        self.q = [None for i in range(n+1)]
        self.q[n] = 1
    # -------------------------1st----------------------------
    def calc_pij(self, i, j):
        if j == 0:
            return self.inA*self.b**i
        elif j == i+1 and i < self.n:
            return self.a*self.inB**i
        elif i == self.n and j == self.n:
            return self.inB**self.n + self.a*C(self.n, 1)*self.inB**(self.n-1)*self.b
        else:
            return self.inA*C(i, j)*(self.inB**j)*self.b**(i-j) + self.a * C(i, j-1) * (self.inB**(j-1))*self.b**(i-j+1)

    def calc_Pij(self, i, j):
        res = 0
        if i >= 1 and i <= self.n and j >= 0 and j <= i-1:
            for k in range(0, j+1):
                res += self.calc_pij(i, k)
            return res

    def calc_qi(self, i):
        self.count+=1
        if self.q[i]:
            return self.q[i]
        else:
            tmp = 0
            for j in range(i+1, self.n+1):
                tmp += self.calc_qi(j)*self.calc_Pij(j, i)
            self.q[i] = tmp/self.calc_pij(i, i+1)
            return self.q[i]

    def calc_pi(self, i):
        assert i >= 0 and i <= self.n
        if i == self.n:
            tmp = 0
            for k in range(0, self.n):
                tmp += self.calc_qi(k)
            return 1/(1+tmp)
        else:
            return self.calc_pi(self.n) * self.calc_qi(i)

    def calc_pxji(self, j, i):
        return C(j, i) * self.inB**i * self.b**(j-i)

    def calc_pxi(self, i):
        sum = 0
        for j in range(i, self.n+1):
            sum += self.calc_pi(j)*self.calc_pxji(j, i)
        return sum
