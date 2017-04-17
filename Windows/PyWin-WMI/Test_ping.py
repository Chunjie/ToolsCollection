import os
import time
import wmi
import _winreg

PingBinaryPath = "ping.exe"
ProcessName = "ping.exe"

jobCompleted = False

c = wmi.WMI()

def readHosts(hostfile = "URLs"):
    hosts = []

    fpath = os.path.join(os.path.curdir, hostfile)
    try:
        fd = open(fpath, 'r')
        lines = fd.readlines()
        fd.close()

        for line in lines:
            hosts.append(line.strip())
    except Exception, e:
        pass   # simply ignore the exception
    return hosts

def spawnPingTest(ping, host):
    process = c.Win32_Process
    cmdline = "%s -n 10 %s" % (ping, host)
    process_id, result = process.Create(CommandLine = cmdline)
    #watcher = c.watch_for(notification_type = "operation", wmi_class = "Win32_Process", delay_secs = 3, ProcessId = process_id)
    #watcher()
    print "Spawn ping access remote host: %s" % host

def main():
    count = 0
    hosts = readHosts()
    while True:
        for host in hosts:
            count += 1
            spawnPingTest(PingBinaryPath, host)
            if count % 10 == 0:
                time.sleep(10)
        time.sleep(10)
    jobCompleted = True

if __name__ == "__main__":
    main()
