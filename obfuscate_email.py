#!/usr/bin/python

"""Convert a string into its HTML entities"""
#https://codereview.stackexchange.com/questions/205103/python-program-that-obfuscates-an-email-address


import argparse


def command_line_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('string_to_mung', help='String to convert')
    parser.add_argument('-l', '--link', action='store_true',
                        help='Embed the munged string into a mailto: link')
    return parser


def mung(plain):
    return ''.join('&#{};'.format(ord(c)) for c in plain)


if __name__ == '__main__':
    args = command_line_parser().parse_args()
    string_munged = mung(args.string_to_mung)
    if (args.link):
        string_munged = '<a href="{0}{1}">{1}</a>'.format(mung('mailto:'), string_munged)
    print(string_munged)
