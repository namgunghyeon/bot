from unittest import TestLoader, TextTestRunner, TestSuite

from src.crawling.__test__.outsider_test import outsider_test_case
from src.crawling.__test__.baemin_test import baemin_test_case
from src.crawling.__test__.kakao_test import kakao_test_case
from src.crawling.__test__.naver_test import naver_test_case

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(outsider_test_case),
        loader.loadTestsFromTestCase(baemin_test_case),
        loader.loadTestsFromTestCase(kakao_test_case),
        loader.loadTestsFromTestCase(naver_test_case)
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)