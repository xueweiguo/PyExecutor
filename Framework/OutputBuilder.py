class OutputBuilder:
    # 生成功能模块数据
    # t:模块类型，n:模块名称
    def build_fun(self, t, n):
        pass

    # 生成功能模块输入数据
    # n：端口名称，data_tag：数据id
    def build_input(self, n, data_tag):
        pass

    # 生成功能模块参数数据
    # n：端口名称，value:参数值
    def build_param(self, port, value):
        pass

    # 生成功能模块输出数据
    # n：端口名称，data_tag：数据id
    def build_output(self, port, data_tag):
        pass

    # 生成功能模块其他设定信息
    # n:信息名称
    # contents:信息内容
    def build_config(self, n, contents):
        pass
