import pytest
import pytest_html
from testcases import tests


if __name__ == '__main__':
    pytest.main(['-vs',  'testcases/tests', '--html=./logs/html_report.html'])

