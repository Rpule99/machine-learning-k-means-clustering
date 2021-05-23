<h1 align="center"> Machine Learning K-Means clustering Algorithm</h1>

<div align="center" >
  <img src="https://img.shields.io/badge/made%20by-Zongo%20Maqutu-blue?style=for-the-badge&labelColor=20232a" />
  <img src="https://img.shields.io/badge/Python 3.8.5-20232a?style=for-the-badge&logo=python&labelColor=20232a" />
  <img src="https://img.shields.io/badge/Numpy-20232a?style=for-the-badge&logo=numpy&labelColor=162e16" />
  <img src="https://img.shields.io/badge/Pycharm-20232a?style=for-the-badge&logo=pycharm&labelColor=517a8a" />
</div>

## Table of Contents
* [Project Setup](#ProjectSetup)
* [Libraries Used](#libraries)
* [Future Scope](#FutureScope)
## Description 
*This is an implementation of the K-Means clustering algorithm written in Python. The numpy library is also used to calculate how similar points are to each other*
  

## Project setup  
To run this project clone this repository in a folder on your local machine.
We first need to build our virtual environment and install a list of 
libraries our program needs to run. To do this, open a terminal in the root directory and run the following commands

```
make install       // installs program dependencies
```


Next we need to activate our virual environment. To do this run the following commands

```
source venv/bin/activate       // Activates our virtual environment
```

Now we can run our algorithm. Run these commands and you will see details of each cluster, centroids belonging those clusters, and the
number of iterations the algorithm goes through before it converges

```
make runKMeans       // runs the program
```
To exit the virtual environment run:

```
deactivate       // runs the program
```
### Libraries Used
* Numpy


## Future Scope
* use the matplotlib to plot the points on a graph and show the clusters at each iteration
* Add animations to move the clusters and update points

<p align="center">Made with ❤️ with Pycharm and vim</p>


