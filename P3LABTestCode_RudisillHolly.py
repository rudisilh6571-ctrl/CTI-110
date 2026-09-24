# HOlly Rudisil
# #P3LAB
# 09/24/2026
# Test potion code to understand how to use floor division and modulo

# example 1 with potions

hp = int(input("How many HP of damage (l-100): "))
print("you took ", hp, "damage")

# large potions
large = hp // 25         #each potion heals 25
hp = hp % 25             #some damage leftover

print("Drank", large, "large potions.") 
print("Damage remaining ", hp)       

# small potions heal 5
small = hp // 5
hp = hp % 5

print("Drank", small, "small potions.")
print("Damage remaining ", hp)

