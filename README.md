# KJM1101 exercises
This is collection of programming exercises for KJM1101 at UiO. The exercises are made/assigned in Jupyter Notebook using NBGrader.

# Workflow

## Adding exercises
1. Create a sub-directory in the source directory.
2. Create the notebook exercise in the directory.
3. In the `nbgrader_config.py` file, add the directory name of the assignment to the dictionary `c.NbGrader.db_assignments`.
4. In a terminal run `nbgrader assign <exercise name>` which will create the corresponding sub-directory in the release directory.

## Releasing exercises
Run `nbgrader release <exercise name>` when the assignment is ready.

## Collecting submitted exersises
Run `nbgrader collect <exercise name>` after the due date to get ready for grading.

## Grading

### Autograde
Run `nbgrader autograde <exercise name>` to automagically grade the test cells.

### Manual grading
Run `nbgrader formgrade <exercise name>` to launch a grading server which can be opened in a web browser. Complete the grading there.

## Feedback
Run `nbgrader feedback <exercise name>` to generate web-based feedback for the students.

# Useful links
- [NBGrader](https://github.com/jupyter/nbgrader)
- [NBGrader demo](https://github.com/jhamrick/nbgrader-demo)
- [NBGrader plotchecker](https://github.com/jhamrick/plotchecker)
- [NBConvert](https://github.com/jupyter/nbconvert)
- [MyBinder beta](https://beta.mybinder.org/)
