"""
In this task you have to code process planner.

You will be given initial thing, target thing and a set of processes to turn one thing into another (in the form of [process_name, start_thing, end_thing]). You must return names of shortest sequence of processes to turn initial thing into target thing, or empty sequence if it's impossible.

If start already equals end, return [], since no path is required.

Example:

test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
];

processes('field', 'bread', test_processes) # should return ['gather', 'mill', 'bake']
processes('field', 'ferrari', test_processes) # should return []
processes('field', 'field', test_processes) # should return [], since no processes are needed

Good luck!
"""

def processes(start, end, processes):
    to_visit = [(start, [])]
    visited = set()
    
    while to_visit:
        start, path = to_visit.pop(0)
        if start == end:
            return path
        visited.add(start)
        for process in processes:
            if process[1] == start and process[2] not in visited:
                to_visit.append([process[2], path + [process[0]]])
    return []
