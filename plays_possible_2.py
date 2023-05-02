from itertools import combinations

combo = [1, 1, 3, 4]

def possible_plays(c):
  
  # single plays
  possible_plays = [c[0], c[1], c[2], c[3]]

  # double plays
  double_plays = [x for x in combinations(c, 2)]
  for d in double_plays:
    possible_plays.append(sum(d))
    
  # triple plays
  triple_plays = [x for x in combinations(c, 3)]
  for t in triple_plays:
    possible_plays.append(sum(t))
    
  # quad play
  possible_plays.append(sum(c))
  
  return possible_plays
  
  