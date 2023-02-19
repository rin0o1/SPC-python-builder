# SPC-python-builder

This script generates SPC code and ANDL models automatically to model mobility within Petri Nets using the Hyrbid Approach.
For additional information regarding this tool: []

## Input Parameters:
    * x : defines the x dimension for the grid environment. As default it is set to 3.
    * y : defines the y dimension for the grid environment. As default it is set to 3.
    * o : defines the number of instances for a Petri Net colour (complex object). As default it is set to 2.
    * c : defines the path of the Petri Net CANDL file.


## Output:
    This script will generate:
    * an ANDL file (generated-andl.andl) unfolding the CANDL provided
    * a SPC code (spcOut.spc) 

## Requirements:
    * Spike installed and set within the environment path

## How to use
    * prepare your candl for the BuilderANDL as described in this article []
    * write your SPC code within the BuilderSPC as illustrate in this article []

## Run the script
    ```
    python3 builder.py --x=x_grid_environment --y=y_grid_environment --o=no_complex_obejcts --c=candl_path
    ```
    Example:
    ```
    python3 builder.py --x=5 --y=6 --o=3 --c=./whaleExampleModel.candl
    ```