#!/usr/bin/env python3

from argparse import ArgumentParser
from panlib.dataprocessor import DataProcessor
from pathlib import Path
import logging
import sys


if __name__ == '__main__':
    logger = logging.getLogger(__name__)

    parser = ArgumentParser()
    parser.add_argument("-i", "--input_json", help="Input data json file", required=True, default="data.json")
    parser.add_argument("-o", "--output", default="data-transformed.json", help="Output file to write the transformed "
                                                                                "data")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()

    log_level = logging.DEBUG if args.debug else logging.INFO

    logging.basicConfig(
        stream=sys.stdout,
        level=log_level,
        format='[%(asctime)s] %(levelname)s:pan-data-processor: %(message)s',
    )
    logger = logging.getLogger(__name__)

    input_file = Path(args.input_json)

    if not input_file.exists():
        logger.error(f"Error: Input file not found!")
        sys.exit(1)

    data_processor = DataProcessor(input_file=input_file, output=args.output, logger=logger)
    if data_processor.load_input():
        transformed_data = data_processor.transform_data()
        data_processor.save_data(data=transformed_data)
    else:
        logger.error(f"Failed to transform data!")




