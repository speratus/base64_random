from .gen import gen_random_base64


def main():
    import sys
    from .gen import gen_random_base64

    length_str = sys.argv[1]

    length = int(length_str)

    print(gen_random_base64(length))
