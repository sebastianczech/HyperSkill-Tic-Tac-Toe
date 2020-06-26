cafe_cats = []
while True:
    cafe_cat = input()
    if cafe_cat == 'MEOW':
        break
    cafe_cats.append(cafe_cat)

max_cat = -1
max_cafe = ""

for cafe_cat in cafe_cats:
    cafe = cafe_cat.split()[0]
    cat = cafe_cat.split()[1]
    if int(cat) > max_cat:
        max_cat = int(cat)
        max_cafe = cafe

print(max_cafe)
