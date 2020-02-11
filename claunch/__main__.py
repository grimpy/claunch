import argparse
from .claunch import Claunch

def main():
    launcher = Claunch()
    parser = argparse.ArgumentParser()
    parser.add_argument("--start")
    parser.add_argument("--stop")
    options = parser.parse_args()
    if options.start:
        launcher.start(options.start)
    elif options.stop:
        launcher.start(options.stop)
    else:
        print("Launch items:")
        for config in launcher.list():
            print(f"* {config['name']}")


if __name__ == '__main__':
    main()
