
class RungeKutta:
    def __init__(self, a: int, b: int, h: float, alpha: int):
        self.a = a
        self.b = b
        self.h = h
        self.alpha = alpha
        self.approx = []

    def f(self, t, w):
        return (1 / t**2) - (w / t) - w**2
    
    def output(self, t, w):
        self.approx.append((t, w))

    def execute(self):
        self.N = int((self.b - self.a) / self.h)
        self.t = self.a
        self.w = self.alpha
        self.output(self.t, self.w)

        for i in range(1, self.N + 1):
            k1 = self.h * self.f(self.t, self.w)
            k2 = self.h * self.f(self.t + self.h / 2, self.w + k1 / 2)
            k3 = self.h * self.f(self.t + self.h / 2, self.w + k2 / 2)
            k4 = self.h * self.f(self.t + self.h, self.w + k3)
            self.w += (k1 + 2 * k2 + 2 * k3 + k4) / 6
            self.t = self.a + i * self.h
            self.output(self.t, self.w)
        return self.approx
