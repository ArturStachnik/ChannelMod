# ChannelMod
This is a program for modeling labyrinthine oil reservoirs in 2D. The program takes data from two separate wells and fixed grid values as a basis. The program generates a random channel modeling, but marked by previous values. The result is a .csv file with the position and width of the channels, as well as a graphical output that represents the results.

These wells intersect a series of sandy river channels. It is necessary to determine the grid values (valores_malla.csv), which include the position of the wells and the maximum area of sand that can exist between them, data that must be obtained from the characteristics of the river system. The program takes into account the channel compactness factor.

To run the program, it is necessary to:

1. Have the latest version of Python 3 installed.
2. Run the "dependencies.bat" file to install the necessary Python libraries.
3. Run the "ChannelMod.ps1" file using PowerShell.

A terminal window will open and prompt for dependent variables needed for the modeling.
The output of the modeling is a graphical representation of the channel location and a numerical result "Hoja1.csv".
