import collections


# 计算一个食物包含的总热量
def computeFoodEnergy(protein, carbonhydrate, fat):
    """
    蛋白质(单位:克)
    碳水化合物(单位:克)
    脂肪的含量(单位:克)
    """
    return protein * 4 + carbonhydrate * 4 + fat * 9


def consumeEnergy(age, weight):
    """
    年龄
    体重(单位:公斤)
    """
    if 18 <= age <= 30:
        return weight * 0.062 * 2.036 * 240
    elif 30 <= age <= 60:
        return weight * 0.034 * 3.538 * 240
    elif age > 60:
        return weight * 0.038 * 2.755 * 240
    else:
        return -1


def computeBMR(sex, weight, stature, age, exerciseLevel):
    """
    性别(M/F)
    体重(单位:公斤)
    身高(单位:厘米)
    年龄
    运动量(段位0-4)
    """
    if sex == 'M':
        BMR = 66 + (13.7 * weight) + (5 * stature) - (6.8 * age)
    else:
        BMR = 655 + (9.6 * weight) + (1.8 * stature) - (4.7 * age)
    if exerciseLevel == 0:
        return BMR * 1.2
    elif exerciseLevel == 1:
        return BMR * 1.375
    elif exerciseLevel == 2:
        return BMR * 1.55
    elif exerciseLevel == 3:
        return BMR * 1.725
    elif exerciseLevel == 4:
        return BMR * 1.9
    else:
        return -1


def computeEachMeal(period, totalEnergy):
    """
    早饭(B)、中饭(L)、晚饭(D)
    总能量需求
    """
    if period.upper().startswith('B'):
        return totalEnergy * 0.3
    elif period.upper().startswith('L'):
        return totalEnergy * 0.4
    elif period.upper().startswith('D'):
        return totalEnergy * 0.3
    else:
        return -1


def computeEachEnergy(energyKind, totalEnergy):
    """
    能量类型
    总能量需求
    """
    if energyKind.upper().startswith('P'):
        return totalEnergy * 0.125
    elif energyKind.upper().startswith('C'):
        return totalEnergy * 0.625
    elif energyKind.upper().startswith('F'):
        return totalEnergy * 0.25
    else:
        return -1


def computeFlavor(recipe_flavors):
    """
    菜谱中味道: 酸甜苦辣咸['sour', 'sweet', 'bitter', 'spicy', 'salty']
    """
    # 统计五种味道
    rst1 = len(set(recipe_flavors))
    # 同一种味道的菜是否过多
    rst_temp = collections.Counter(recipe_flavors)
    rst2 = len([_ for _ in rst_temp.keys() if _ > 1])
    # 味道种类过少
    if rst1 < 2:
        print('X: Too few flavors')
    else:
        print('Type of Flavors OK')
    # 同一种味道过多
    if rst2 > 0:
        print('X: Too many same flavors')
    else:
        print('Number of same Flavors OK')


def computeColor(recipe_colors):
    """
    菜谱中色彩: 红绿蓝黄白黑['red','green','blue','yellow','white','black']
    """
    # 统计颜色
    rst1 = set(recipe_colors)
    # 同一种颜色的菜是否过多
    rst_temp = collections.Counter(recipe_colors)
    rst2 = len([_ for _ in rst_temp.keys() if _ > 1])
    # 色彩种类过少
    if rst1 < 2:
        print('X: Too few colors')
    else:
        print('Type of Colors OK')
    # 同一种色彩过多
    if rst2 > 0:
        print('X: Too many same colors')
    else:
        print('Number of same Colors OK')


def computePH(acidNum, alkaliNum):
    """
    酸性食物数量
    碱性食物数量
    """
    if acidNum > alkaliNum:
        print('X: Unhealthy')
    else:
        print('Healthy')


def computerYY(recipe_yy):
    """
    菜谱中性质: 温平寒['warm','plain','cold']
    """
    rst1 = collections.Counter(recipe_yy)
    if rst1['warm'] != rst1['cold']:
        print('X: UnBalanced')
    else:
        print('Balanced')
