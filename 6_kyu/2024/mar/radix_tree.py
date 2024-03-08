"""
Implement a function which creates a radix tree ( a space-optimized trie [prefix tree] )

    in which each node that is the only child is merged with its parent ( unless a word from the input ends there )

    from a given list of words

    using dictionaries ( aka hash tables, hash maps, maps, or objects )

    where:
        The dictionary keys are the nodes.
        Leaf nodes are empty dictionaries.
        The value for empty input is an empty dictionary.
        Words are all lowercase or empty strings.
        Words can contain duplicates.

Examples:

>>> radix_tree()
{}

>>> radix_tree("")
{}

>>> radix_tree("", "")
{}

>>> radix_tree("radix", "tree")
{"radix": {}, "tree": {}}

>>> radix_tree("ape", "apple")
{"ap": {"e": {}, "ple": {}}}

>>> radix_tree("apple", "applet", "apple", "ape")
{"ap": {"ple": {"t": {}}, "e": {}}}

>>> radix_tree("romane", "romanus", "romulus", "rubens", "rubicon", "rubicundus")
{"r": {"om": {"an": {"e": {}, "us": {}}, "ulus": {}},
       "ub": {"ens": {}, "ic": {"on": {}, "undus": {}}}}}

>>> radix_tree("appleabcd", "apple")
{"apple": {"abcd": {}}}
"""

from itertools import groupby
from os.path import commonprefix

def radix_tree(*words):
    result = {}
    for key, grp in groupby(sorted(word for word in words if word), key=lambda x: x[0]):
        lst = list(grp)
        prefix = commonprefix(lst)
        result[prefix] = radix_tree(*(w[len(prefix):] for w in lst))
    return result
