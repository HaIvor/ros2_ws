# Summary

The ROS 2 structure with only the push-sum consensus between two nodes by the use of the unet simulations. 


## About 

A code developed from https://github.com/Brovidius/ROS2_nodecomx where the ra-NRC was simplified down into the algo.py. Some functions still remains from the ra-nrc that doesn't need to be there, such as how the values are processed with converters etc., but due to limited time the consensus algorithm on algo.py was prioritized. The setup will still work, it will just go through some unneccesary steps. 

## Important notes 

Since this includes float16 transmissions, some problems could occur due to the float16 rounding behavior. This is because our "mass counters" ($\sigma_i$ / $\rho_i$) gets so large. The higher the number, the worse of an approximation the float16 will make. This will cause shaky results after a certain number of transmissions. The results will be worse the higher the starting values since the mass counters will increase more rapidly. 

The folder setup is like this to illustrate how the plotting was setup, but the important part to take from this for further development is the package nodecomx in src which can be be added to the ROS project. Nodecomx and nodecomh runs the same stuff, just different starting values on the $y_i$ which is the value we want to come to a consensus. In reality only one nodecom is needed, but this is done to plot the results. 

## Running the code

If you download the whole ROS workspace, you may need to delete the folders "build", "install" and "log", then *colcon build* again in the terminal to get them back. 

To run the two nodes, 6 terminal windows were opened where every one was sourced (source install/local.setup.bash), then the following commands were ran in ~ros2_ws folder:

### For node 1

terminal 1
```
ros2 run nodecomx receiver
```
terminal 2
```
ros2 run nodecomx processing
```
terminal 3
```
ros2 run nodecomx transmitting 
```

### For node 2
terminal 4
```
ros2 run nodecomh receiver
```
terminal 5
```
ros2 run nodecomh processing
```
terminal 6
```
ros2 run nodecomh transmitting 
```

## The results

![Consensus](consensus.png)