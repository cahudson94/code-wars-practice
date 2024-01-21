"""
In this Kata you must calulate the number of bounces a ball makes when shot between two walls
Task Details:

    Mr Reecey has bought a new ball cannon and he lives in a tower block

    He wants to calulate the number of bounces between the two towers before he shoots his shot

    The gun is set up to fire with a velocity v, on the tower block height h and the width between them as w

    The gun is set up parrallel to the horizontal

In this diagram the ball bounces twice:

<sodipodi:namedview id="namedview7" pagecolor="#ffffff" bordercolor="#666666" borderopacity="1.0" inkscape:pageshadow="2" inkscape:pageopacity="0.0" inkscape:pagecheckerboard="0" inkscape:document-units="mm" showgrid="false" inkscape:zoom="0.77771465" inkscape:cx="408.24742" inkscape:cy="570.26057" inkscape:window-width="1723" inkscape:window-height="1111" inkscape:window-x="476" inkscape:window-y="176" inkscape:window-maximized="0" inkscape:current-layer="layer1" />
Technicalities:

    There are 5 fixed tests and 100 random tests

    SI units are used for height, width, velocity and g (m, m, m/s, m/s^2 respectively)

    Mr Reecey uses g = 9.81, ignores air resistance and assumes elastic collisions

    The ball is modelled as very small

    Also, remember to return the number of bounces as an integer

time to ground = (2 * height / gravity) ^ .5
"""

def bounce_count(h, w, v):
    return v * ((2 * h / 9.81) ** 0.5) // w
