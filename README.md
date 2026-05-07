# Amazing Journeys of Langton's Ant
Introduced in 1986, Langton's Ant is a cellular automata well-know for the variety of theoritical concepts it's linked with. This repositery proposes a lot of experiments made with this automata, and some explanations about what they are lighting up.

# Explanations about the name of files
  - "Fourmi" means "Ant" in french
  - The key word "exp" means that the grid expands as the ant needs more space, just as if the ant evolutes in an infinite space.
  - The key word "mod" means that the ant evolutes in a finite space, just as it was a donut : when it hits the left wall, it comes back by the right one.
  - the key word "n" means that you will choose at the beginnig how many ants you want on your simulation (when there is no "n" it means that there's only one ant)
  - the key word "gif" means that instead of directly showing the screen where evolutes the ant, it will create a gif of the simulation
  - the file "fourmi_base" is the initial code : one ant on a white screen with a finished size. "fourmi_main" is the same but better optimised.
  - the files "fourmi_mot_rec_fin" and "fourmi_mot_sqr_fin" are a configuration where one ant is put on a random finish rectangular (resp. square) map.

# Introducing Langton's Ant cellular automaton
This automaton is an ant on a 2-coloured grid which follows the following rules :
if the cell where the ant is is a white cell, she turns it to black and rotate to left
else, the cell is a black cell, she turns it to white and rotate to right.
Then, she move one cell forward and repete it.

# Some nice results
 1) Unbounded trajectory
      The proof was made that for every initial map, the trajectory of the ant is unbounded. This proof is accessible in the file "proof_unbounded_trajectory.txt".
 2) Attractors
      What we observe by whatching the evolution of the ant from diverse initial configurations is an attractor of its trajectory, a kind of "highway" : a drawing of 104 steps that the ant repetes infinitely. When we put more than one ant on a map, we observe that when an ant draws a highway, the other ants can use this highway to move faster in one direction, which justifies the name we gave to it. To simplify, an attractor is a stable state towards which a system evolves (in the case of Langton's Ant, the attractor is this drawing that constitutes the highway). Even if it wasn't proved yet, some mathematicians conjectured that this attractor appears, whatever the initial finite configuration. However, it is false in the case of an infinite configuration. 
