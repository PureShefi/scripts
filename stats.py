import argparse
import psutil
import datetime
from subprocess import check_output

def get_pid(name):
    return int(check_output(["pidof", "-s", name]))

def main():
    parser = argparse.ArgumentParser(
    description="print the cpu and memory usage of process and the disk usage of specified path")
    parser.add_argument("process", help="the name of the process", type=str)
    parser.add_argument(
        "-p", "--path", help="the path to get the disk usage", type=str)
    args = parser.parse_args()


    try:
        process = psutil.Process(get_pid(args.process))
    except psutil.NoSuchProcess as noprocess:
        print "there isn't a process with PID {0:d}".format(noprocess.pid)
        return

    cpu = process.cpu_percent()
    mem = process.memory_percent()

    if args.path is not None:
        disk = psutil.disk_usage(args.path)
        output = '{0:.2f},{1:.2f},{2:.2f}'.format(cpu, mem, disk.percent)
    else:
        output = '{0:.2f},{1:.2f}'.format(cpu, mem)
    print output

if __name__ == "__main__":
    main()