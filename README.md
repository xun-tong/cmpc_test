# cmpc_test

The MPC problem setup description is found in `firefly.py`, which is here without disturbance states.   

The automatically generated code are in the `cmpc` directory.   


All the available constants are found in `cmpc/include/mpc_const.h`.    
`cmpc/include/mpc_base.h` includes the type definition real_t, which is the type for all numeric operations of the algorithm. By default, the generated code uses double precision float (64-bit) for all computations.     

`firefly_mpc.c` is a test file to make use of the generated code.

