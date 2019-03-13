from lab2 import C

class Solver2:

    def __init__(self, a, b, n, r):
        assert 0 < a < 1 and 0 < b < 1 <= n and r >= 1
        self.a = a
        self.b = b
        self.inA = 1 - a
        self.inB = 1 - b
        self.n = n
        self.r = r
        self.R = n + r
        self.count = 0
        self.q = [None for i in range(n+r+1)]
        self.q[n+r] = 1

    # -------------------------1st----------------------------

    def calc_pij(self, i, j):

        if i == j == self.R:
            return self.inB**self.n + self.a*self.n*self.inB**(self.n-1)*self.b
        elif j == i+1 and self.n <= i <= self.R-1:
            return self.a*self.inB**self.n
        elif i - self.n + 1 <= j <= min(i, self.R-1) and self.n <= i <= self.R:
            return self.inA*C(self.n, i-j)*self.inB**(self.n-i+j)*self.b**(i-j) + self.a*C(self.n, i-j+1)*self.inB**(self.n-i+j-1)*self.b**(i-j+1)
        elif self.n <= i <= self.R and j == i - self.n:
            return self.inA*self.b**self.n
        elif 0 <= i <= self.n - 1 and j == i + 1:
            return self.a*self.inB**i
        elif self.n - 1 >= i >= 0 == j:
            return self.inA*self.b**i
        elif 1 <= i <= self.n - 1 and 1 <= j <= i:
            return self.inA*C(i, j)*self.inB**j*self.b**(i-j) + self.a*C(i, j-1)*self.inB**(j-1)*self.b**(i-j+1)

    def calc_qi(self, i):
        if self.q[i]:
            if self.r >= i >= 1:
                summ = 0
                for j in range(i+1, i+self.n+1):
                    summ += self.calc_pij(j, i)*self.calc_qi(j)
                self.q[i-1] = ((1 - self.calc_pij(i, i))*self.q[i] - summ) / self.calc_pij(i-1, i)
            elif self.R >= i >= self.r+1:
                summ = 0
                for j in range(i+1, self.R+1):
                    summ += self.calc_pij(j, i)*self.calc_qi(j)
                self.q[i-1] = ((1 - self.calc_pij(i, i))*self.q[i] - summ) / self.calc_pij(i-1, i)
            return self.q[i]
        else:
            self.calc_qi(i+1)
            return self.calc_qi(i)

    def calc_pi(self, i):
        if i == self.R:
            summ = 0
            for k in range(0, self.R):
                summ += self.calc_qi(k)
            return 1 / (1 + summ)
        else:
            return self.calc_pi(self.R)*self.calc_qi(i)
