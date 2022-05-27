import time
from importlib import import_module
from parsers.build_parsers import build_parser
from os import environ
environ['TF_CPP_MIN_LOG_LEVEL'] = '1'  # only print warnings and errors

parser = build_parser()

args = parser.parse_args()
if args.help:
    parser.print_help()
    exit(1)
groups = args.groups

if 'download' in groups:
    from data.download import download
    start = time.time()
    download.main(args)
    print(f'download time: {time.time()-start}')
if 'split' in groups:
    from data.format.splitters import split
    start = time.time()
    split.main(args)
    print(f'split time: {time.time()-start}')

if 'format' in groups:
    from src.data.format import format
    start = time.time()
    format.main(args)
    print(f'format time: {time.time()-start}')
if 'featurize' in groups:
    from data.featurize import featurize
    start = time.time()
    featurize.main(args)
    print(f'featurization time: {time.time()-start}')
if 'train' in groups:
    from models import train
    start = time.time()
    train.main(args)
    print(f'train time: {time.time()-start}')
if 'test' in groups:
    from models import test
    start = time.time()
    test.main(args)
    print(f'test time: {time.time()-start}')
