# We want to match a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to match the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.

def make_bricks(small, big, goal):
  match = False

  # how many 5's in the goal
  goal_five = (goal/5)

  # if no 5's but 1's meet goal, match
  if big == 0 and small >= goal:
      match = True

  # if more 5's than can, then use 'big' to get length
  if goal_five > big:
    big_len = big * 5
  # else use only the max available
  elif goal_five <= big:
    big_len = goal_five * 5

  # if 1's and 5's are greater than goal, match
  if big_len + small >= goal:
    match = True

  return match
