"""
Background

This exercise assumes basic knowledge of generators, including passing familiarity with the yield keyword.
Catching You Up on Generators

While it is obvious that you can obtain items from generators,
it is less known that you can also send data into generators in languages like Python and JavaScript.
We are going to explore the very basics of that today.

First, we need to establish a couple of concepts:

    Sending: To send something to a generator, you call the .send method on it.
    It’s a general form of next. In fact, next(generator) is the same as generator.send(None).
    Both functions allow you to access the next item of the generator, but .send also lets you send a non-None message.

    yielded_value = my_generator.send('howdy from the outside world!')

    Receiving: By assigning the yield expression to a variable, you are able to access whatever was sent to the generator.

    So, the following line inside a generator

    msg = yield 5

    yields 5, pauses the generator, and gives control back to the caller.
    If the caller sends a msg (or calls next, which sends a None message), the generator stores that in msg and resumes until it yields another element.

    Priming a Generator: You can only send a message to a generator if you had primed it by calling next (or .send(None)) on it first.
    This is to ensure the generator actually gets to the part of its body that yields.

Since this an introductory Kata, you may want to look at a sample example that puts all these concepts together:
View example
Here’s a generator that infinitely repeats the last message sent to it.

def echo_echo():
    thing_to_repeat = None  # Initialize.
    
    while True:
        new_thing = yield thing_to_repeat
        
        # If the user actually sent something instead of just calling next.
        if new_thing is not None: thing_to_repeat = new_thing

        # Else, it means the user just called next, so keep repeating the old thing.

# Usage
echo = echo_echo()
next(echo)  # As previously discussed, this first call to next is mandatory before sending.

print('Setting echo to ', echo.send('hi'))  # Prints 'Setting echo to  hi'.
for i in range(5): print(next(echo))  # Prints 'hi' 5 times.
    
print('Setting echo to ', echo.send('bye'))  # Prints 'Setting echo to  bye'.
for i in range(5): print(next(echo))  # Prints 'bye' 5 times.

Task

Imagine you run a very tiny production line with two "worker" generators, gen1 and gen2, that generate data for you.
Your task is to create a new generator function, round_robin (or roundRobin in JS),
that will allow you to collect items from these two generators in a round-robin fashion.

def round_robin(gen1, gen2):
    # ...

The term “round-robin” is often used to describe a process where participants take turns in a cyclic order.
In this case, your generator function should yield one item from gen1, then one item from gen2, then one item again from gen1 and so forth,
continuing this alternating pattern.

Moreover, you may want to provide feedback to these generators based on their output.
Your round_robin generator should be open to being sent messages by calling the .send() method on it.
When round_robin receives a message, it should forward this message to the next generator in the sequence.

For example, if round_robin has just yielded an item from gen2, and you send a message to round_robin,
that message should internally be forwarded directly to gen1.

Here is sample usage:

factory = round_robin(gen1, gen2)
print(next(factory))     # Yields one item from gen1.
print(next(factory))     # Yields one item from gen2.
print(next(factory))     # Yields one item from gen1.
print(factory.send(32))  # Yields one item from gen2 after sending 32 to it.
print(factory.send(6))   # Yields one item from gen1 after sending 6 to it.

Note that .send, like next, consumes one element. It's easy to accidentally miss out this item, so don't.
Assumptions

    You do NOT need to worry about priming the generators before sending.
    By the time you need to send messages to the generators,
    the testing process will have ensured that the generators are already in a state where they are ready to receive.
    Both generators are infinite - neither of them gets exhausted, so you don't need to handle that.
    In the random tests, the generators that will be fed into your function will exclusively be among a pool of four generators I wrote.
    This is to make debugging easier and more sane from your side.
    View provided generators
        count_up or countUp (also included in the fixed tests): Infinitely counts up from whatever number sent to it (or 0 by default).
        For example, if you send 3 to it, it will yield back 3 4 5 6 7 8 9 ....
        gen_multiples or genMultiples: Infinitely yields from the multiplication table of the number sent to it (0's table, by default).
        For example, if you send 3 to it, it will yield back 0 3 6 9 12 15 ....
        split_string or splitString (also included in the fixed tests): Infinitely yields characters from a string sent to it, and loops back when finished.
        If sent nothing, loops ''. For example, if you send 'hey' to it, it will yield back 'h' 'e' 'y' 'h' 'e' 'y' ....
        repeat_string or repeatString: Infinitely repeats a string sent to it.
        For example, if you send 'hey' to it, it will yield back 'hey' 'hey' 'hey' 'hey' ....
"""

from itertools import cycle

def round_robin(gen1, gen2):
    msg = None
    for gen in cycle([gen1, gen2]):
        msg = yield gen.send(msg)
