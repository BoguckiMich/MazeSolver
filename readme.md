# Maze solvers

Idea to solve mazes with two different approaches. First one is about working with picture, and second one is about recursion.

# What you can find in here?

1. OpenCvSolver - based on `OpenCV` library to create one path based only on picture. - **_Still working_**
2. RecursionSolver - based on recursive function

# What do you need?

- Python 3+
- OpenCV for Python
- Numpy
- Pillow

# How to run?

1. **OpenCvSolver** -  run ```python OpenCvSolver.py name_of_the_file.extension``` to create solution
    - you will receive many pictures from steps I did to get solution - to close them just press any key
    - after finish you should receive file: <code>name_of_the_file_solution.png</code> - **_work in progress_**
    
2. **RecursionSolver** - run ```python RecursionSolver.py -th name_of_the_file.extension``` to create solution
    - <code>-th</code> parameter is to set thickness of the walls,*it is not required*, because this solution base on white spaces between walls
    - you will receive many pictures from steps I did to get solution - to close them just press any key
    - on this step you can verify is the thickness is to low of to big - default value is set to 4. Max value I used was 
    8 in some examples, and min value was 3 for bigger mazes.
    - after finish you should receive file: <code>name_of_the_file_solution.png</code> where you will receive green path
    as solution and red paths as terrain where recursion also checked the maze

# What can be improved?

**My experience**

Improve or implement algorithms to second version of app

Solution to the first app

Backtracking in second app

***

### Author
Pichael :) 
