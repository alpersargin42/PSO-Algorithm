import numpy as np
import time
import math


def PSO(problem,
        MaxIter=100,#iterasyon
        PopSize=100,#populasyon aralığı
        swarm_size=10, #değer aralığı
        c1=2,#bilişsel bileşen sabiti
        c2=2,#sosyal bileşen sabiti
        w=0.7,#eylemsizlik sabiti
        wdamp=1.0
        ):
    # Boş parçacık şablonunu oluşturduk
    empty_particle = {
        'position': None,
        'velocity': None,
        'cost': None,
        'best_position': None,
        'best_cost': None,
    }

    #Matematiksel atamaları yaptık.
    CostFunction = problem['CostFunction']
    VarMin = problem['VarMin']
    VarMax = problem['VarMax']
    nVar = problem['nVar']

    # Global Best'i tanımla
    gbest = {'position': None, 'cost': np.inf}

    # Popülasyon değerlerini atadık
    pop = []
    for i in range(0, PopSize):
        pop.append(empty_particle.copy())
        pop[i]['position'] = np.random.uniform(VarMin, VarMax, nVar)
        pop[i]['velocity'] = np.zeros(nVar)
        pop[i]['cost'] = CostFunction(pop[i]['position'])
        pop[i]['best_position'] = pop[i]['position'].copy()
        pop[i]['best_cost'] = pop[i]['cost']

        if pop[i]['best_cost'] < gbest['cost']:
            gbest['position'] = pop[i]['best_position'].copy()
            gbest['cost'] = pop[i]['best_cost']

    # Popülasyon değerlerini gelen verilere göre formülüze ettik.
    for it in range(0, MaxIter):
        for i in range(0, PopSize):

            pop[i]['velocity'] = w * pop[i]['velocity'] \
                                 + c1 * np.random.rand(nVar) * (pop[i]['best_position'] - pop[i]['position']) \
                                 + c2 * np.random.rand(nVar) * (gbest['position'] - pop[i]['position'])

            pop[i]['position'] += pop[i]['velocity']
            pop[i]['position'] = np.maximum(pop[i]['position'], VarMin)
            pop[i]['position'] = np.minimum(pop[i]['position'], VarMax)

            pop[i]['cost'] = CostFunction(pop[i]['position'])

            if pop[i]['cost'] < pop[i]['best_cost']:
                pop[i]['best_position'] = pop[i]['position'].copy()
                pop[i]['best_cost'] = pop[i]['cost']

                if pop[i]['best_cost'] < gbest['cost']:
                    gbest['position'] = pop[i]['best_position'].copy()
                    gbest['cost'] = pop[i]['best_cost']

        w *= wdamp
        print('Iteration {}: Best Cost = {}'.format(it, gbest['cost']))

    return gbest, pop

# Geçen süreyi ölçmek için MATLAB'daki tic toc fonksiyonlarını kendimiz yazarak oluşturduk!
startTime_for_tictoc=0

def tic():

    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():

    if 'startTime_for_tictoc' in globals():
        dt = math.floor(100*(time.time() - startTime_for_tictoc))/100.
        print('Geçen süre{} saniye(s).'.format(dt))
    else:
        print('Başlangıç zamanı ayarlanmadı.')
