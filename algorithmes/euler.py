
class Euler:
    def __init__(self, a: int, b: int, h: float, alpha: int):
        self.a = a
        self.b = b
        self.h = h
        self.alpha = alpha
        self.approx = []
    
    def f(self, t, w):
        return -w + t + 1

    def output(self, t, w):
        self.approx.append((t, w))

    def execute(self):
        self.N = int((self.b - self.a) / self.h)
        self.t = self.a
        self.w = self.alpha
        self.output(self.t, self.w)
        for i in range(1, self.N + 1):
            self.w += self.h * self.f(self.t, self.w)
            self.t = self.a + i * self.h
            self.output(self.t, self.w)
        return self.approx
            