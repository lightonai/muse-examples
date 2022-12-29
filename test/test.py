import json
import unittest

from lightonmuse import Tokenize


class TestCreateEndpoint(unittest.TestCase):
    def setUp(self) -> None:
        with open("examples.json") as f:
            self.data_string = f.read()

    def test_valid_json_and_limits(self):
        # will raise JSONDecodeError if not a valid JSON
        examples = json.loads(self.data_string)
        for example in examples:
            print(example['title'])
            tokenizer = Tokenize(example['model'])
            response, cost, rid = tokenizer(example['request']['text'])
            assert not isinstance(example['request'], list), f"Example {example['title']} has batch size > 1"
            assert not isinstance(example['request']['text'], list), f"Example {example['title']} has batch size > 1"
            assert "n_completions" not in example['request']['params'] or \
                   example['request']['params']['n_completions'] == 1, \
                f"Example {example['title']}\n" \
                f"n_completions in params: {'n_completions' in example['request']['params'].keys()}\n" \
                f"n_completions > 1: {example['request']['params']['n_completions']>1}\n"


if __name__ == '__main__':
    unittest.main()
