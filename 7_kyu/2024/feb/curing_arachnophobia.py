"""
There is no single treatment that works for every phobia, but some people cure it by being gradually exposed to the phobic situation or object.
In this kata we will try curing arachnophobia by drawing primitive spiders.

Our spiders will have legs, body, eyes and a mouth. Here are some examples:

/\((OOwOO))/\

/╲(((0000w0000)))╱\

^(oWo)^

You will be given four values:

    leg size where each value stands for its own leg type: 1 for "^ ^", 2 for "/\ /\", 3 for "/╲ ╱\", 4 for "╱╲ ╱╲"
    body size where each value stands for its own body type: 1 for "( )", 2 for "(( ))", 3 for "((( )))"
    mouth representing the spider's mouth
    eye representing the spider's eye

Note: the eyes are symmetric, and their total amount is 2 to the power of body size.

You will also be given only valid data. That's it for the instructions, you can start coding!

"""

def draw_spider(leg_size, body_size, mouth, eye):
    legs = {1: "^ ^", 2: "/\\ /\\", 3: "/╲ ╱\\", 4: "╱╲ ╱╲"}
    body = {1: "( )", 2: "(( ))", 3: "((( )))"}
    eyes = eye * (2 ** body_size // 2)
    body_with_eyes = body[body_size].replace(" ", eyes + mouth + eyes)
    return legs[leg_size].split()[0] + body_with_eyes + legs[leg_size].split()[1]
