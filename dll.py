import os
os.system("color 6 && cls")
print("1. Single Player\n")
print("2. Two Player\n")

player = str(input("> "))

if player == "1":
	os.system("cd data1/data && run.bat")

if player == "2":
	os.system("cd data2/data && run.bat")

else:
	print("Please Type 1 or 2")