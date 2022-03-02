import cProfile
import glob
import os
import sys
import re
import inspect
import ast
from inspect import getfullargspec
import line_profiler
import memory_profiler
import gprof2dot
import flake8





@profile@profile
def multiplication(a):
    result = a*4
    print(result)


@profile@profile
def addition():
    result = 3+4
    print(result)



multiplication()
addition()
multiplication(a)
addition()
