# base64_random

Generates a Base 64 random number of an arbitrary length.

base64_random uses Python's `secrets` module to generate cryptographically secure random numbers.

## Usage
There are two main ways to use this package, command line invocation and importing the module. 

### Command Line Invocation
Command line usage is quite easy, simply pass the module the length of number you wish to generate:

```shell
python -m base64_random 10
```

### Python module usage
You can also import this module in your code to use it:

```python
from base64_random import gen_random_base64

base64_number = gen_random_base64(10)

print(base64_number)
```

## Installation
