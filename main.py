from argparse import ArgumentParser
from scanner import Scanner


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('target', help='Target IP / Hostname')

    args = parser.parse_args()
    target = args.target

    scanner = Scanner(target=target)
    scanner.scan_run()
