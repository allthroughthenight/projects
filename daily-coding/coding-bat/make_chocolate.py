# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

def make_chocolate(small, big, goal):
  small_bars = 0

  # how many bigs in the goal
  goal_five = (goal/5)

  # if bigs more than can use, then use all of them
  if goal_five > big:
    big_len = big * 5
  # else use only the max available
  elif goal_five <= big:
    big_len = goal_five * 5

  # if able to match or exceed goal, get how many small bars used
  if big_len + small >= goal:
    small_bars = goal - big_len
  else:
    small_bars = -1

  return small_bars
