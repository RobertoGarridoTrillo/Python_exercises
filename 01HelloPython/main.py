def print_hi(name):
    print("Hello, {:>30}".format(name))


def print_bye(name):
    print("Bye,{:_>33}".format(name))


if __name__ == '__main__':
    print_hi('World!')
    print_bye('Galaxy!')
