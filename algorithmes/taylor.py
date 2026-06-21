from math import sin, cos

class Taylor:
    def __init__(self, a: int, b: int, h: float, alpha: int):
        self.a = a
        self.b = b
        self.h = h
        self.alpha = alpha
        self.approx = []

    def f(self, t, w):
        return 1 + t * sin(t * w)
    
    def fprime(self, t, w):
        return sin(t * w) + t * (w + t * self.f(t, w)) * cos(t * w)
    
    def T(self, t, w):
        return self.f(t, w) + (self.h / 2) * self.fprime(t, w)

    def output(self, t, w):
        self.approx.append((t, w))

    def execute(self):
        self.N = int((self.b - self.a) / self.h)
        self.t = self.a
        self.w = self.alpha
        self.output(self.t, self.w)
        for i in range(1, self.N + 1):
            self.w += self.h * self.T(self.t, self.w)
            self.t = self.a + i * self.h
            self.output(self.t, self.w)
        return self.approx
