# scikit-surgerydocker
Scikit-srugerydocker is a template project which can containerize (create docker image) of your Python project/algorithm with minimal efforts. It also specify the steps of how to share the your project with the world in an easy way without any charge. If your project/algorithm gets input data, do processing and produce results (as shown in the directory tree below) then you can use scikit-surgerydocker to containerise your project/algorithm for easy sharing and research reproducability. It further explains how you can download and use the shared image on remote user's computer.

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

The documentation describes the containerization of two example projects. First example showing the CPU program ([cpu-ex](https://github.com/UCL/cpu-ex)) and the other showing the GPU program ([stereo-recon-example](https://weisslab.cs.ucl.ac.uk/ThomasDowrick/stereo-recon-example)). The documenation also explains how you can compress and upload your newly created docker image to a docker registry for easy sharing. It further explains how you can download and use the shared image on remote user's computer.

Another related project [scikit-surgerychallange](https://github.com/UCL/scikit-surgerychallenge) could be used to download the docker image from the cloud repository and run it on different dataset. This can be particularly useful for hosting efficiency of containarized algorithm by providing specific hardware resource (RAM size, CPU, Number and type of GPU's) and specific execution time to each docker image. Together the scikit-surgerydocker and scikit-surgerychallange can be used to host research challanges.