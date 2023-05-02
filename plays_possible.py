from itertools import permutations, combinations

combo = [1, 1, 3]

def possible_plays(c):
  
  # single plays
  possible_plays = [c[0], c[1], c[2]]

  # double plays
  double_plays = [x for x in combinations(c, 2)]
  for d in double_plays:
    possible_plays.append(sum(d))
    
  # triple play
  possible_plays.append(sum(c))
  
  return possible_plays
  
# print(possible_plays(combo))
  
  