from snuMenu import snuMenu

l = [snuMenu("감골"), snuMenu("긱식 뙇뙇"), snuMenu("학관 점심"), snuMenu("asdfj afs af"), snuMenu("301 저녁")]
snuMenu.update(1)
snuMenu.update(2)
for a in l:
    print(a.getMenu())

