<!-- [![Build Status](https://travis-ci.com/UCL/scikit-surgerydocker.svg?branch=main)](https://travis-ci.com/UCL/scikit-surgerydocker)  -->
[![Documentation Status](https://readthedocs.org/projects/scikit-surgerydocker/badge/?version=latest)](https://scikit-surgerydocker.readthedocs.io/en/latest/?badge=latest)

# scikit-surgerydocker
This repo shows how to containerize (create docker image) of your Python project/algorithm. If your project/algorithm takes input data, process it and produce results (as shown in the directory tree below) then you can use scikit-surgerydocker to containerise your project/algorithm for easy sharing and research reproducability. 

```
.
├── input_data
│   ├── file-1
│   ├── file-2
│   └── file-n
├── output_data
│   ├── result-1
│   ├── result-2
│   └── result-n
└── src
    └── application.py
```

The documentation describes the containerization of two example projects. First example showing the CPU program example ([cpu-ex](https://github.com/UCL/cpu-ex)) and the other showing the GPU program example ([stereo-recon-example](https://weisslab.cs.ucl.ac.uk/ThomasDowrick/stereo-recon-example)). The documenation also explains how you can compress and upload your newly created docker image to a docker registry for easy sharing. It further explains how you can use the shared image on user's end.


Another related project [scikit-surgerychallange](https://github.com/UCL/scikit-surgerychallenge) could be used to download the docker image from the cloud repository and run it on different dataset. This can be particularly useful for hosting efficiency of containarized algorithm by providing specific hardware resource and time to each docker image. Together the scikit-surgerydocker and scikit-surgerychallange can be used to host docker challanges.  

## Documentation
The documentation of the project can be found on [readthedocs](https://scikit-surgerydocker.readthedocs.io/en/latest/).
