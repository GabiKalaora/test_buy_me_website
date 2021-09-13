import os
import sys


def main():
    arg = sys.argv[1:]
    if len(arg) <= 0:
        print("you need to pass all <filename>.py that needed for the program test!")
    path_to_volum = f"{os.getcwd()}/shared_with_container"

    os.mkdir("shared_with_container")
    os.system(f"cp {' '.join(arg)} {path_to_volum}")
    os.system("docker image build . -t joyzoursky/python-chromedriver:3.9-selenium")
    os.system(
        f"docker run -it -w /usr/workspace -v {path_to_volum}:/usr/workspace joyzoursky/python-chromedriver:3.9-selenium bash")


if __name__ == '__main__':
    main()
