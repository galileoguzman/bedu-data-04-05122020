import random

PROMOTIONS = [0.05, 0.10, 0.15]

pricing = [1975, 1825, 275, 1500, 850, 675, 1175, 1600, 2175, 2175, 625, 1150, 1175, 350, 1125, 1250, 1875, 1275, 825, 1575, 300, 1275, 875, 1650, 875]

def apply_promotion_code(initial_price):
    promotion_to_apply = random.choice(PROMOTIONS)
    final_price = initial_price - (initial_price * promotion_to_apply) # 1975 -> 1990.1278631278643
    return round(final_price, 2)


final_menu_pricing = list(map(apply_promotion_code, pricing))

print(pricing)
print('\n\n')
print(final_menu_pricing)
