import wmi 
import os 
import sys 
import time 
 
def sys_version():
    c = wmi.WMI()
    for sys in c.Win32_OperatingSystem():
        print "Version:%s" % sys.Caption.encode("UTF8"),"Vernum:%s" % sys.BuildNumber
        print sys.OSArchitecture.encode("UTF8")
        print sys.NumberOfProcesses
 
def cpu_mem():
    c = wmi.WMI()
    for processor in c.Win32_Processor():
        #print "Processor ID: %s" % processor.DeviceID
        print "Process Name: %s" % processor.Name.strip()
    for Memory in c.Win32_PhysicalMemory():
        print "Memory Capacity: %.fMB" %(int(Memory.Capacity)/1048576) 
 
def cpu_use():
    c = wmi.WMI()
    while True:
        for cpu in c.Win32_Processor():
            timestamp = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime())
            print '%s | Utilization: %s: %d %%' % (timestamp, cpu.DeviceID, cpu.LoadPercentage)
            time.sleep(5)

def disk():
    c = wmi.WMI()
    for physical_disk in c.Win32_DiskDrive():
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                print physical_disk.Caption.encode("UTF8"), partition.Caption.encode("UTF8"), logical_disk.Caption 
                
    for disk in c.Win32_LogicalDisk(DriveType=3):
        print disk.Caption, "%0.2f%% free" % (100.0 * long (disk.FreeSpace) / long (disk.Size)) 
      
def network():
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        print "MAC: %s" % interface.MACAddress
        for ip_address in interface.IPAddress:
            print "ip_address: %s" % ip_address
            
    for s in c.Win32_StartupCommand():
        print "[%s] %s <%s>" % (s.Location.encode("UTF8"), s.Caption.encode("UTF8"), s.Command.encode("UTF8"))
        
    for process in c.Win32_Process():
        print process.ProcessId, process.Name
                                             
def main():
    sys_version()
    cpu_mem()
    disk()
    network()
    cpu_use()
    
if __name__ == '__main__':
    main() 
