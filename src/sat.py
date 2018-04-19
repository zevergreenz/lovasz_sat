#!/usr/bin/env python
"""
Solves SAT instance by reading from stdin using the Lovasz Local Lemma Sequential 
Solver algorithm or Random Solver (naive) algorithm.
"""
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
from argparse import FileType
from sys import stdin
from sys import stderr
from collections import Counter

from satinstance import SATInstance
from solvers import lovasz_sat
from solvers import random_sat

def main():
    args = parse_args()
    instance = None
    with args.input as file:
        instance = SATInstance.from_file(file)

    # Run several times for benchmarking purposes.
    result = []
    for _ in range(10000):
        assignment, count = args.algorithm.solve(instance)
        if assignment != None:
            result.append(count)
    print(Counter(result))

    if args.verbose and assignment != None:
        print('Found satisfying assignment:')
        print(instance.assignment_to_string(assignment,
                                            brief=args.brief,
                                            starting_with=args.starting_with))
    elif args.verbose:
        print('No satisfying assignment exists.', file=stderr)


def parse_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('-v',
                        '--verbose',
                        help='verbose output.',
                        action='store_true')
    parser.add_argument('-a',
                        '--all',
                        help='output all possible solutions.',
                        action='store_true')
    parser.add_argument('-b',
                        '--brief',
                        help=('brief output:'
                              ' only outputs variables assigned true.'),
                        action='store_true')
    parser.add_argument('--starting_with',
                        help=('only output variables with names'
                              ' starting with the given string.'),
                        default='')
    parser.add_argument('--random',
                        help='use the random algorithm.',
                        action='store_const',
                        dest='algorithm',
                        default=lovasz_sat,
                        const=random_sat)
    parser.add_argument('-i',
                        '--input',
                        help='read from given file instead of stdin.',
                        type=FileType('r'),
                        default=stdin)
    return parser.parse_args()


if __name__ == '__main__':
    main()
