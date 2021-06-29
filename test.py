import unittest

from main import first_reversed_flow, reversed_dict, second_reversed_dict, compose_dict

INPUT_VALUES = {
    'hired': {
        'be': {
            'to': {
                'deserve': 'I'
            }
        }
    }
}
OUTPUT_VALUES = {
    'I': {
        'deserve': {
            'to': {
                'be': 'hired'
            }
        }
    }
}
OUTPUT_VALUES_LIST = ['hired', 'be', 'to', 'deserve', 'I']
INPUT_VALUE = {'hired': 'be'}
OUTPUT_VALUE = {'be': 'hired'}
OUTPUT_VALUE_LIST = ['hired', 'be']


class AReversedFlowTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("\nReversedFlowTestCase")

    def test_single_dict(self):
        print("test_single_dict")
        output = first_reversed_flow(INPUT_VALUE)
        self.assertEqual(output, OUTPUT_VALUE)

    def test_multi_dict(self):
        print("test_multi_dict")
        output = first_reversed_flow(INPUT_VALUES)
        self.assertEqual(output, OUTPUT_VALUES)

    def test_empty_input(self):
        print("test_empty_input")
        output = first_reversed_flow({})
        self.assertEqual(output, [])

    def test_error_type_input(self):
        print("test_error_type_input")
        output = first_reversed_flow("")
        self.assertEqual(output, [])


class BFirstReversedDictTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("\nFirstReversedDictTestCase")

    def test_single_dict(self):
        print("test_single_dict")
        output = reversed_dict(INPUT_VALUE)
        self.assertEqual(output, OUTPUT_VALUE_LIST)

    def test_multi_dict(self):
        print("test_multi_dict")
        output = reversed_dict(INPUT_VALUES)
        self.assertEqual(output, OUTPUT_VALUES_LIST)

    def test_empty_input(self):
        print("test_empty_input")
        output = reversed_dict({})
        self.assertEqual(output, [])

    def test_error_type_input(self):
        print("test_error_type_input")
        output = reversed_dict("")
        self.assertEqual(output, [])


class CSecondReversedDictTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("\nSecondReversedDictTestCase")

    def test_single_dict(self):
        print("test_single_dict")
        output = second_reversed_dict(INPUT_VALUE)
        self.assertEqual(output, OUTPUT_VALUE)

    def test_multi_dict(self):
        print("test_multi_dict")
        output = second_reversed_dict(INPUT_VALUES)
        self.assertEqual(output, OUTPUT_VALUES)

    def test_empty_input(self):
        print("test_empty_input")
        output = second_reversed_dict({})
        self.assertEqual(output, [])

    def test_error_type_input(self):
        print("test_error_type_input")
        output = second_reversed_dict("")
        self.assertEqual(output, [])


class DComposeDictTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("\nComposeDictTestCase")

    def test_single_dict(self):
        print("test_single_dict")
        output = compose_dict(OUTPUT_VALUE_LIST)
        self.assertEqual(output, INPUT_VALUE)

    def test_multi_dict(self):
        print("test_multi_dict")
        output = compose_dict(OUTPUT_VALUES_LIST)
        self.assertEqual(output, INPUT_VALUES)

    def test_empty_input(self):
        print("test_empty_input")
        output = compose_dict({})
        self.assertEqual(output, "")

    def test_error_type_input(self):
        print("test_error_type_input")
        output = compose_dict("")
        self.assertEqual(output, "")

