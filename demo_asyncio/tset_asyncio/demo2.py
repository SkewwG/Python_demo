import asyncio
import requests
from bs4 import BeautifulSoup
import chardet
from threading import current_thread
import socket
from IPy import IP
import time
IP_NUM = 10
IP_NUM_1 = IP_NUM - 1
# "20": {"name": "ftp_data", "detail": "数据端口", "exp": "爆破、嗅探、溢出、后门"},
ports_protocols = {
        "20": {"name": "ftp_data", "detail": "数据端口", "exp": "爆破、嗅探、溢出、后门"},
        "21": {"name": "ftp_control", "detail": "控制端口", "exp": "爆破、嗅探、溢出、后门"},
        '23': {"name": 'telnet', "detail": '远程连接', 'exp': '爆破、嗅探'},
        '25': {'name': 'smtp', 'detail': '邮件服务', 'exp': '邮件伪造'},
        '53': {'name': 'DNS', 'detail': '域名系统', 'exp': 'DNS区域传输、DNS劫持、DNS缓存投毒、DNS欺骗、深度利用：利用DNS隧道技术刺透防火墙'},
        '67': {'name': 'dhcp', 'detail': '', 'exp': '劫持、欺骗'},
        '68': {'name': 'dhcp', 'detail': '', 'exp': '劫持、欺骗'},
        '110': {'name': 'pop3', 'detail': '', 'exp': '爆破'},
        '139': {'name': 'samba', 'detail': '', 'exp': '爆破、未授权访问、远程代码执行'},
        '143': {'name': 'imap', 'detail': '', 'exp': '爆破'},
        '161': {'name': 'snmp', 'detail': '', 'exp': '爆破'},
        '389': {'name': 'ldap', 'detail': '', 'exp': '注入攻击、未授权访问'},
        '512': {'name': 'linux r', 'detail': '', 'exp': '直接使用rlogin'},
        '513': {'name': 'linux r', 'detail': '', 'exp': '直接使用rlogin'},
        '514': {'name': 'linux r', 'detail': '', 'exp': '直接使用rlogin'},
        '873': {'name': 'rsync', 'detail': '', 'exp': '未授权访问'},
        '888': {'name': 'BTLINUX', 'detail': '', 'exp': '宝塔Linux主机管理后台/默认帐户：admin|默认密码：admin'},
        '999': {'name': 'PMA', 'detail': '', 'exp': '护卫神佩带的phpmyadmin管理后台，默认帐户：root|默认密码：huweishen.com'},
        '1080': {'name': 'socket', 'detail': '', 'exp': '爆破：进行内网渗透'},
        '1352': {'name': 'lotus', 'detail': '', 'exp': '爆破：弱口令、信息泄露：源代码'},
        '1433': {'name': 'mssql', 'detail': '', 'exp': '爆破：使用系统用户登录、注入攻击'},
        '1521': {'name': 'oracle', 'detail': 'iSqlPlus Port:5560,7778', 'exp': '爆破：TNS、注入攻击'},
        '2049': {'name': 'nfs', 'detail': '', 'exp': '配置不当'},
        '2181': {'name': 'zookeeper', 'detail': '', 'exp': '未授权访问'},
        '3306': {'name': 'mysql', 'detail': '', 'exp': '爆破、拒绝服务、注入'},
        '3389': {'name': 'rdp', 'detail': '', 'exp': '爆破、Shift后门'},
        '4848': {'name': 'glassfish', 'detail': 'web中间件，admin/adminadmin', 'exp': '爆破：控制台弱口令、认证绕过'},
        '5000': {'name': 'sybase/DB2', 'detail': '', 'exp': '爆破、注入'},
        '5432': {'name': 'postgresql', 'detail': '', 'exp': '缓冲区溢出、注入攻击、爆破：弱口令'},
        '5632': {'name': 'pcanywhere', 'detail': '', 'exp': '拒绝服务、代码执行'},
        '5900': {'name': 'vnc', 'detail': '', 'exp': '爆破：弱口令、认证绕过'},
        '5901': {'name': 'vnc', 'detail': '', 'exp': '爆破：弱口令、认证绕过'},
        '5902': {'name': 'vnc', 'detail': '', 'exp': '爆破：弱口令、认证绕过'},
        '6379': {'name': 'redis', 'detail': '', 'exp': '未授权访问、爆破：弱口令'},
        '7001': {'name': 'weblogic', 'detail': '', 'exp': 'JAVA反序列化、控制台弱口令、控制台部署webshell'},
        '7002': {'name': 'weblogic', 'detail': '', 'exp': 'JAVA反序列化、控制台弱口令、控制台部署webshell'},
        '80': {'name': 'web', 'detail': '', 'exp': '常见Web攻击、控制台爆破、对应服务器版本漏洞'},
        '443': {'name': 'web', 'detail': '', 'exp': '常见Web攻击、控制台爆破、对应服务器版本漏洞'},
        '8080': {'name': 'web|Tomcat|..', 'detail': '', 'exp': '常见Web攻击、控制台爆破、对应服务器版本漏洞、Tomcat漏洞'},
        '8069': {'name': 'zabbix', 'detail': '', 'exp': '远程命令执行'},
        '9090': {'name': 'websphere', 'detail': '', 'exp': '文件泄露、爆破：控制台弱口令、Java反序列'},
        '9200': {'name': 'elasticsearch', 'detail': '', 'exp': '未授权访问、远程代码执行'},
        '9300': {'name': 'elasticsearch', 'detail': '', 'exp': '未授权访问、远程代码执行'},
        '11211': {'name': 'memcacache', 'detail': '', 'exp': '未授权访问'},
        '27017': {'name': 'mongodb', 'detail': '', 'exp': '爆破、未授权访问'},
        '27018': {'name': 'mongodb', 'detail': '', 'exp': '爆破、未授权访问'},
        '50070': {'name': 'Hadoop', 'detail': 'NameNode', 'exp': '爆破、未授权访问'},
        '50075': {'name': 'Hadoop', 'detail': 'DataNode', 'exp': '爆破、未授权访问'},
        '14000': {'name': 'Hadoop', 'detail': 'httpfs', 'exp': '爆破、未授权访问'},
        '8480': {'name': 'Hadoop', 'detail': 'journalnode', 'exp': '爆破、未授权访问'},
        '8088': {'name': 'web', 'detail': '后台', 'exp': '爆破、未授权访问'},
        '50030': {'name': 'Hadoop', 'detail': 'JobTracker', 'exp': '爆破、未授权访问'},
        '50060': {'name': 'Hadoop', 'detail': 'TaskTracker', 'exp': '爆破、未授权访问'},
        '60010': {'name': 'Hadoop', 'detail': 'master', 'exp': '爆破、未授权访问'},
        '60030': {'name': 'Hadoop', 'detail': 'regionserver', 'exp': '爆破、未授权访问'},
        '10000': {'name': 'Virtualmin/Webmin', 'detail': 'hive-server2', 'exp': '服务器虚拟主机管理系统'},
        '10003': {'name': 'Hadoop', 'detail': 'spark-jdbcserver', 'exp': '爆破、未授权访问'},
        '5984': {'name': 'couchdb', 'detail': 'http://xxx:5984/_utils/', 'exp': '未授权访问'},
        '445': {'name': 'SMB', 'detail': '', 'exp': '弱口令爆破，检测是否有ms_08067等溢出'},
        '1025': {'name': '111', 'detail': '', 'exp': 'NFS'},
        '2082': {'name': '', 'detail': '', 'exp': 'cpanel主机管理系统登陆 （国外用较多）'},
        '2083': {'name': '', 'detail': '', 'exp': 'cpanel主机管理系统登陆 （国外用较多）'},
        '2222': {'name': '', 'detail': '', 'exp': 'DA虚拟主机管理系统登陆 （国外用较多）'},
        '2601': {'name': '', 'detail': '默认密码zebra', 'exp': 'zebra路由'},
        '2604': {'name': '', 'detail': '默认密码zebra', 'exp': 'zebra路由'},
        '3128': {'name': '', 'detail': 'squid', 'exp': '代理默认端口,如果没设置口令很可能就直接漫游内网了'},
        '3311': {'name': '', 'detail': '', 'exp': 'kangle主机管理系统登陆'},
        '3312': {'name': '', 'detail': '', 'exp': 'kangle主机管理系统登陆'},
        '4440': {'name': '', 'detail': 'rundeck 弱口令:admin/admin', 'exp': '参考WooYun: 借用新浪某服务成功漫游新浪内网'},
        '6082': {'name': '', 'detail': 'varnish',
                 'exp': '参考WooYun: Varnish HTTP accelerator CLI 未授权访问易导致网站被直接篡改或者作为代理进入内网'},
        '7778': {'name': '', 'detail': 'Kloxo', 'exp': '主机控制面板登录'},
        '8083': {'name': '', 'detail': 'Vestacp', 'exp': '主机管理系统 （国外用较多）'},
        '8649': {'name': '', 'detail': 'ganglia', 'exp': ''},
        '8888': {'name': '', 'detail': 'amh/LuManager', 'exp': '主机管理系统默认端口'},
        '9000': {'name': '', 'detail': 'fcgi', 'exp': 'fcgi php执行'},
        '50000': {'name': '', 'detail': 'SAP', 'exp': '命令执行'}
}
socket.setdefaulttimeout(5)



def scanPorts(ip):
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.setblocking(False)            # 设置为非阻塞
        addr = (str(ip), int(port))
        # print(addr)
        try:
            s.connect(addr)
            print('[+] {} open'.format(addr))
        except BlockingIOError:
            pass
            #print('[-] {} close. BlockingIOError'.format(addr))
        except Exception as e:
            pass
            #print('[-] {} close. error:{}'.format(addr, e))




if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    ip_list = []
    ports = ports_protocols.keys()
    with open(r'ips.txt', 'rt') as f:
        for CIDR_IPS in f:
            CIDR_IPS = CIDR_IPS.strip()
            print('[{}]'.format(CIDR_IPS))
            ips = IP(CIDR_IPS)
            for i, ip in enumerate(ips):
                if i % IP_NUM != IP_NUM_1:
                    ip_list.append(ip)
                else:
                    ip_list.append(ip)
                    list(map(scanPorts, ip_list))
                    del ip_list[:]
    print(time.time() - start_time)
