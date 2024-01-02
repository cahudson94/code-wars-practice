"""
Thanks to the effects of El Nino this year my holiday snorkelling trip was akin to being in a washing machine... Not fun at all.

Given a string made up of '~' and '_' representing waves and calm respectively, your job is to check whether a person would become seasick.

Changes from calm to wave or wave to calm will add to the effect (really wave peak to trough but this will do). Find out how many changes in level the string has and if that number is more than 20% of the length of the string, return "Throw Up", else return "No Problem".
"""

def sea_sick(sea):
    changes = 0
    for idx, x in enumerate(sea[:-1]):
        if x != sea[idx + 1]:
            changes += 1
    return "No Problem" if changes <= len(sea) * .2 else "Throw Up"
