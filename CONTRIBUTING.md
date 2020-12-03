



# Contributing to scikit-surgerydocker


## Reporting bugs and feature requests

Please create a new [issue](https://github.com/UCL/scikit-surgerydocker/issues/new) on the issues list.

When reporting a bug, please include:
* The version of scikit-surgerydocker you are using
* Your OS version (for example Windows 10 64-bit, macOS High Sierra, Ubuntu 18.04)
* Detailed steps to reproduce the bug.

## How to contribute to scikit-surgerydocker

1. Find an [issue](https://github.com/UCL/scikit-surgerydocker/issues) you would like to work and assign it to yourself. You can also [add new issue](https://github.com/UCL/scikit-surgerydocker/issues/new/choose) to describe your own feature or bugfix.
1. Fork the repository
4. Create a branch for your changes. The branch name should start with the issue number, followed by hyphen separated words describing the issue. For example: `6-add-contribution-guidelines-to-the-repo`
5. Make your changes following the coding guidelines below.
6. Commit and push your changes to the branch on your fork. The commit message should start with `Issue #<issue number>: `, for example: `Issue #1: Fixed typo`. Commit in small, related chunks. Review each commit and explain its purpose in the commit message.
7. When finished, submit a merge request: 

## Design Considerations

1. As few dependencies as possible. Try to stick to standard packages like numpy and pandas etc.
2. Discuss extra dependencies with the team and maybe the outcome will be to create a new separate package, where you can be more specific and more modular.
3. Unit test well, using pytest, with good coverage.
4. All errors as exceptions rather than return codes.


## Coding guidelines

1. Please follow [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines.
2. Create a python virtual environment (virtualenv) for development
3. Make sure that pylint passes. You may disable specific warnings within the code where it is reasonable to do so
4. Include comments to make your code easily understandable.
5. Add unit tests for new and modified code
6. Make sure all existing and new tests pass
7. Make sure all docstrings have been added
8. Make sure all dependencies have been added to requirements
9. Make sure your code works for all required versions of Python
10. Make sure your code works for all required operating systems