import pso

# Fonksiyonumuzu oluşturduk
def Sphere(x):
    return sum(x**2)

# Problemi define ettik
problem = {
        'CostFunction': Sphere,
        'nVar': 10,
        'VarMin': -5,
        'VarMax': 5,
    }

pso.tic()
print('PSO Çalıştırılıyor ...')
gbest, pop = pso.PSO(problem, MaxIter = 100, PopSize = 55, c1 = 2, c2 = 2, w = 0.7, wdamp = 1.0)
print()
pso.toc()
print()

# Global Best Belirleme
print('Global Best:')
print(gbest)
print()
