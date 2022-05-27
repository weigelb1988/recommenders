import argparse
from random import choices


def add_split_args(parser):
    group = parser.add_argument_group('split')
    try:
         group.add_argument("--split_method", default="random", choices=['random', 'chrono', 'strat', "spark"], help="Way to split the data")
    
    except argparse.ArgumentError:
        pass
    try:
        group.add_argument('--data_path', '-o', type=str, default='data/download/ml-100k.data',
                       help='path to download directory')
    except argparse.ArgumentError:
        pass
    try:
        group.add_argument('--train_path', type=str, default='data/download/train_ml-100k.data', help='path to store the train data')
    except argparse.ArgumentError:
        pass
    
    try:
        group.add_argument('--test_path', type=str, default='data/download/test_ml-100k.data', help='Path to store the test data.')
    except argparse.ArgumentError:
        pass
    try:
        group.add_argument('--val_path', type=str, default='data/download/val_ml-100k.data', help='Path to store the test data.')
    except argparse.ArgumentError:
        pass 
    try:
        group.add_argument('--ratio', type=float, nargs="+", default=[0.6, 0.3, 0.1], help='Ratios, in [train test val] format')
    except argparse.ArgumentError:
        pass 

    try:
         group.add_argument("--filter_by", default="user", choices=['user', 'item'], help="Column to split by")
    
    except argparse.ArgumentError:
        pass

    try:
         group.add_argument("--min_samples", default=10, type=int, help="minimum number of samples for a given user/item")
    
    except argparse.ArgumentError:
        pass
    return parser
