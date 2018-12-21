#!/usr/bin/python3

# -----------------------------------------------------------------------------
# name: Your Name (your.name@organization.nl)
# algo: ?
# -----------------------------------------------------------------------------

import argparse
from collections import namedtuple
from json import dumps

Placement = namedtuple('Placement', ['x', 'y', 'o'])


def run_your_fancy_algorithm(W, D, l, b):
    """Convert BCPP(W, D, l, b) into array of placements"""
    placements = []
    #
    # Do your magic here!
    #
    p = Placement(0, 0, "H")
    placements.append(p._asdict())
    return placements


def parse_arguments():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] <W> <D> <l> <b>',
        description='OGD kerstpuzzel 2018',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='kerstpuzzel.py <W> <D> <l> <b>')
    parser.add_argument('W', type=int, help='Width parking space')
    parser.add_argument('D', type=int, help='Depth parking space')
    parser.add_argument('l', type=int, help='length camper')
    parser.add_argument('b', type=int, help='breadth camper')
    args = parser.parse_args()
    if args.W <= 0 or args.D <= 0 or args.l <= 0 or args.b <= 0:
        parser.error('All values must be greater than 0')
    if args.W < args.D:
        parser.error('W must be greater than or equal to D')
    if args.l < args.b:
        parser.error('l must be greater than or equal to b')
    if args.l > args.W or args.b > args.D:
        parser.error('invalid l,b cannot be placed within WxD area')
    return args.W, args.D, args.l, args.b


def main():
    """Application entry point"""
    W, D, l, b = parse_arguments()
    placements = run_your_fancy_algorithm(W, D, l, b)
    print(dumps(placements))


if __name__ == "__main__":
    main()
