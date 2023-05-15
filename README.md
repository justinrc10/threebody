# threebody
Three-body problem simulator

The three-body problem is a famous physics problem concerning motion caused by gravitational force. 
The formulation is as follows:

Suppose you have three bodies out in space such that the only forces in the system are the pairwise gravitational forces exerted between the bodies. 
Determine the path that each body takes.

Since the formula for the gravitational force between two bodies has been discovered to be F = G * m_1 * m_2 * r / |r|^3, where m_1 and m_2 are the masses of the bodies, r is the vector that connects the two bodies, and G is a constant, together with Newton's laws, we can set up a system of second order ordinary differential equations that mathematically models the paths of each of the bodies. 

So it appears that the problem has essentially been solved! Once we have a differential equation, you usually either solve it analytically or approximate it numerically. However, what makes this problem so famous is that it is almost impossible to do either!

For one, it has been shown that the path almost never has a closed form.
That is, if p_1(t) = (x_1(t), y_1(t)) is a parametrization of the first body, then it is impossible to write x_1(t) or y_1(t) in a finite combination of elementary functions.

Furthermore, if one chooses to expand the solution using a series expansion, the convergence rate would be too slow to generate sufficient accuracy for applications. From the Wikipedia article on the three-body problem:

"The corresponding series, however, converges very slowly. That is, obtaining a value of meaningful precision requires so many terms that this solution is of little practical use. Indeed, in 1930, David Beloriszky calculated that if Sundman's series were to be used for astronomical observations, then the computations would involve at least 10^8000000 terms."

Finally, it has been shown that the system is also almost always chaotic.
Mathematically, this means that if you start with one set of initial conditions and generate one path, and then restart with even slightly different initial conditions and generate a new path, then the new path does not have to share any resemblence to the original path at all.
Thus, even if one mathematically solved for the initial conditions required to generate a desired path, it is not guaranteed that replicating those initial conditions in an experiment will replicate the desired path, since it is nearly impossible to perfectly set up initial conditions in practice.

The program threebody.py is a naive approach to the three-body problem using the Runge-Kutta numerical method. I first wrote out the system of 6 second order ordinary differential equations (2 spacial variables for each of the 3 bodies with respect to time) and converted it to a system of 12 first order ordinary differential equations in the standard appraoch. From there, I simply applied the Runge-Kutta method to generate a path for the system and extracted the spacial coordinates at each time-step.

While the resulting animation may look like three bodies acting on each other's gravitational pull, it should be noted that I cannot verify the motion is consistent with reality.
