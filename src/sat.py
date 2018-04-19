#!/usr/bin/env python
"""
Solves SAT instance by reading from stdin using the Lovasz Local Lemma Sequential 
Solver algorithm.
"""
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
from argparse import FileType
from sys import stdin
from sys import stderr

from satinstance import SATInstance
from solvers import lovasz_sat
from solvers import random_sat

__author__ = 'Sahand Saba'

def main():
    args = parse_args()
    instance = None
    with args.input as file:
        instance = SATInstance.from_file(file)

    assignments = lovasz_sat.solve(instance)
    count = 0
    for assignment in assignments:
        if args.verbose:
            print('Found satisfying assignment #{}:'.format(count),
                  file=stderr)
        # print(instance.assignment_to_string(assignment,
        #                                     brief=args.brief,
        #                                     starting_with=args.starting_with))
        count += 1
        if not args.all:
            break

    if args.verbose and count == 0:
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
                        help='use the iterative algorithm.',
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
