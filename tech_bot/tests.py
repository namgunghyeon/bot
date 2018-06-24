from unittest import TestLoader, TextTestRunner, TestSuite

from src.crawling.__test__.outsider_test import outsider_test_case

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite(loader.loadTestsFromTestCase(outsider_test_case))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)