import json
import re


def parse_swagger(swagger_file):
    """解析swagger文件,返回接口列表和参数列表"""
    with open(swagger_file, 'r') as f:
        swagger_doc = json.load(f)
    server = swagger_doc['host']
    base_path = swagger_doc['basePath']
    paths = swagger_doc['paths']
    interfaces = list(paths.keys())
    interface_info = {}
    interface_params = {}

    for path in paths:
        if paths[path]['get']:
            interface_info[path] = {
                'url': get_url(server, base_path, path),
                'method': 'GET'
            }
        # if paths[path]['post']:
        #     interface_info[path] = {
        #         'url': get_url(server, base_path, path),
        #         'method': 'POST'
        #     }

    for interface in interfaces:
        params = paths[interface]['get']['parameters']
        param_values = {}
        for param in params:
            name = param['name']
            if param['type'] == 'array':
                items = param['items']
                values = items['enum']
            elif 'enum' in param:
                values = param['enum']
            else:
                continue
            param_values[name] = values
        interface_params[interface] = param_values
        interface_info[interface]['params'] = interface_params[interface]
        # interface_params[interface] = params

    return interfaces, interface_params, interface_info


def get_url(server, base_path, path):
    """获取接口的url"""
    url = server + base_path + path
    url = re.sub(r"<.*>/", "", url)
    return url


if __name__ == '__main__':
    interfaces, interface_params,interface_info = parse_swagger('../tests/swagger.json')
    url = get_url('http://postman-echo.com', '', interfaces[0])
    print(interfaces)
    print(interface_params)
    print(interface_info)
    print(url)