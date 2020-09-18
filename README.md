# Pytest
> #### Topics to be covered:
>- Introduction to unit testing
>- Why Pytest?
>    - Pytest vs unittest
>- Introduction to Pytest - Arrange, Act & Assert
>    - Running our first test using pytest
>    - Pytest assertions
>    - Pytest test discovery conventions
>    - Structuring unit tests within our project(layouts).
>    - Pytest skip
>- Pytest Exception Handling
>- Pytest Marking
>- Pytest Fixtures
>- Parametrized Test Functions
>- Combining Test Fixtures and Parametrized Test Functions
>- Mocking
>- Debugging pytest

## Introduction
#### Definition
- Unit testing involves testing individual components of the software program or application.   
- The main purpose behind this is to check that all the individual parts are working as intended.  
- A unit is known as the smallest possible component of software that can be tested.  
- Generally, it has a few inputs and a single output.

#### Advantages
- Quality of Code
- Find Software Bugs Easily
- Facilitates Change
- Provides Documentation
- Debugging Process
- Design
- Reduce Costs

## Pytest Introduction
#### Test Discovery Conventions
If no arguments are specified then test files are searched in locations from test paths (if configured) 
or the current directory. Alternatively, command line arguments can be used in any combination of directories, 
file names or node ids.

In the selected directories, pytest looks for test_*.py or *_test.py files. 
In the selected files, pytest looks for test prefixed test functions outside of class 
and test prefixed test methods inside Test prefixed test classes (without an __init__() method).

#### Pytest related modules to explore.
>https://pypi.org/project/pytest-mock/
>
>https://pypi.org/project/pytest-cov/
 

