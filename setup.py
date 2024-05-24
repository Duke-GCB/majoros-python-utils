from setuptools import setup, find_packages

# modules are all .py files starting with a capital letter
import os
import re

py_modules = [f[:-3] for f in os.listdir('.')
              if f.endswith('.py') and re.match(r'^[A-Z]', f)]

setup(
    name='majoros-utils',
    version='0.1.3',
    py_modules=py_modules,
    description="Majoros lab utility classes",
    author="Bill Majoros",
    author_email='"Bill Majoros" <martiandna@gmail.com>',
    license="GPL version 3"
)
