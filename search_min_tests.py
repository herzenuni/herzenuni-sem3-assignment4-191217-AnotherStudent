from search_min import *
# python -m pytest search_min_tests.py -v
import pytest

@pytest.mark.parametrize("array,result", [
  ([-10, -0, 10, 99, -1], -9900),
  ([10000, 0, 3, 1, 2], 0),
  ([1, 2, 3, 4, 5], 6),
  ([1929, 39, 946, 23, 4], 3588),
  ([32, 7, 0, 3], 0),
  ([0, 0, 0], 0),
  ([-10, -2, -10, -1, -4], -400)])
def test_simple(array, result):
	assert search_min(array) == result

def test_exceptions_too_few():
	try:
		search_min([1,2])
	except ValueError:
		assert True
	else:
		assert False

def test_exceptions_no_list():
	try:
		search_min('a')
	except ValueError:
		assert True
	else:
		assert False

def test_exceptions_no_number_in_list():
	try:
		search_min([1, 2, 3, 4, 5, True])
	except ValueError:
		assert True
	else:
		assert False