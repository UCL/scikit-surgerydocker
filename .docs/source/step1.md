# Dockerizing a CPU program:
This is a hands on demo tutorial, showing how scikit-surgerydocker package could be used to dockerize the Python application.
In this demo we are dockerizing [cpu-ex](https://github.com/UCL/cpu-ex) program. 

## About cpu-ex program:
The cpu-ex is short for CPU-Example, which means that the program does not require GPU for execution (For programs requiring GPU, see the next example). The cpu-ex is mimicing what a real world algorithm/program will do on execution i.e. 

1. Read the input file `input_file.txt` from the `cpu-ex/input_data` directory
1. Process it, append more lines to the existing text
1. Store the output in newly created file `output_file.txt` in `cpu-ex/output_data`.

## Clone the projects
First step is to clone both the projects.

It is recommended to create a new directory.
```
# Make temp directory
mkdir temp
# Change directory to temp
cd temp
```
To clone scikit-surgerydocker:
```
git clone https://github.com/UCL/scikit-surgerydocker.git
```
To clone the project to containerise:
```
https://github.com/UCL/cpu-ex.git
```
Now the temp directory will have the following structure
```
temp
├── cpu-ex
│   ├── docs
│   │   └── source
│   ├── project
│   │   ├── input
│   │   └── output
│   └── tests
│       └── data
└── scikit-surgerydocker
    ├── docs
    │   └── source
    ├── project
    │   ├── input
    │   └── output
    └── tests
        └── data
```

## Copy the code
Second step is to copy the application/algorithm code from your project (cpu-ex) to scikit-surgerydocker 









# Program execution without docker

First step is to clone the repository using the following command

```
git clone git@github.com:UCL/scikit-surgerydocker.git
```

To run the python application directly

```
cd scikit-surgerydocker/project
python3 app.py
```

On execution the python program will:

1. Read the text file `input_file.txt` from the `scikit-surgerydocker/project/input` directory
2. Append more lines to the existing text
3. Store the whole text in a newly created file `output_file.txt` in `scikit-surgerydocker/project/output`.

You can check the `output_file.txt` after executing `app.py`.

```
cd ./output
cat output_file.txt
```
