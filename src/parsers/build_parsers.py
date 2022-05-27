import argparse
from parsers.download_parser import add_download_args
from parsers.split_parser import add_split_args
from parsers.format_parser import add_format_args
from parsers.featurize_parser import add_featurize_args
from parsers.train_parser import add_train_args
from parsers.test_parser import add_test_args


def build_parser():
    parser = argparse.ArgumentParser(description='Module for running scripts '
                                     'within the repo.', add_help=False, conflict_handler="resolve")
    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument(dest="groups", nargs='+', help='a list of files to test.',
                        type=str.lower, choices=['download','split', 'format', 'featurize', 'filter', 'train', 'test'])
    # returns tuple of (known, unknown), we grab the known and then our groups
    groups = parser.parse_known_args()[0].groups
    if 'download' in groups:
        parser = add_download_args(parser)
    if 'split' in groups:
        parser = add_split_args(parser)
    if 'format' in groups:
        parser = add_format_args(parser)
    if 'featurize' in groups:
        parser = add_featurize_args(parser)
    if 'train' in groups:
        parser = add_train_args(parser)
    if 'test' in groups:
        parser = add_test_args(parser)
    return parser
