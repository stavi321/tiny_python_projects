#!/usr/bin/env python3
"""
Author: me
Purpose: Say hello
"""

import argparse

#------------------------------------------------
def get_args():
    """Get command line argument"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='name to greet')
    return parser.parse_args()

#-----------------------------------------------------------
def main():
    """fill"""
    args = get_args()
    print('Hello, ' + args.name + '!')

#---------------------------------------
if __name__ == '__main__':
    main()
