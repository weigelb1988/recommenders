import argparse


def add_format_args(parser):
    group = parser.add_argument_group('format')
    try:
        group.add_argument('--example', '-e', type=str, default='/example/example/',
                           help='path to extract directory containing acc and gyro.csv files')
    except argparse.ArgumentError:
        pass

    group.add_argument('--output_file', '-o', type=str, default='examples..pkl',
                       help='path to extract directory containing acc and gyro.csv files')

    group.add_argument('--max_threads', type=int, default=5, help='The max '
                       'number of running threads, including the main thread. Default is 5.')

    return parser
