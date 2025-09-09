# Jax Jacobson
# 9/8/25
# CS 310 - W2 Filesystem Explorer.

## How do you list a directory? 
# Given we have already imported Path and set path='.' in the argument, the for loop: for x in Path(path).iterdir(): will
# iterate through the current directory. Setting a variable to x.resolve() will then give us the absolute path which we can print.

## What does 'argv' contain?
# sys.argv contains the command-like arguments passed to a Python script.