import os
import glob
import sys

from ruamel.yaml import YAML


def modifyYaml():
    # 确定应用程序是一个脚本文件还是冻结的exe文件
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(sys.executable)
    elif __file__:
        path = os.path.dirname(__file__)

    directory = path + '/'
    print('工作目录:', directory)
    #读取配置信息
    with open(directory + 'AddHosts.yaml', 'r') as file:
        add_hosts_data = YAML().load(file)
        add_hosts = add_hosts_data.get('hosts')
        exclude_files = add_hosts_data.get('exclude_files')
        clash_catalog = add_hosts_data.get('clash_catalog')

    print('新增hosts:', add_hosts)
    print('排除的文件:', exclude_files)
    yaml_files = glob.glob(clash_catalog + '*.yaml')  # 获取所有yaml文件

    yaml = YAML()
    for file in yaml_files:
        file_name = os.path.basename(file)
        if file_name not in exclude_files:
            with open(file, 'r') as file_temp:
                data = yaml.load(file_temp)

            hosts = data.get('hosts')
            if hosts is not None:
                add_hosts.update(hosts)  # 如果之前存在hosts，就更新

            data['hosts'] = add_hosts  # 设置hosts

            with open(file, 'w', encoding='utf-8') as file_temp:
                yaml.dump(data, file_temp)
                print(file_name, '修改成功')


if __name__ == '__main__':
    modifyYaml()
    # 打包
    # pyinstaller --onefile main.py
    # pyinstaller -D main.py
