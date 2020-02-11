#! /Users/arunab/anaconda3/bin/python
import sys
import os

readme_file_name = "ReadMe.md"
chapter_no = "Chapter_"


if __name__ == '__main__':
    print("Hello World")
    program_name = sys.argv[0]
    arguments = sys.argv[1:]

    if len(sys.argv[1:]) > 2:
        print("Please pass only two  argument to the program. ", len(sys.argv[1:]))
        sys.exit(1)

    number = int(arguments[0])
    if number < 10:
        number = "0"+str(number)
    number = str(number)

    chapter_name = arguments[1]
    chapter_name.replace(" ", "-")
    print("progam name: ", program_name, " arguments: ", arguments)
    try:
        os.makedirs('DOCS/'+chapter_no+number+chapter_name+"/"+readme_file_name)
        os.makedirs('SRC/'+chapter_no+number+chapter_name+"/")
    except FileExistsError:
        print("The directory already exist")


