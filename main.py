from algorithmes.euler import Euler
from algorithmes.taylor import Taylor
from algorithmes.rungeKutta import RungeKutta
from math import exp


def afficher(approx):
    for t, w in approx:
        print(f"\tt: {t:.2f}\t\tw: {w:.6f}")


hs = [0.2, 0.1, 0.05]
y = exp(-5) + 5
print("\n--------------------------------------------------------------------------------------")
print("SUJET 1")
print("a) - Approximation de y(5) en utilisant l'algorithme d'EULER:")
for h in hs:
    print(f"h={h}:")
    euler = Euler(0, 5, h, 1)
    approx = euler.execute()
    afficher(approx)

print("b) - La valeur optimale de h en utilisant l'approximation y(5) assumer à 10^-6")
print(f"\tValeur actuelle de y(5) = {y}")
w = approx[-1][1]
h = 0.2
while (y - w) > 10**-6:
    h /= 2
    euler = Euler(0, 5, h, 1)
    approx = euler.execute()
    w = approx[-1][1]
    print(f"\tpour h: {h:.6f}\t\tw: {w:.6f}")
print(f"La valeur optimale de h est: {h:0.6f}")


print("\n--------------------------------------------------------------------------------------")
print("SUJET 2")
print("a) - Approximation de y en utilisant l'algorithme de TAYLOR d'ordre 2 avec h=0.1:") 
taylor = Taylor(0, 2, 0.1, 0)
approx = taylor.execute()
afficher(approx)

print("b) - Comparaison de celle-ci avec la valeur actuelle de y:")
t = 0
for i in range(0, 21):
    print(f"\tt: {t:.1f}\t\tw: {approx[i][1]:.6f}\t\ty({t:.1f}): {exp(-t) + t:.6f}")
    t += 0.1


print("\n--------------------------------------------------------------------------------------")
print("SUJET 3")
print("a) - Approximation de y en utilisant l'algorithme de RUNGE-KUTTA d'ordre 4 avec h=0.1:")
rungekutta = RungeKutta(1, 2, 0.1, -1)
approx = rungekutta.execute()
afficher(approx)

print("b) - Comparaison de celle-ci avec la valeur actuelle de y:")
t = 1
for i in range(0, 11):
    print(f"\tt: {t:.1f}\t\tw: {approx[i][1]:.6f}\t\ty({t:.1f}): {-1 / t:.6f}")
    t += 0.1