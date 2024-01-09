"""
Your task is to implement a function that calculates an election winner from a list of voter selections using an Instant Runoff Voting algorithm. If you haven't heard of IRV, here's a basic overview (slightly altered for this kata):

    Each voter selects several candidates in order of preference.
    The votes are tallied from the each voter's first choice.
    If the first-place candidate has more than half the total votes, they win.
    Otherwise, find the candidate who got the least votes and remove them from each person's voting list.
    In case of a tie for least, remove all of the tying candidates.
    In case of a complete tie between every candidate, return nil(Ruby)/None(Python)/undefined(JS).
    Start over.
    Continue until somebody has more than half the votes; they are the winner.

Your function will be given a list of voter ballots; each ballot will be a list of candidates (symbols) in descending order of preference. You should return the symbol corresponding to the winning candidate. See the default test for an example!

optimized:
def runoff(voters):
    while voters[0]:
        votes = {x: 0 for x in voters[0]}
        candidates = list(votes.keys())
        for voter in voters:
            votes[voter[0]] += 1
        losers = min(votes.values())
        for candidate in candidates:
            if votes[candidate] > len(voters) / 2:
                return candidate
            if votes[candidate] == losers:
                for voter in voters:
                    voter.remove(candidate)
    return None
"""

def runoff(voters):
    results = {x: 0 for x in voters[0]}
    for voter in voters:
        results[voter[0]] += 1
    if max(results.values()) > len(voters) / 2:
        return [key for key, val in results.items() if val == max(results.values())][0]
    to_remove = []
    for key, val in results.items():
        if val == min(results.values()):
            to_remove.append(key)
    for idx, voter in enumerate(voters):
        for name in to_remove:
            voter.remove(name)
        if not voter:
            return None
        voters[idx] = voter
    return runoff(voters)
