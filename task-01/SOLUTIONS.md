# COMMANDS USED 
## 1.cd
Used to change directory
## 2.la
lists out the contents of the current directory including hidden files
## 3.nvim
this command lets you edit a file in neovim, it also creates the file if it doesn't exist
## 4.cp
let's you copy and paste a specified file to a certain destination.
## 5.mv
does the function of cutting and pasting. similar to the cp command. also is used to remane a file.
## 6.mkdir
a very important command which allows the user to create a new directory.
## 7.rm 
used to remove a certain file or folder.
## 8.python3
used to run a python script

# GIT COMMANDS USED
## 1.git clone
used to clone a certian repository
## 2.git status
used to check the status of the git repo, ie modifications,staged or staged etc
## 3.git add
used to add a file to the repo
## 4.git commit 
commits the changes and new additions to the repo and makes a log
## 5.git push
finally pushes the changes to the remote repository
## 6.git branch -a
used to list the all the branches (including remote ones) in the repo
## 7.git switch
used to switch branches and also return from detached head state
## 8.git checkout
used to goto a previous commit, puts you in detached head state

# SCRIPTING
I used the os module in python to easily do some repetative tasks

Here is the code used
```python
import os

x=str(input("Enter X: "))
y=str(input("Enter Y: "))

file_name = os.popen(f"cat {x}/Spell_{y}.txt ").read().split('\n')[0]
os.system(f"cp spellbook/{file_name}.py codes/")
os.system(f"python3 spellbook/{file_name}.py")
```
 
