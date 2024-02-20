"""
I have four positive integers, A, B, C and D, where A < B < C < D.
The input is a list of the integers A, B, C, D, AxB, BxC, CxD, DxA in some order. Your task is to return the value of D.
"""

def alphabet(ns):
    ns = sorted(ns)
    c = ns[2] if ns[2] != ns[0] * ns[1] else ns[3]
    return ns[-1] // c
