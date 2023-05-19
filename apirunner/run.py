import itertools
import json
import unittest

from HTMLReport import TestRunner

from swagger_parser import parse_swagger
import requests

BASE_URL = 'http://postman-echo.com'


def generate_test_suite(swagger_file: str) -> "TestSuite":
    """
    根据swagger文件生成测试套件
    :param swagger_file: swagger文件(JSON格式)
    :return: 测试套件
    """
    interfaces, interface_params, interface_info = parse_swagger(swagger_file)
    testcases = []
    test_suite = unittest.TestSuite()

    print(interface_info)
    for interface in interfaces:
        params_keys = list(interface_params[interface].keys())
        params_values = list(interface_params[interface].values())
        combinations = list(itertools.product(*params_values))

        for combo in combinations:
            param_dict = dict(zip(params_keys, combo))
            testcase = {
                "name": f"{interface.replace('/', '_')}_{'_'.join(params_keys)}",
                "interface": interface,
                "method": interface_info[interface]['method'],
                "params": param_dict,
                "expect": 200
            }
            testcases.append(testcase)

            def test_method(self):
                url = "http://" + interface_info[interface]['url']
                if interface_info[interface]['method'] == 'GET':
                    response = requests.get(url, params=param_dict)
                elif interface_info[interface]['method'] == 'POST':
                    response = requests.post(url, json=param_dict)
                else:
                    response = requests.put(url, json=param_dict)

                self.assertEqual(response.status_code, 200)

            setattr(test_suite, f'test_{testcase["name"]}', test_method)

    with open('../tests/testcases.json', 'w') as f:
        json.dump(testcases, f, indent=4, default=str)

    return test_suite


class TestSuite(unittest.TestCase):
    def test_testcases(self):
        with open('../tests/testcases.json') as f:
            testcases = json.load(f)

        for testcase in testcases:
            url = BASE_URL + testcase['interface']
            if testcase['method'] == 'GET':
                response = requests.get(url, params=testcase['params'])
                print(response.text)
            elif testcase['method'] == 'POST':
                response = requests.post(url, json=testcase['params'])

            self.assertEqual(response.status_code, testcase['expect'])


if __name__ == '__main__':
    generate_test_suite('../tests/swagger.json')
    runner = unittest.TextTestRunner()
    # runner = TestRunner(
    #     report_file_name="index",
    #     output_path="report",
    #     title="一个简单的测试报告",
    #     description="随意描述",
    #     thread_count=1,
    #     thread_start_wait=0.1,
    #     tries=3,
    #     delay=0,
    #     back_off=1,
    #     retry=False,
    #     sequential_execution=True,
    #     lang="cn"
    # )
    runner.run(unittest.makeSuite(TestSuite))
