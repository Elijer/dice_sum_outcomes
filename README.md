# dice_sum_outcomes

I wish I had a single file that did all this, but it was faster to just simulate each dice scenario separately, so what you see is a file for 2, 3, and 4 dice. The calculations for one dice are trivial - the likelihood of each "play" is `1/6`.

Let me define what a "play" is here - a play is any number you can reach by using the value of just one dice or any additional dice available. For example, if you have three dice to roll and you roll [1, 5, 6], then any of the following would be valid "plays":

- 1
- 5
- 6
- 1 + 5 = 6
- 5 + 6 = 6
- 1 + 6 = 7
- 1 + 5 + 6 = 12

Therefore, for this roll, you could play: 1, 5, 6, 6, 6, 7, 12.

So the purpose of this repo is to not only calculate how many valid "plays" exist for each roll for 1, 2, 3 and 4 dice situations, but also how likely those plays are to be available. For example, 6 came up (ominously) 3 times, so 6 is more likely than any of the other 7 potential "plays", and therefore it's availability is statistically `3/7`.

# Why
I'm making a boardgame and in order to balance it, I sorta need to know how likely each number is. So this was my way of figuring that out. I would love to hear any suggestions or references to other work on this subject.
