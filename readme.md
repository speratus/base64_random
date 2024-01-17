# base64-random

Generates a base 64 random number of an arbitrary length.

base64_random uses Python's `secrets` module to generate the random numbers, so you should be able to generate high
quality random numbers when using this library. That said, I cannot recommend that this library be used in contexts 
where high-quality random numbers are used to secure sensitive information. Please use a suitable cryptography library
for contexts where you need to protect information.

Please also note, that as of the time of writing, this library provides **NO SUPPORT** for Base64 encoding or decoding.
Additionally, this library generates numbers in base 64, it has no relation to the 
[Base64](https://en.wikipedia.org/wiki/Base64) encoding format.

## Usage
There are two main ways to use this package, command line invocation and importing the module. 

### Command Line Invocation
Command line usage is quite easy, simply pass the module the length of number you wish to generate:

```shell
python -m base64_random 10
```
Or, by invoking the shell script:
```shell
b64r 10
```

### Python module usage
You can also import this module in your code to use it:

```python
from base64_random import gen_random_base64

base64_number = gen_random_base64(10)

print(base64_number)
```

## Installation
`base64_random` is available on pip!

```shell
pip install base64-random
```

You can also install `base64-random` directly from git, but please refer to the 
[official documentation](https://pip.pypa.io/en/stable/getting-started/#install-a-package-from-github) for the details
of how to do that.

### Building from Source
If you wish to build `base64-random` directly from the source code, you can do that by following these steps:

1. Clone the repo from [GitHub](https://github.com/speratus/base64_random).
2. Install dependencies. I *highly* recommend that you use [`pipenv`](https://pypi.org/project/pipenv/) for this purpose. 
   The only dependencies are those required to build the library itself.
    1. If you do use pipenv to install dependencies, make sure to activate the shell environment by running `pipenv shell`.
3. Once dependencies are installed, simply run the python build module:
```shell
python -m build
```
4. If you have followed all the instructions correctly, then you should now have a `*.whl` file and a `*.tar.gz` file
    in the `dist` directory.
5. Once the wheel file is generated, you can install it by running `pipenv install dist/base64_random-<VERSION>.whl`.
    if you prefer to install with `pip`, you can do so by running the very similar command:
   `pip install dist/base64_random-<VERSION>.whl`.

You're done! You should now be able to import the library.