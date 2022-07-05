from panlib.dataprocessor import DataProcessor
import logging
from pathlib import Path
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s:pan-data-processor:%(message)s',
)
logger = logging.getLogger(__name__)


def test_load_input():
    input_file = Path("test_data")
    data_processor = DataProcessor(input_file=input_file, logger=logger)
    assert data_processor.load_input() is True


def test_transform_data():
    input_file = Path("test_data")
    data_processor = DataProcessor(input_file=input_file, logger=logger)
    data_processor.load_input()
    assert data_processor.transform_data() is True


def test_transform_incorrect_file():
    input_file = Path("not_present")
    data_processor = DataProcessor(input_file=input_file, logger=logger)
    data_processor.load_input()
    assert data_processor.transform_data() is False


def test_transform_incorrect_data_syntax():
    input_file = Path("test_incorrect_data")
    data_processor = DataProcessor(input_file=input_file, logger=logger)
    data_processor.load_input()
    assert data_processor.transform_data() is False


def test_transform_incorrect_data_format():
    input_file = Path("test_incorrect_data1")
    data_processor = DataProcessor(input_file=input_file, logger=logger)
    data_processor.load_input()
    assert data_processor.transform_data() is False

def test_save_data_failure():
    input_file = Path("test_data")
    data_processor = DataProcessor(input_file=input_file, logger=logger)
    data_processor.load_input()
    data_processor.transform_data()
    assert data_processor.save_data() is None

def test_save_data_success():
    input_file = Path("test_data")
    data_processor = DataProcessor(input_file=input_file, output="test_data_transformed.json", logger=logger)
    data_processor.load_input()
    data_processor.transform_data()
    assert data_processor.save_data() is None