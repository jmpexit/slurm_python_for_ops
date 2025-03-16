#!/bin/python3
import argparse
import sys

# ./{prog_name} 1 2 3
# ./{prog_name} -v rtgr


# def main():
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument("json_file")
#     args = parser.parse_args()
#
#     print(args)
#     print(args.json_file)
#     print(type(args.json_file))

    # python task_060201_TOLAUNCH_TEXT_argparse.py test.json


def main():
    parser = argparse.ArgumentParser(description="Convert yaml to json", prog="main",
                                     epilog="WAIT FOR YOUR MR")

    subparsers = parser.add_subparsers(title="My subparcers", # группа вложенных парсеров
                                       help="My subparcers help")

    subparser_1 = subparsers.add_parser(name="yaml", help="yaml help")
    subparser_2 = subparsers.add_parser(name="json", help="json help")

    subparser_1.add_argument("-y", "--yaml_file", metavar="path/to/your/daemon.yaml",
                        help="path to yaml with docker daemon config", required=True)
    subparser_2.add_argument("-j", "--json_file")
    subparser_2.add_argument("-v", dest="is_validate", help="is need validation") #, nargs="+")
                                        # nargs : + - at least 1; * - any: ? - 0 or 1; const number - exact number

    args = parser.parse_args()

    print(args)


if __name__ == '__main__':
    main()