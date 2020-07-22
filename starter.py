from collections import defaultdict

from recipeCheck import computeEachMeal, computeEachEnergy, computeBMR
from recipeGenerate import generateRecipe


def Recipe():
    for i in range(1, 8):
        print(f'第{i}天全天菜谱:')
        b = generateRecipe('breakfast')
        b2 = '+'.join(b)
        print(f'【早饭】:{b2}')
        l = generateRecipe('lunch')
        l2 = '+'.join(l)
        print(f'【中饭】:{l2}')
        d = generateRecipe('dinner')
        d2 = '+'.join(d)
        print(f'【晚饭】:{d2}')
        e = generateRecipe('extra')
        e2 = '+'.join(e)
        print(f'【下午茶】:{e2}')


def energyDistribution(sex, weight, stature, age, exerciseLevel):
    map1 = {'breakfast': '早饭', 'lunch': '中饭', 'dinner': '晚饭', 'protein': '蛋白质', 'carbonhydrate': '碳水化合物', 'fat': '脂肪'}
    totalEnergy = int(computeBMR(sex, weight, stature, age, exerciseLevel))
    energyEachMeal_temp = {}
    energyEachMeal = defaultdict(list)
    for i in ['breakfast', 'lunch', 'dinner']:
        energy = int(computeEachMeal(i, totalEnergy))
        energyEachMeal[map1[i]].append(f'总能量:{energy}')
        energyEachMeal_temp[map1[i]] = energy
    for k, v in energyEachMeal_temp.items():
        for i in ['protein', 'carbonhydrate', 'fat']:
            energy = int(computeEachEnergy(i, v))
            energyEachMeal[k].append(f'{k}:{map1[i]}能量:{energy}')
    for k, v in energyEachMeal.items():
        print(k, v)


if __name__ == '__main__':
    energyDistribution('M', 70, 180, 20, 2)
    Recipe()
