def MultilplyTuplets(tuplets):
    r = 1
    for a in tuplets:
        r = r * a
    return r
tuplet1 = (4, 3, 2, 2, -1, 18)
tuplet2 = (2, 4, 8, 8, 3, 2, 9)
print(MultilplyTuplets(tuplet1))
print(MultilplyTuplets(tuplet2))