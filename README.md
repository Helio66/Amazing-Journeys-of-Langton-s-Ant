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
if the cell where the ant is is a white cell, she turn it to black and 
