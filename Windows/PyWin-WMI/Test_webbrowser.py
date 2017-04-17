import os
import time
import wmi
import _winreg

BrowserBinaryPath = "C:\Program Files (x86)\Internet Explorer\iexplore.exe"
ProcessName = "iexplore.exe"

jobCompleted = False

c = wmi.WMI()

def readUrls(urlfile = "URLs"):
    urls = []

    fpath = os.path.join(os.path.curdir, urlfile)
    try:
        fd = open(fpath, 'r')
        lines = fd.readlines()
        fd.close()

        for line in lines:
            urls.append(line.strip())
    except Exception, e:
        pass   # simply ignore the exception
    return urls

def spawnWebBrowser(browser, url):
    if not os.path.exists(browser):
        return

    process = c.Win32_Process
    cmdline = "%s %s" % (browser, url)
    process_id, result = process.Create(CommandLine = cmdline)
    #watcher = c.watch_for(notification_type = "operation", wmi_class = "Win32_Process", delay_secs = 3, ProcessId = process_id)
    #watcher()
    print "Spawn web browser accessing web url: %s" % url

def stopWebBrowser(name = ProcessName):
    pids = []
    for p in c.Win32_Process():
        if p.Name.strip().lower() == name.strip().lower():
            pids.append(p.ProcessId)

    try:
        for pid in pids:
            for p in c.Win32_Process(ProcessId = pid):
                p.Terminate(0)
    except Exception, e:
        pass  # simply ignore the exception

def main():
    count = 0
    urls = readUrls()
    while True:
        for url in urls:
            count += 1
            spawnWebBrowser(BrowserBinaryPath, url)
            if count % 10 == 0:
                time.sleep(10)
                stopWebBrowser()
        time.sleep(10)
        stopWebBrowser()
    jobCompleted = True

if __name__ == "__main__":
    main()
