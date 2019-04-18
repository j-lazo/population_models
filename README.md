# Population Models

This repo contains the scripts to simulate a population model of 3 species with 3 different methods:

1. Using a deterministic ODE solver
2. Using an stochastic method (Gillespie Algorithm)
3. Using a agent based approach

For the first two options the ODE system is: 

![equation_system](equation_sys.png)

The system models a food chain as follows: 

*The food chain begins with the plant. The plant is eaten by the rabbit. The rabbit is then eaten by a larger animal, the fox.*

Being **G** the amount of *grass*, **R** the number of *rabbits*, and **F** the number of *foxes*. The deltas are the death rates of each specie according to their subindex....  


![result_1](results/_lotkavolterra_ode45_100_150_150_150.png)
![result_2](results/_lotkavolterra_ode45_spaceplot_100_401_201_101.png)
