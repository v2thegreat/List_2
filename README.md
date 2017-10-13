# List_2

## What is it?

A Python List which acts as a wrapper for numpy which acts as a list.

## Objectives

  * Create numpy wrapper for numpy's array which causes it to work as lists
  * Enable the wrapper to take up less space than Python lists
  * Enable the wrapper to act on speeds that are faster than or similar speeds to Python Lists

## How Does it work?

Using numpy array's it's able to act as a list which doesn't take up as much space in the memory. 

So essentially, you're able to store data into list_2, work with it as if its a list. Your list can have billions of elements and you can probably run it on a rasberrii pi without having hardware issues (I think)!

## Wouldn't that make it slower than list?

Yep, but to counteract that, we use Cython to speed up the code! On my system, its about 1.056 10**-5 sec. times slower, which seems to be negligible

## How tested is this?

Not alot sadly, its going to be a while unit its going to reach the above mentioned objectives

## How do I use it?

Simple, to import:

```
from List_2 import list_2
```

To create an empty list

```
l = list_2()
```

You can also (for sake of easy writing):

```
from List_2 import list_2 as list
```

and to create an empty list

```
l=list()
```

Then, it can work on all functions in Python's lists or it tries to :P

## Shit doesn't work. What do I do?

Well, you have the code right here. Have a look at that and try to see if that helps, or try fixing it yourself (isn't that the point of opensource projects?)

If you still don't have any idea what's going wrong, either create an issue, or email me on [here](mailto:v2thegreat@gmail.com).