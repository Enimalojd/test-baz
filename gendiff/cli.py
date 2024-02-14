import argparse


def get_reference():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--format',
        default='json',
        choices=['json'],
        help='Output format'
    )
    return parser.parse_args()
