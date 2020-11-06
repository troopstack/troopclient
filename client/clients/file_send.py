# -*- coding: utf-8 -*-
"""
@  time    : 2020/03/09
@  author  : XieYZ
"""
from ..api import APIClient


class FileSendClient(APIClient):

    def file_send(self, data, file_name, file, dest, cover=False):
        """文件推送"""
        url = f"{self.file_send_url}"
        data.update({
            "file_name": file_name,
            "file": file,
            "dest": dest,
            "cover": cover
        })
        common_params = self.common_params()
        common_params.update(data)
        res = self.post(url=url, data=common_params)
        print(res)
        return res
