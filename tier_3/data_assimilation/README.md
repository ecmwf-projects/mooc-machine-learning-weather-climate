# 2022-mooc-ecmwf-bocquet-brajard

This MOOC explains how data assimilation and machine learning can be combined to achieve model discovery or model error correction.
It consists of an introduction, easily convertible into preliminary slides, and of three parts, meant to be used in sequence.
See https://lms.ecmwf.int/ for the full ECMWF event.


## Objective of this MOOC and outline

The goal of this lecture is to give a brief and very limited introduction to the connections between __machine learning/deep learning__ and __data assimilation__. Machine learning has found many new convincing applications over the past couple of years, besides computer vision or natural language. The geosciences are among them. Even within the geosciences, there is a considerable range of potential applications of machine learning and deep learning; some of them have been evidenced recently.

Our specific goal today will be to not only learn the state of a physical system through its observation and a prior of this state but also to correct its dynamics.This contrasts with traditional data assimilation where the model is usually assumed to be known, or corrected via only a bunch of parameters in the control variables. 

__This MOOC is organised into four parts:__

1. This theoretical introduction (intro), which you might be tempted to skip if you are not interested in the mathematical rationale.
2. The toy model that we will try to learn is introduced, assuming we already have an approximation. The *ensemble Kalman filter* data assimilation method is applied to the observations of the true model using our best approximation of this true model (part 1) and provides an analysis of the full true model trajectory.
3. A correction to the approximate model is then learned through *machine learning* using the approximate model and the analysis obtained from part 1 (part 2).
4. Finally, the *hybrid surrogate* model (i.e., the approximate model together with our machine learning correction) is tested and evaluated (part 3).

This will be followed by a small set of questions about the MOOC.



## Credits
This jupyter notebook has been created by Marc Bocquet and Julien Brajard
for the ECMWF MOOC of 2023 on Machine Learning in Weather & Climate. It has been reviewed and improved by Alban Farchi, Sophie Mauran and Laurent Bertino.
It also benefited from pieces of code previously developed by Marc Bocquet, Julien Brajard and Alban Farchi.


## Before running the notebook
Please, have a look at the introductory part.

#### For that, you to install the jupyter addon rise https://rise.readthedocs.io/ via pip install rise in your conda mooc environment.
Run the introductory notebook:
- Part Intro [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) ](https://colab.research.google.com/github/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_3/data_assimilation/mooc_ecmwf_bocquet_brajard_intro.ipynb)
[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_3/data_assimilation/mooc_ecmwf_bocquet_brajard_intro.ipynb)

and then activate the rise slideshow mode.

#### It can also be displayed as a pdf file:
https://github.com/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_3/data_assimilation/mooc_ecmwf_bocquet_brajard_intro.pdf

## Run the notebooks on google colab
Just run each notebook starting with the part 1:
- Part 1 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) ](https://colab.research.google.com/github/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_3/data_assimilation/mooc_ecmwf_bocquet_brajard_part1.ipynb)
[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_3/data_assimilation/mooc_ecmwf_bocquet_brajard_part1.ipynb)

- Part 2 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) ](https://colab.research.google.com/github/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_3/data_assimilation/mooc_ecmwf_bocquet_brajard_part2.ipynb)
[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_3/data_assimilation/mooc_ecmwf_bocquet_brajard_part2.ipynb)

- Part 3 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) ](https://colab.research.google.com/github/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_3/data_assimilation/mooc_ecmwf_bocquet_brajard_part3.ipynb) 
[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_3/data_assimilation/mooc_ecmwf_bocquet_brajard_part3.ipynb)


## Run the notebooks on you machine
1. Create the conda enviromment: ```conda env create -f environment.yml```
2. Activagte the enviromnment: ```conda activate mooc```
3. Run jupyter lab: ```jupyter lab```
4. Run the notebooks from the first (part 1) to the last (part 3)

## References
<span style="color:teal"> For more information about the ideas developed and exemplified in this mooc, please have a look at the following papers: </span>

* <font size="3"> Bocquet, M., Brajard, J., Carrassi, A., & Bertino, L. (2019). Data
assimilation as a learning tool to infer ordinary differential equation
representations of dynamical models. *Nonlin. Processes Geophys.*, *26*,
143--162. https://doi.org/10.5194/npg-26-143-2019  </font> <br /> 

* <font size="3"> Bocquet, M., Brajard, J., Carrassi, A., & Bertino, L. (2020). Bayesian
inference of chaotic dynamics by merging data assimilation, machine
learning and expectation-maximization. *Foundations of Data Science*, *2*, 55--80. https://doi.org/10.3934/fods.2020004  </font> <br /> 

* <font size="3"> Brajard, J., Carrassi, A., Bocquet, M., & Bertino, L. (2020). Combining
data assimilation and machine learning to emulate a dynamical model from
sparse and noisy observations: a case study with the Lorenz 96 model. *J. Comput. Sci.*, *44*, 101171.
https://doi.org/10.1016/j.jocs.2020.101171  </font> <br /> 

* <font size="3"> Brajard, J., Carrassi, A., Bocquet, M., & Bertino, L. (2021). Combining
data assimilation and machine learning to infer unresolved scale
parametrisation. *Phil. Trans. R. Soc. A*, *379*, 20200086.
https://doi.org/10.1098/rsta.2020.0086  </font> <br /> 

* <font size="3"> Farchi, A., Bocquet, M., Laloyaux, P., Bonavita, M., & Malartic, Q.
(2021). A comparison of combined data assimilation and machine learning
methods for offline and online model error correction. *J. Comput.
Sci.*, *55*, 101468. https://doi.org/10.1016/j.jocs.2021.101468  </font> <br /> 

* <font size="3"> Farchi, A., Laloyaux, P., Bonavita, M., & Bocquet, M. (2021). Using
machine learning to correct model error in data assimilation and
forecast applications. *Q. J. R. Meteorol. Soc.*, *147*, 3067--3084.
https://doi.org/10.1002/qj.4116  </font>
