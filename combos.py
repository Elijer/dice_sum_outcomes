from itertools import combinations, combinations_with_replacement
l = [1, 2, 3, 4]
# print(list(combinations(l, 2)))
# print(list(combinations(l, 3)))

def find_all_sums(lest):
  combos = list(combinations(l, 2))
  sums = []
  for c in combos:
    sums.append(sum(c))
    return sums
    
print(find_all_sums(l))