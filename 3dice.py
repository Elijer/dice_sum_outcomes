sides = [x for x in range(1, 7)]

rolls = {}
dice = 3

# roll dice a, b and c
counter = 1
for a in sides:
  for b in sides:
    for c in sides:
      rolls[counter] = [a, b, c]
      counter = counter + 1
      
plays = []
      
for r in rolls:
  roll = rolls[r]
  roll.append(roll[0] + roll[1])
  roll.append(roll[1] + roll[2])
  roll.append(roll[0] + roll[2])
  roll.append(roll[0] + roll[1] + roll[2])
  for play in roll:
    if play < 14:
      plays.append(play)
      
freqs = {}
for possibility in range(1,14):
  freqs[possibility] = { "occurences": 0, "chance": 0}
  
for play in plays:
  freqs[play]["occurences"] = freqs[play]["occurences"] + 1
  
for freq in freqs:
  freqs[freq]["chance"] =  freqs[freq]["occurences"] / len(plays)
  freqs[freq]["examplanation"] = f"Out of a total of {len(plays)}, {freq} would be playable about {freqs[freq]['occurences']} times"
  print(freqs[freq]["chance"])