# python-workshops-phase-1-unit-e-hw
Practice Problems for Unit 1E of Python Workshops

# Explaining What is going on

Hopefully you have this open in VS Code. If not you should have gotten a link to clone this repo onto your computer. You can then open the folder (the repo) that was cloned in VS Code. Use the "Mark Down All in On" Extension to open this readme.md file to see it easier. The button should be in the top right area of the screan. 

We will be using Github Classroom to make grading easier. This will let you automatically see your grade every time you upload (or push) your work. I will walk you through how to do that. 


# What will be graded?

In this unit, file `unit_1e_hw.py` will be graded. That is the file you will want to modify. You can see how it will be graded in the `test_unit_1e_hw.py` file. The goal is to pass all tests in the `test_unit_1e_hw.py` file. 
<br><br>
Lets start by passing one test, seeing if we passed it locally, then uploading it to Github Classroom to get your grade. 
<br><br>
# Saving and Grading your Code using gitterpy.py
## EML Git Automation Script
This Python script automates the process of committing and pushing changes to a Git repository or running pytest in a more streamlined manner.

## Usage
- To use this script, simply place it in the git repository's parent folder (where you can find a folder named .git) 

     - .git is a hidden folder; so you may need to unhide files first; or run the following commands and search for .git  
        (MAC/Linux)  
        `ls -a`  
        (Windows)   
        `dir /a`

- Run gitterpy with the appropriate argument. For example, to run pytest (to evaluate your work locally), use the following command:

    `python gitterpy.py test`

- To (submit) commit and push changes to the remote Git repository, use the following command:

    `python gitterpy.py upload`

If any errors occur during the push, the script will print an error message.

GitterPY Source: https://github.com/RSounder/gitterPy
