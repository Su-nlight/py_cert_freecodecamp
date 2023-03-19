import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.data = [k for k, v in kwargs.items() for x in range(v)]

  def draw(self, n):
    n = min(n, len(self.data))
    return [self.data.pop(random.randrange(len(self.data))) for x in range(n)]


def experiment(hat, ball_expec, ball_draw, nos_exp):
  m = 0
  for x in range(nos_exp):
    another_hat = copy.deepcopy(hat)
    ball_draw = another_hat.draw(ball_draw)
    reqbal = sum([1 for k, v in ball_expec.items() if ball_draw.count(k) >= v])
    m += 1 if reqbal == len(ball_expec) else 0

  return m / nos_exp
