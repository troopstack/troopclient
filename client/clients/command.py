# -*- coding: utf-8 -*-
"""
@  time    : 2020/03/09
@  author  : XieYZ
"""
from ..api import APIClient


class CommandClient(APIClient):

    def command(self, data):
        """执行命令"""
        url = f"{self.command_task_url}"
        common_params = self.common_params()
        common_params.update(data)
        print(common_params)
        res = self.post(url=url, data=common_params)
        return res
