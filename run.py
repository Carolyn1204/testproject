import sys, os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest, HTMLTestRunner
from time import sleep
# from testproject.config import global_parameters as gp
# from testproject.src.common import base
# from testproject.util import send_email

from config import global_parameters as gp
from src.common import base
from util import send_email



suite = unittest.defaultTestLoader.discover(start_dir=gp.testcase_path, pattern='*test.py')

if __name__ == "__main__":
    report = gp.report_path + 'my_report_' + base.BaseClass.current_date() + '.html'
    f = open(report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                           title='Test Report',
                                           description='Report of testproject')
    runner.run(suite)
    f.close()

    sleep(5)
    email = send_email.s_email()
    email.send_report()
