"""Tools:

Tools of a task are a list of tools that the task requires. This info is available to agents during execution, helping them understand
the task they are working on."""

import controlflow as cf
import random


def roll_dice(n_dice: int):
    return [random.randint(1, 6) for _ in range(n_dice)]

rolls = cf.run(
    "Roll 3 dice",
    result_type=list[int],
    tools=[roll_dice],
)

print(rolls)