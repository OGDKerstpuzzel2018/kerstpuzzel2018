#!/usr/bin/python3

# -----------------------------------------------------------------------------
# name: Your Name (your.name@organization.nl)
# algo: ?
# -----------------------------------------------------------------------------

import sys, getopt, json


def run_your_fancy_algorithm(W, D, l, b):
    """Convert BCPP(W, D, l, b) into array of placements"""
    placements = []

    #
    # Do your magic here!
    #

    # Just adding two dummy placements similar to what your algo will do
    p = Placement(0, 0, "H")
    if p.is_sane(W, D, l, b):
        placements.append(p)
    p = Placement(W-b, D-l, "V")
    if p.is_sane(W, D, l, b):
        placements.append(p)
    return placements


class Placement:
    """Simple object representing a placement"""
    def __init__(self, x: int, y: int, o: str):
        """Constructor"""
        self.x: int = x
        self.y: int = y
        self.o: str = o

    def is_sane(self, W, D, l, b):
        """Sanity check w.r.t. the space bounds"""
        return  (self.x >= 0) \
            and (self.y >= 0) \
            and (self.x + (l if self.o == "H" else b) <= W) \
            and (self.y + (l if self.o == "V" else b) <= D)


class PlacementEncoder(json.JSONEncoder):
    """Special encoder for Placements to facilitate JSON exports"""
    def default(self, obj):
        if isinstance(obj, Placement):
            return [obj.x, obj.y, obj.o]
            # Let the base class default method raise the TypeError
            return json.JSONEncoder.default(self, obj)


def print_usage():
    """Print the invocation usage"""
    print('kerstpuzzel.py <W> <D> <l> <b>')


def check_preconditions(W, D, l, b):
    """Make sure the preconitions on the input is met"""
    if W <= D:
        print('W must be greater than D')
        sys.exit(2)
    if l <= b:
        print('l must be greater than b')
        sys.exit(2)
    if l > W or b > D:
        print('invalid l,b cannot be placed within WxD area')
        sys.exit(2)


def main(argv):
    """Application entry point"""
    W, D, l, b = 0, 0, 0, 0;
    try:
        opts, args = getopt.getopt(argv,"h",["help"])
        W = int(args[0])
        D = int(args[1])
        l = int(args[2])
        b = int(args[3])
    except (getopt.GetoptError, IndexError, ValueError):
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print_usage()
            sys.exit()
    check_preconditions(W, D, l, b)
    placements = run_your_fancy_algorithm(W, D, l, b)
    print(json.dumps(placements, cls=PlacementEncoder))


if __name__ == "__main__":
    main(sys.argv[1:])
