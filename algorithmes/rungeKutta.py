
class RungeKutta:
    def __init__(self, a: int, b: int, h: float, alpha: int):
        self.a, self.b, self.h = a, b, h
        self.alpha = alpha
        self.approx = []

    def f(self, t, w):
        return (1 / t**2) - (w / t) - w**2
    
    def output(self, t, w):
        self.approx.append((t, w))

    def execute(self):
        N = int((self.b - self.a) / self.h)
        t = self.a
        w = self.alpha
        self.output(t, w)

        for i in range(1, N + 1):
            k1 = self.h * self.f(t, w)
            k2 = self.h * self.f(t + self.h / 2, w + k1 / 2)
            k3 = self.h * self.f(t + self.h / 2, w + k2 / 2)
            k4 = self.h * self.f(t + self.h, w + k3)
            w += (k1 + 2 * k2 + 2 * k3 + k4) / 6
            t = self.a + i * self.h
            self.output(t, w)
        return self.approx
