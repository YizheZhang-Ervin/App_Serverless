import random

co_rice = ['薏仁', '黑米', '梗米', '面', '普通米饭', '糙米饭']
co_dish = ['黄豆', '黑豆', '山药', '马铃薯', '红薯', '玉米']
co_breakfast = ['燕麦', '小麦(全麦面包)']
protein_meat = ['鸡胸肉', '青条鱼', '马鲛鱼', '秋刀鱼', '大马哈鱼', '虾']
protein_drink = ['牛奶', '酸奶', '豆浆']
fat = ['栗子', '杏仁', '牛油果', '花生', '腰果']
cellulose = ['花椰菜', '大蒜', '洋葱', '红椒', '卷心菜', '西红柿', '西兰花', '白菜', '豆苗']
vitamin = ['苹果', '猕猴桃', '葡萄', '草莓', '桂圆', '金橘']
drink = ['柠檬汁', '枸杞', '绿茶', '雪梨', '蜂蜜']
seasoning = ['植物油', '橄榄油', '亚麻籽', '黑芝麻']


def randomChoose(sequence):
    return sequence[random.randint(0, len(sequence) - 1)]


def generateRecipe(period):
    """
    period: 早饭(B)、中饭(L)、晚饭(D)、加餐(E)
    """
    if period.upper().startswith('B'):
        combo1 = randomChoose(co_breakfast)
        combo2 = randomChoose(protein_drink)
        combo3 = randomChoose(fat)
        combo4 = randomChoose(vitamin)
        return combo1, combo2, combo3, combo4
    elif period.upper().startswith('L'):
        combo1 = randomChoose(co_rice)
        combo2 = randomChoose(co_dish)
        combo3 = randomChoose(protein_meat)
        combo4 = randomChoose(seasoning)
        combo5 = randomChoose(cellulose)
        combo6 = randomChoose(vitamin)
        return combo1, combo2, combo3, combo4, combo5, combo6
    elif period.upper().startswith('D'):
        combo1 = randomChoose(co_rice)
        combo2 = randomChoose(co_dish)
        combo3 = randomChoose(protein_meat)
        combo4 = randomChoose(seasoning)
        combo5 = randomChoose(cellulose)
        combo6 = randomChoose(vitamin)
        return combo1, combo2, combo3, combo4, combo5, combo6
    elif period.upper().startswith('E'):
        combo1 = randomChoose(fat)
        combo2 = randomChoose(vitamin)
        combo3 = randomChoose(drink)
        return combo1, combo2, combo3
    else:
        return -1
