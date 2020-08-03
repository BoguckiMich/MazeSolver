# Maze solvers

Idea to solve mazes with two different approaches. First one is about working with picture, and second one is about recursion.

# What you can find in here?

1. OpenCvSolver - based on `OpenCV` library to create one path based only on picture.
2. RecursionSolver - based on recursive function

# What do you need?

- Python (version 3.6+)
- OpenCV for Python (version 4.2+)
- Numpy (version 1.19+)
- Pillow (version 7.2)

To install these dependencies use ```pip install name_of_dependency``` for example ```pip install OpenCv-python```.

# How to run?

1. **OpenCvSolver** -  run ```python OpenCvSolver.py name_of_the_file.extension``` to create solution
    - you will receive many pictures from steps I did to get solution - to close them just press any key
    - after finish you should receive file: <code>name_of_the_file_solution.png</code> in the folder directory of maze picture
    
2. **RecursionSolver** - run ```python RecursionSolver.py -th name_of_the_file.extension``` to create solution
    - <code>-th</code> parameter is to set thickness of the walls,*it is not required*, because this solution base on white spaces between walls
        if there is too much white space between wals, probably will get *MemoryError:stack overflow*
    - you will receive many pictures from steps I did to get solution - to close them just press any key
    - on this step you can verify is the thickness is to low of to big - default value is set to 4. Max value I used was 
    8 in some examples, and min value was 3 for bigger mazes.
    - after finish you should receive file: <code>name_of_the_file_solution.png</code> where you will receive green path
    as solution and red paths as terrain where recursion also checked the maze

# What can be improved?

**My experience**

*Improve or implement algorithms to second version of app* - There are algorithims to solve maze faster. But I dont know much about them.
Examples are: Dijkstra's algorithm, BFS algorithm, Flood fill algorithm

*Backtracking in second app* - Because of very big amount of operation done in recursion, I should upgrade 
this function by **marking** the places where during the recursion, there is more than one corridor to take turn,
and after reaching wall, go back to latest marked point instead of checking every one on the way back.

***

### Author
Pichael :) 
