# coding:utf-8
import requests
import json

class sqlmapApi(object):
    apiUrl = "http://127.0.0.1:8775/"
    headers = {"Content-Type": "application/json"}
    options = {}

    def __init__(self, debug=False):
        self.taskid = None
        self.debug = debug

    def __del__(self):
        self.scan_stop()
        self.scan_kill()
        self.scan_delete()

    # 获得 每个任务的url
    def get_param(self, paramid):
        apiparams = {
            0: "task/new",
            1: "scan/%s/start",
            2: "scan/%s/status",
            3: "scan/%s/data",
            4: "scan/%s/stop",
            5: "scan/%s/kill",
            6: "option/%s/set",
            7: "task/%s/delete",

        }
        return self.apiUrl + apiparams[paramid]

    # 设置headers值
    def set_headers(self, headers):
        self.headers = headers


    # 设置options
    def set_options(self, **kwargs):
        self.options = kwargs
        url = self.get_param(6) % self.taskid
        response = requests.post(url, data=json.dumps(self.options), headers=self.headers)
        return self.get_response(response, 'success')

    #
    def get_response(self, response, keyword, stdout=None):
        retcode, retjson = response.status_code, response.json()
        if stdout and self.debug:
            print stdout
        if retcode == 200:
            return retjson[keyword]

    # 创建并且返回taskid
    def get_taskid(self):
        url = self.get_param(0)
        response = requests.get(url)
        return self.get_response(response, 'taskid')

    # 传入url 开始扫描
    def post_scan(self, taskurl):
        post_data = {"url": taskurl}
        url = self.get_param(1) % self.taskid
        response = requests.post(url, data=json.dumps(post_data), headers=self.headers)
        return self.get_response(response, 'success')

    # 通过taskid查询扫描状态
    def get_status(self):
        url = self.get_param(2) % self.taskid
        response = requests.get(url)
        return self.get_response(response, 'returncode')

    # 通过taskid 查询结果
    def get_data(self):
        url = self.get_param(3) % self.taskid
        response = requests.get(url)
        return self.get_response(response, "data")

    # 判断扫描是否完毕
    def has_returncode(self,):
        pass

    # 通过taskid停止扫描
    def scan_stop(self):
        url = self.get_param(4) % self.taskid
        response = requests.get(url)
        return self.get_response(response, 'success', "Stop task({})".format(self.taskid))

    # 通过taskid 杀掉进程
    def scan_kill(self):
        url = self.get_param(5) % self.taskid
        response = requests.get(url)
        return self.get_response(response, 'success', "Kill task({})".format(self.taskid))

    # 通过taskid 杀掉进程
    def scan_delete(self):
        url = self.get_param(7) % self.taskid
        response = requests.get(url)
        return self.get_response(response, 'success', "Delete task({})".format(self.taskid))


# print 'Hello,JetBrains.Loid'
import time
def push_task():
    a = sqlmapApi()
    taskid = a.get_taskid()
    a.taskid = taskid
    a.set_options(level=5)
    print a.options
    if taskid:
        print a.post_scan(taskurl="http://119.23.209.99/sqli-labs/Less-1/index.php?id=1")
    while a.get_status() != 0:
        print "scanning"
        time.sleep(5)

    print a.get_data()

push_task()