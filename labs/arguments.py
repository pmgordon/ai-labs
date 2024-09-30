"""Utility for parsing command line arguments"""
import argparse


def parse_args():
    """function for parsing command line args"""
    parser = argparse.ArgumentParser(prog='sample_program',
                                     description='A template for Python')
    # Add this for a required option
    parser.add_argument('--required-option',
                        metavar='-R',
                        type=str,
                        help='A Required Option',
                        required=True)

    parser.add_argument('--non-required-option',
                        metavar='-N',
                        help='A Non Required Option')

    parser.add_argument('--non-required-boolean',
                        action="store_true",
                        default=False,
                        help='A Non Required Boolean with default false')


    return parser.parse_args()
