# Dockerizing a CPU program:
This is a hands on demo tutorial, showing how scikit-surgerydocker package could be used to dockerize the Python application.
In this demo we are dockerizing [cpu-ex](https://github.com/UCL/cpu-ex) program. 

## About cpu-ex program:
The cpu-ex is short for CPU-Example, which means that the program does not require GPU for execution (For programs requiring GPU, see the next example). The cpu-ex is mimicing what a real world algorithm/program will do on execution i.e. 

1. Read the input file `input_file.txt` from the `cpu-ex/input_data` directory
1. Process it, append more lines to the existing text
1. Store the output in newly created file `output_file.txt` in `cpu-ex/output_data`.

## Step 1: Clone the projects
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
│   ├── input
│   ├── src
│   └── tests
│       └── data
└── scikit-surgerydocker
    ├── input_data
    ├── output_data
    └── src
```

## Step 2: Copy the code
Second step is to copy the application/algorithm code from your project (cpu-ex) to scikit-surgerydocker
```
cp -r cpu-ex/src/* scikit-surgerydocker/src/
```

## Step 3: Copy the input data
Third step is to copy the input data to `scikit-surgerydocker/input_data` directory. In cpu-ex project the input data is stored in `cpu-ex/input` directory. 
```
cp -r cpu-ex/input/* scikit-surgerydocker/input_data/*
```
