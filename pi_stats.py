#!/usr/bin/python3
#-*- coding: utf-8 -*
import psutil
import math


to_gb = 1024*1024*1024


def get_cpu_stats():
    x = lambda a : f"{a}%"
    print(f"Physical Cores:\t{psutil.cpu_count(logical=False)}")
    print(f"CPU Count:\t{psutil.cpu_count()}")
    cpu_percent = psutil.cpu_percent(percpu=True, interval=0.1)
    print(f"Percentages:\t{list(map(x, cpu_percent))}")


def get_memory_stats():
    vmem = psutil.virtual_memory()
    total_mem = vmem.total/to_gb
    used_mem = vmem.used/to_gb

    print(f"Total memory:\t{math.ceil(total_mem)} GB")
    print("Memory used:\t%.2f GB" % used_mem)


def get_disk_stats():
    path = "/home"
    disk_usage = psutil.disk_usage(path=path)
    used = disk_usage.used / to_gb
    total = disk_usage.total / to_gb
    free = disk_usage.free / to_gb
    print(f"Disk Stats in {path}")
    print("Total:\t%.1f GB" % total)
    print("Used:\t%.1f GB" % used)
    print("Percent:\t%.2f" % disk_usage.percent)


def main():
    print("System Stats:")
    print("=============")
    get_cpu_stats()
    print("\n")
    get_memory_stats()
    print("\n")
    get_disk_stats()


if __name__== "__main__":
  main()
