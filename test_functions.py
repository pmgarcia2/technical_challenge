import unittest
from stackexchange_analysis import connect_to_api, count_answers, get_least_views_item, get_oldest_and_newest_item, get_owner_highestrep_item

class StackExchangeAnalysis(unittest.TestCase):
    def test_connect_to_api(self):
        # Test case with successful connection
        api_url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
        response = connect_to_api(api_url)
        self.assertEqual(response.status_code, 200)

        # Test case with connection error
        api_url = "https://api.stackexchange.com/2.2/test_case"
        response = connect_to_api(api_url)
        self.assertIsNone(response)

    def test_count_answers(self):
        # Test case with answers
        data = {"items": [{"is_answered": True}, {"is_answered": True}, {"is_answered": False}]}
        expected_answered, expected_unanswered = 2, 1
        actual_answered, actual_unanswered = count_answers(data)
        self.assertEqual(expected_answered, actual_answered)
        self.assertEqual(expected_unanswered, actual_unanswered)

        # Test case without answers
        data = {"items": []}
        expected_answered, expected_unanswered = 0, 0
        actual_answered, actual_unanswered = count_answers(data)
        self.assertEqual(expected_answered, actual_answered)
        self.assertEqual(expected_unanswered, actual_unanswered)

    def test_get_least_views_item(self):
        # Test case with items
        data = {"items": [{"view_count": 10}, {"view_count": 5}, {"view_count": 20}]}
        expected_item = {"view_count": 5}
        actual_item = get_least_views_item(data)
        self.assertEqual(expected_item, actual_item)

        # Test case without items
        data = {"items": []}
        expected_item = None
        actual_item = get_least_views_item(data)
        self.assertEqual(expected_item, actual_item)

    def test_get_oldest_and_newest_item(self):
        # Test case with items
        data = {"items": [{"creation_date": 1708617473}, {"creation_date": 1707177048}, {"creation_date": 1387366120}]}
        expected_oldest, expected_newest = {"creation_date": 1387366120}, {"creation_date": 1708617473}
        actual_oldest, actual_newest = get_oldest_and_newest_item(data)
        self.assertEqual(expected_oldest, actual_oldest)
        self.assertEqual(expected_newest, actual_newest)

        # Test case without items
        data = {"items": []}
        expected_oldest, expected_newest = None, None
        actual_oldest, actual_newest = get_oldest_and_newest_item(data)
        self.assertEqual(expected_oldest, actual_oldest)
        self.assertEqual(expected_newest, actual_newest)

    def test_get_owner_highestrep_item(self):
        # Test case with items
        data = {"items": [{"owner": {"reputation": 10}}, {"owner": {"reputation": 20}}, {"owner": {"reputation": 30}}]}
        expected_item = {"owner": {"reputation": 30}}
        actual_item = get_owner_highestrep_item(data)
        self.assertEqual(expected_item, actual_item)

        # Test case without items
        data = {"items": []}
        expected_item = None
        actual_item = get_owner_highestrep_item(data)
        self.assertEqual(expected_item, actual_item)

if __name__ == "__main__":
    unittest.main()