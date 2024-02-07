"""
Introduction

There is a war and nobody knows - the alphabet war!
The letters called airstrikes to help them in war - dashes and dots are spread everywhere on the battlefield.
Task

Write a function that accepts reinforces array of strings and airstrikes array of strings.
The reinforces strings consist of only small letters. The size of each string in reinforces array is the same.
The airstrikes strings consists of * and white spaces. The size of each airstrike may vary. There may be also no airstrikes at all.

The first row in reinforces array is the current battlefield. Whenever some letter is killed by bomb,
it's replaced by a letter from next string in reinforces array on the same position.
The airstrike always starts from the beginning of the battlefield.
The * means a bomb drop place. The each * bomb kills letter only on the battelfield.
The bomb kills letter on the same index on battlefield plus the adjacent letters.
The letters on the battlefield are replaced after airstrike is finished.
Return string of letters left on the battlefield after the last airstrike. In case there is no any letter left in reinforces on specific position, return _.

reinforces = [ "abcdefg",
               "hijklmn"];
airstrikes = [ "   *   ",
               "*  *   "];
               
The battlefield  is     : "abcedfg".
The first airstrike    : "   *   "  
After first airstrike  : "ab___fg"
Reinforces are comming : "abjklfg"
The second airstrike   : "*  *   "
After second airstrike : "_____fg"
Reinforces are coming  : "hi___fg"
No more airstrikes => return "hi___fg"

Other example

  reinforces =    
          ["g964xxxxxxxx",
           "myjinxin2015",
           "steffenvogel",
           "smile67xxxxx",
           "giacomosorbi",
           "freywarxxxxx",
           "bkaesxxxxxxx",
           "vadimbxxxxxx",
           "zozofouchtra",
           "colbydauphxx" ];
airstrikes =
          ["* *** ** ***",
           " ** * * * **",
           " * *** * ***",
           " **  * * ** ",
           "* ** *   ***",
           "***   ",
           "**",
           "*",
           "*" ]

That should lead to:

alphabet_war(reinforces, airstrikes); # => codewarsxxxx

Alphabet war Collection
Alphavet war
Alphabet war - airstrike - letters massacre
Alphabet wars - reinforces massacre
Alphabet wars - nuclear strike
Alphabet war - Wo lo loooooo priests join the war
"""

def alphabet_war(reinforces, airstrikes):
    out = list(list(x) for x in zip(*reinforces))
    replaces = {i: 0 for i in range(len(out))}
    for strike in airstrikes:
        bombed = []
        for i in replaces:
            if i < len(strike) and strike[i] == "*":
                if i > 0 and i - 1 not in bombed:
                    bombed.append(i - 1)
                    replaces[i - 1] += 1
                if i < len(replaces) - 1 and i + 1 not in bombed:
                    bombed.append(i + 1)
                    replaces[i + 1] += 1
                if i not in bombed:
                    bombed.append(i)
                    replaces[i] += 1
    return "".join([line[replaces[idx]] if replaces[idx] < len(line) else "_" for idx, line in enumerate(out)])
