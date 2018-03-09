r"""
.. default-role:: math

The system description
----------------------

The system considered is the Cessna Citation 500
aircraft presented in ([M02]_, p.64).  A continuous-time
linear model is given by `\dot{x} = A_c x + B_c u, y = C x`, where

.. math::
   A_c = \left[ \begin{matrix}
   -1.2822 & 0 & 0.98 & 0 \\
   0 & 0 & 1 & 0 \\
   -5.4293 & 0 & -1.8366 & 0 \\
   -128.2 & 128.2 & 0 & 0 \\
   \end{matrix} \right], \;\;
   B_c = \left[ \begin{matrix}
   -0.3 \\
   0 \\
   -17 \\
   0 \\
   \end{matrix} \right],
   C = \left[ \begin{matrix}
   0 & 1 & 0 & 0 \\
   0 & 0 & 0 & 1 \\
   -128.2 & 128.2 & 0 & 0 \\
   \end{matrix} \right],

and the state vector is given by `x = [x_1 \; x_2 \; x_3 \; x_4]^T`, where:

* `x_1` is the angle of attack (rad),
* `x_2` is the pitch angle (rad),
* `x_3` is the pitch angle rate (rad/s), and
* `x_4` is the altitude (m).

The only input `u_1` is the elevator angle (rad).
The outputs are `y_1 = x_2`,  `y_2 = x_4`, and `y_3 = -128.2 x_1 + 128.2 x_2`
is the altitude rate (m/s)

The system is subject to the following constraints:

* input constraints `-0.262 \leq u_1 \leq 0.262`,
* slew rate constraint in the input `-0.524 \leq \dot{u}_1 \leq 0.524`
* state constraints `-0.349 \leq x_2 \leq 0.349`,
* output constraints `-30.0 \leq y3 \leq 30.0`.

To consider the slew rate constraint in the input, we introduce an additional
state `x_5`. The sampling interval is `dt = 0.5` s, and the
horizon length is `N = 10` steps.

The controller parameters
-------------------------

The book [M02]_ proposes to use identity matrices of appropriate size for
the weighting matrices `Q` and `R`. We instead select them diagonal
with values that give a similar controller performance and much lower
condition number of the Hessian of the MPC quadratic program (see
:ref:`tuning.cond`),
a desirable property for any numerical algorithm.

"""

from numpy import diag  # similar effect with: from numpy import *

dt = 0.1
N = 19
# discrete-time system
Ad = [[1,	0,	0,	0.09995,	0,		0,	0,		0.0431908],
      [0,	1,	0,	0,		0.09995,	0,	-0.0430852,	0],
      [0,	0,	1,	0,		0,		0.1,	0,		0],
      [0,	0,	0,	0.999,		0,		0,	0,		0.810794],
      [0,	0,	0,	0,		0.999,		0,	-0.807829,	0],
      [0,	0,	0,	0,		0,		1,	0,		0],
      [0,	0,	0,	0,		0,		0,	0.67032,	0],
      [0,	0,	0,	0,		0,		0,	0,		0.675598]]
Bd = [[0,		0.00516734,	0],
      [-0.005261,	0,		0],
      [0,		0,		0.00495],
      [0,		0.151006,	0],
      [-0.153652,	0,		0],
      [0,		0,		0.1],
      [0.297306,	0,		0],
      [0,		0.292535,	0]]
# Weighting matrices for a problem with a better condition number
Q = diag([40, 40, 60, 20, 20, 25, 20, 20])
R = diag([35, 35, 2])
P = [[428.621,		0,		0,		108.103,	0,		0,		0,		108.491],
     [0,		427.748,	0,		0,		107.214,	0,		-106.405,	0],
     [0,		0,		563.584,	0,		0,		111.51,		0,		0],
     [108.103,		0,		0,		109.174,	0,		0,		0,		108.329],
     [0,		107.214,	0,		0,		108.248,	0,		-105.983,	0],
     [0,		0,		111.51,		0,		0,		111.486,	0,		0],
     [0,		-106.405,	0,		0,		-105.983,	0,		176.989,	0],
     [108.491,		0,		0,		108.329,	0,		0,		0,		182.576]]
# input constraints
u_lb = [[-0.436332],
	[-0.436332], 
	[-4.8066]] 
u_ub =  [[0.436332], 
	 [0.436332], 
	 [10.1934]]
