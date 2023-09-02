import os

x=str(input("Enter X: "))
y=str(input("Enter Y: "))

file_name = os.popen(f"cat {x}/Spell_{y}.txt ").read().split('\n')[0]
os.system(f"python3 spellbook/{file_name}.py")