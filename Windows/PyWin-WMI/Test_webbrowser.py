import os
import wmi
import _winreg

BrowserBinaryPath = "C:\Program Files (x86)\Internet Explorer\iexplore.exe"

jobCompleted = False

def readUrls():
    urls = [
        "www.tudou.com",
        "www.sina.com",
        "www.douban.com"
    ]
    return urls

def spawnWebBrowser(browser, url):
    if not os.path.exists(browser):
        return
        
    c = wmi.WMI()
    process = c.Win32_Process
    cmdline = "%s %s" % (browser, url)
    process_id, result = process.Create(CommandLine = cmdline)
    watcher = c.watch_for(notification_type = "operation", wmi_class = "Win32_Process", delay_secs = 3, ProcessId = process_id)
    watcher()
    print "Complete accessing web url: %s" % url

def main():
    urls = readUrls()
    for url in urls:
        spawnWebBrowser(BrowserBinaryPath, url)        
    jobCompleted = True

if __name__ == "__main__":
    main()
