import argparse


def add_download_args(parser):
    group = parser.add_argument_group('download')
    try:
         group.add_argument("--data_url", type=str, default="https://files.grouplens.org/datasets/movielens/ml-100k/u.data", help="URL to get the data from")
    
    except argparse.ArgumentError:
        pass
    try:
        group.add_argument('--data_path', '-o', type=str, default='data/downloads/ml-100k.data',
                       help='path to download directory')
    except argparse.ArgumentError:
        pass
    try:
        group.add_argument('--max_threads', type=int, default=5, help='The max '
                       'number of running threads, including the main thread. Default is 5.')
    except argparse.ArgumentError:
        pass
   
    return parser
