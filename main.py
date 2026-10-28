def davlatlar():
    davlatlar2 = ["Yaponiya", "Amerika", "Arabiston","Kolumbiya","Koreya","Rossiya","Xitoy"]
    davlatlar2.sort(reverse=True)
    print(davlatlar2)
    # davlatlar2.sort(reverse=False)
    print(sorted(davlatlar2))
# davlatlar()

def raqamlar():
    for a in range(0,121,2):
        print(a)
    print(sum(range(0,121,2)))
    print(max(range(0,121,2)) - min(range(1,121,3)))
    # print(max(range(0,121,2)))
# raqamlar()

def taomlar():
    taomlarr = ['osh', 'manti', 'shawarma', "sho'rva", "choy", 'xolva', 'shakar']
    nonushta = taomlarr.copy()
    nonushta.remove(taomlarr[0])
    nonushta.remove(taomlarr[1])
    nonushta.remove(taomlarr[2])
    nonushta.remove(taomlarr[3])
    nonushta.append("non")
    nonushta.append("murabbo")
    print("nonushta: " , nonushta)
    print("taomlar: " , taomlarr)
taomlar()