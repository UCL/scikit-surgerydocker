[![Build Status](https://travis-ci.com/UCL/scikit-surgerydocker.svg?branch=main)](https://travis-ci.com/UCL/scikit-surgerydocker) [![Documentation Status](https://readthedocs.org/projects/scikit-surgerydocker/badge/?version=latest)](https://scikit-surgerydocker.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/UCL/scikit-surgerydocker/branch/main/graph/badge.svg?token=BGIXM5LW3C)](https://codecov.io/gh/UCL/scikit-surgerydocker)

# scikit-surgerydocker
This repo shows how to containerize (create docker image) of your project/algorithm. If your project/algorithm takes input data, process it and produce results (as shown in the directory tree below) then you can use scikit-surgerydocker to containerise your project/algorithm for easy sharing and reproducability. 

```
.
├── input
│   ├── file-1
│   ├── file-2
│   └── file-n
├── output
│   ├── result-1
│   ├── result-2
│   └── result-n
└── src
    └── application.py
```

The documentation describes the containerization of two example projects. One showing the CPU example and the other showing the GPU example. The documenation also explains how you can compress and upload your newly created docker image to a docker registry for easy charing. 


Another related project [scikit-surgerychallange](https://github.com/UCL/scikit-surgerychallenge) could be used to download the docker image from the cloud repository and run it on another dataset for finding efficiency of your containarized algorithm. Together the scikit-surgerydocker and scikit-surgerychallange can be used to host docker challanges.  

## Documentation
The documentation of the project can be found on [readthedocs](https://scikit-surgerydocker.readthedocs.io/en/latest/).
