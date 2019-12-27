import yaml, os


class GetData:

    def get_yml_data(self, name):
        """
        返回yaml文件数据
        :param name: 需要读取文件名字
        :return:
        """
        # 打开文件
        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            # 加载文件
            return yaml.safe_load(f)
