import unittest
from shikiho_parser import parse_shikiho_html

class TestShikihoParser(unittest.TestCase):
    def test_parse_shikiho_html(self):
        html_content = '''
        <div class="growth">12%</div>
        <div class="profit_margin">6%</div>
        '''
        expected_data = {
            'growth': 12,
            'profit_margin': 6.0
        }
        self.assertEqual(parse_shikiho_html(html_content), expected_data)

if __name__ == '__main__':
    unittest.main()