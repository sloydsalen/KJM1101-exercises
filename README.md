# KJM1101 exercises
This is collection of programming exercises for KJM1101 at UiO. The exercises are made/assigned in Jupyter Notebook using NBGrader.

## Adding exercises
1. Create a sub-directory in the source directory.
2. Create the notebook exercise in the directory.
3. In the `nbgrader_config.py` file, add the directory name of the assignment to the dictionary `c.NbGrader.db_assignments`.
4. In a terminal run `nbgrader assign <exercise name>` which will create the corresponding sub-directory in the release directory.

## Releasing exercises
Run `nbgrader release <exercise name>`.

# Useful links
- [NBGrader](https://github.com/jupyter/nbgrader)
- [NBGrader demo](https://github.com/jhamrick/nbgrader-demo)
- [NBGrader plotchecker](https://github.com/jhamrick/plotchecker)
- [NBConvert](https://github.com/jupyter/nbconvert)
- [MyBinder beta](https://beta.mybinder.org/)
