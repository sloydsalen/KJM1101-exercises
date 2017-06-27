# KJM1101 exercises
This is collection of programming exercises for KJM1101 at UiO. The exercises are made/assigned in Jupyter Notebook using NBGrader.

## Adding exercises
1. Create a sub-directory in the source directory.
2. Create the notebook exercise in the directory.
3. In the nbgrader_config.py file, add the directory name of the assignment to the dictionary c.NbGrader.db_assignments.
4. In a terminal run `nbgrader assign <exercise name>` which will create the corresponding sub-directory in the release directory.
