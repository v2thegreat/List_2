# List_2

List_2 is a wrapper on NumPy's array to enable it to act as a Python list.

This is done to __increase the memory efficiency in Python code__ while enhancing code flexibility, as well as adding the functionality of both NumPy's array and Python list so that they can be used together

## Getting Started

### Choosing the Right Version

There are two variations of the list_2 module, and are as follows:

##### Cythonised Version:

###### Pros:
* 100x Faster than Default Python version

###### Cons:
* Compatable only with Python 3.6
* Runs only on Windows
* Difficult to modify and make changes

##### Python Version:

###### Pros:
* Compatible with every Python version
* Runs on all Operating Systems without issues
* Easy to make changes and modify

###### Cons:
* Extremely Slow

#### Prerequisites:

Running List_2 requires the python module: __NumPy__ and no additional modules

##### Installing NumPy:

Installing Numpy can be done by following the official [Numpy documentation](https://docs.scipy.org/doc/numpy-1.10.1/user/index.html)

### Installing list_2

#### Installing Cythonised list_2

##### Installing via pip:

__This has not been released on pip yet__

Installing via pip by the following prompt (on the command prompt):

```
pip install clist_2
```

__*Note:*__ Future versions are likely to impliment the cythonised version of list_2 as the default version, making the prompt:

```
pip install list_2
```

##### Physical Installation:

Simply download the list_2 file from [here](link.for.downloading) and place it in the ```C:\Program Files\Python36\Lib``` folder

__*Note:*__ This method of installation has the issue that running tests becomes slightly tedious, as they have to be downloaded and run.

Further, this is only a temprory fix, and is likely to be removed in the future when pip installation becomes reliable/wheels are avalible from the authors end.

Finally, it should be noted that this method is the most reliable. BUT it should also be noted that the author has not tested it out, and would change this comments after he tests it out at the official release

#### Installing Python Version:


##### Installing via pip:

Installing via pip by the following prompt (on the command prompt):

```
pip install list_2
```

__*Note:*__ Future versions are likely to impliment the cythonised version of list_2 as the default version, making this Python Distribution obselete

##### Physical Installation:

Simply download the list_2 file from [here](link.for.downloading) and place it in the ```C:\Program Files\Python36\Lib``` directory

__Notes:__ This method of installation has the issue that running tests becomes tedious, as they have to be downloaded and run.

Further, this is only a temprory fix, and is likely to be removed in the future when pip installation becomes reliable/wheels are avalible from the authors end.

Finally, it should be noted that this method is the most reliable. BUT it should also be noted that the author has not tested it out, and would change this comments after he tests it out at the official release

## Running the Tests

### Unit Tests
<!-- Tests for list_2 are written with the assistance of unit tests, and they can be executed by the following command on the IDLE:

```
>>> from list_2 import list_2_testing
>>> list_2_testing.run_tests()
```

 -->

Tests for list_2 are written with the assistance of Python's unit tests.
Download the unit tests from the github repositiory [here](link.for.download) and execute them.

It should be noted that unit tests for the following functions hasn't been written:

* `__lt__`
* `__gt__`
* `__le__`
* `__ge__`
* `__repr__`

This is because these functions haven't been implimented yet, with the exception of `__repr__` function, which wasn't seen as nessesary.


### Speed Tests

Speed/Performance tests are written as comparasion between Python's default list and list_2's functions. You can download them [here](link.for.download)

It should be noted that most functions in list_2 are slower as compaired to list_2 for the following reasons:

* Python lists are written in C, which faster
* List_2 python version is written in Python, on Python functions, and is hence slower

For these two reasons, the Python version is slower. In an attempt to speed up the code, Cythonised versions are the ones that are faster as well (but still not faster than Python lists, but work is being done on that)

Cythonised versions aren't ready yet, but they will by the end Jan. of 2018

### Memory Tests

Memory Tests aren't written, but they can be checked with the following commands:

```
>>> from sys import getsizeof
>>> from list_2 import list_2
>>> l = list(range(1000))
>>> l2_intType = list_2(range(1000), dtype=int)
>>> l2_objectType = list_2(range(1000))
>>> print(getsizeof(l), getsizeof(l2_intType.arr), getsizeof(l2_objectType.arr))
9112 4096 8096
```

This example clearly shows that the list_2 takes less space compared to default Python lists.

## Usage

### As a more memory efficient Python list

Using it as a Python list can be setup in the following manner:

```
from list_2 import list_2
```

and using

```
l=list_2()
```

instead of 

```
l=list()
```

or 

```
l=[]
```

### As a Numpy Array

Using the list_2 as a Numpy Array is pretty simple; by following the following format: `<list_2 object>.arr` you can use the list_2 as a numpy array.
This is because the Numpy Array object is located with the attribute name: `arr`

### As something in between the two

Using the list_2 object can be used in a flexible manner; such as that the developer can switch seemlessly between using it as a list and an array without problems. 

#### For Example

The following operations are considered valid:
```
>>> l2=list_2(range(10))
>>> l2.arr *= 3 #multiplying all the elements of the container by 3, and hence invoking it as a Numpy Array
>>> l2.append(5) #appending 5 to the end of the container, and hence invoking it as a Python list
>>> print(l2)   #displaying the list to confirm
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 5] #Yep seems right
>>>
```
