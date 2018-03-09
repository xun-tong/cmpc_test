#ifndef MPC_CONST_H
#define MPC_CONST_H

#include "mpc_base.h"



enum { 
MPC_HOR = 19,  /**< MPC prediction horizon. */
MPC_STATES = 8,  /**< Number of system states. */
MPC_INPUTS = 3,  /**< Number of system inputs. */
MPC_MXCONSTRS = 0, /**< Number of mixed stage constraints. */
MPC_HOR_INPUTS = 57,  /**< Horizon times number of inputs. */
MPC_HOR_STATES = 152,  /**< Horizon times number of states. */
MPC_HOR_MXCONSTRS = 1  /**< Horizon times number of mixed constrained
plus the number of end state constraints. */
}; 

#endif /* MPC_CONST_H */
