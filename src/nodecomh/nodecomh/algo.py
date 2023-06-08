import numpy as np 
from datetime import datetime
import sympy as sym
import os 

log = np.log # The natural logarithm
log2 = np.log2 # Log base 2

class NRC_algo():
    initialized = False

    def __init__(self):

        if not NRC_algo.initialized:

                # Number of out neighbors. Since this simulation is just using two nodes, they each have one neighbor.
                self.out_neigh = 1 

                self.yi = 43.243 # if n=3 -> they are 3x1 zero matrices
                self.sigmai_y = 0                # 3x1 and 3x3. Gradient is 3x1 and hessian is 3x3

                # Each np.zeros is for node j1, j2. Will make more np.zeros if it has more neighbors...
                self.rhoi_y = 0

                self.sigmaj_y = 0

                self.path = os.path.join(os.getcwd() + "/src/nodecomh", "log_to_plot.txt")

                NRC_algo.initialized = True

    def data_reception(self, input_array):

        # Should get these values from node j: transmitter_node_ID, sigmaj_y and sigmaj_z 

        self.sigmaj_y = input_array[:1] # 1 her?
        print("received value:", self.sigmaj_y)
        print("yi før mass c", self.yi)
        self.yi = self.yi + self.sigmaj_y - self.rhoi_y
        print("yi etter mass c", self.yi)

        with open(self.path, mode="a") as f:
            f.write(f'{self.yi[0]} \n')

        self.rhoi_y = self.sigmaj_y 

    def data_transmission(self):
       
        # Push sum consensus
        print("yi før push-sum", self.yi)
        self.yi = (1/(self.out_neigh + 1)) * self.yi
        print("yi etter push-sum", self.yi)

        # These sigmas are broadcasted to the neighbors (just setting them global in the simulation)
        self.sigmai_y = self.sigmai_y + self.yi
       
        output_array = self.sigmai_y
        print("output_array:", output_array)
        print("-------")
        return output_array