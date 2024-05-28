# ChannelMod
This is a program for modeling labyrinthine oil reservoirs in 2D. The program takes data from two separate wells and fixed grid values as a basis. The program generates a random channel modeling, but marked by previous values. The result is a .csv file with the position and width of the channels, as well as a graphical output that represents the results.

These wells intersect a series of sandy river channels. It is necessary to determine the grid values (valores_malla.csv), which include the position of the wells and the maximum area of sand that can exist between them, data that must be obtained from the characteristics of the river system. The program takes into account the channel compactness factor.

To run the program, it is necessary to:

1. Have the latest version of Python 3 installed in the system.
2. Run the "dependencies.bat" file to install the necessary Python libraries.
3. Run the "ChannelModExec.bat" file.
4. Introduce the desired iterations.
5. You need to close every generated plot in order to follow up with the iterations.

The output of the modeling is a graphical representation of the channel location and a numerical result "Hoja1.csv" for each iteration. If you want to save the generated file, it is mandatory to copy it to a desired destination before close the plot window.
You can save each generated plot by clicking the "save" icon present at the matplotlib UI.
