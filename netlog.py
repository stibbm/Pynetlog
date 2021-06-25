import time
import psutil
from datetime import date
from datetime import datetime


def main():
    bytes_recv = 0
    bytes_sent = 0

    while True:

        new_bytes_recv = psutil.net_io_counters().bytes_recv
        new_bytes_sent = psutil.net_io_counters().bytes_sent

        if bytes_recv:
            print_download_stat(new_bytes_recv - bytes_recv)

        if bytes_sent:
            print_upload_stat(new_bytes_sent - bytes_sent)


        bytes_recv = new_bytes_recv
        bytes_sent = new_bytes_sent

        time.sleep(1)

def convert_to_mbit(value):
    return value/1024./1024.*8

def print_upload_stat(value):
    today = datetime.now()
    print (today, " upload rate %0.3f mb" % convert_to_mbit(value))

def print_download_stat(value):
    today = datetime.now()
    print (today, " download rate %0.3f mb" % convert_to_mbit(value))


def main1():
    while(True):
        try:
            today = datetime.now()
            print(today, " starting main")
            main()
        except Exception as e:
            print(e)

main1()
