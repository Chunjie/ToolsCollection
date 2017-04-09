import wmi
import _winreg
import win32evtlog

def run1():
    #fd = open("E:\\test.log", "w")
    #fd.write("Result is:\n")
    
    c = wmi.WMI(privileges=["Security"])
    #c = wmi.WMI()
    watcher = c.watch_for(notification_type = "creation", wmi_class = "Win32_NTLogEvent", Type = "error")
    while True:
        error = watcher()
        #fd.write("Error in %s log: %s\n" % (error.Logfile, error.Message))
        print("Error in %s log: %s\n" % (error.Logfile, error.Message))
    #fd.close()

def run2():
    server = 'localhost'
    logtype = 'System'
    hand = win32evtlog.OpenEventLog(server,logtype)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)
    while True:
        events = win32evtlog.ReadEventLog(hand, flags,0)
        if events:
            for event in events:
                print 'Event Category:', event.EventCategory
                print 'Time Generated:', event.TimeGenerated
                print 'Source Name:', event.SourceName
                print 'Event ID:', event.EventID
                print 'Event Type:', event.EventType
                data = event.StringInserts
                if data:
                    print 'Event Data:'
                    for msg in data:
                        print msg
                print "=====================>"

def main():
    #run1()
    run2()
	
if __name__ == "__main__":
    main()
