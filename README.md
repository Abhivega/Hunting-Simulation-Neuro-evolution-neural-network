# Hunt
Simulation of a hunting using p5 and Python using boids. The original inspiration is to create a machine learning framework that enables predators to catch it’s pray. To start, I created a python script using p5 to create a hunting ground. Later on this can be used to obtain necessary data points for a deep learning / neuro evolution framework.
    Now the hunting is completely done using procedural learning with recombination and mutation of best fit. 

## Changes

*   Fully functioning recombination method.
    *   Selects the best two performing predators and their weights are recombined with a probability, more weightage is given to the best performer
    *   A slight mutation chance is also included
    *   Observed to perform better with recombination
*   Keyboard PRESS "S” to save the weights of the best performer to an .npz file. The neural network can initialize its weights from this file by giving a true flag. Thus, training can be done in a sequence with increasing difficulty without redoing the whole calculation for each variation. This feature allows great flexibility and it corresponds to how normal learning happens in organisms - a gradual learning procedure.


## contributing

Any optimization is welcome. This is my first attempt here at GitHub.


