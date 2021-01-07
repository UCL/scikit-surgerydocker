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
