import requests
import os
import logging
import argparse

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)


def crawl(output_folder):
    LOG.info('Dummy crawler function. Dumping output to "{}"'.format(output_folder))
    pass


if __name__ == "__main__":
    # Parse arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--output-folder",
                            help="Folder where to add data to.",
                            required=True, type=str)

    args = arg_parser.parse_args()

    assert os.path.exists(args.output_folder), '"{}" path does not exist'.format(args.output_folder)

    # Do the actual crawling
    crawl(args.output_folder)
