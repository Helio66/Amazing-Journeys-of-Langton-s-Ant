# Introducing Langton's Ant cellular automaton
This automaton is an ant on a 2-coloured grid which follows the following rules :
if the cell where the ant is is a white cell, she turns it to black and rotate to left
else, the cell is a black cell, she turns it to white and rotate to right.
Then, she move one cell forward and repete it.

# Some nice results
 1) Unbounded trajectory : 
      The proof was made that for every initial map, the trajectory of the ant is unbounded. This proof is accessible in the file "proof_unbounded_trajectory.txt".
 2) Attractors : 
      What we observe by whatching the evolution of the ant from diverse initial configurations is an attractor of its trajectory, a kind of "highway" :
      a drawing of 104 steps that the ant repetes infinitely. When we put more than one ant on a map, we observe that when an ant draws a highway,
      the other ants can use this highway to move faster in one direction, which justifies the name we gave to it. To simplify, an attractor is a stable state
      towards which a system evolves (in the case of Langton's Ant, the attractor is this drawing that constitutes the highway).
      Even if it wasn't formally proved yet, some mathematicians published an analogy with physics, allowing us to verify that this attractor appears, whatever the
      initial finite configuration. However, it is false in the case of an infinite configuration.

# Studying the problem "Does the Ant ever visit this given cell ?"


