# Program execution without docker

Clone the repository
```
git clone git@github.com:UCL/scikit-surgerydocker.git
```
To run the python application directly
```
cd scikit-surgerydocker
python3 app.py
```
On execution the python program will (1) read the text file `inputfile.txt` from provided `scikit-surgerydocker/input` directory, (2) append more lines to the existing text and (3) store the whole text in a newly created file `outputfile.txt` in `scikit-surgerydocker/output` directory provided in the project. You can check the `outputfile.txt` after executing `app.py`.

```
cd ./output
cat outputfile.txt
```
