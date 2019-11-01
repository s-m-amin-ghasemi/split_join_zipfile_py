import os
from math import ceil

def join_zipfile(fn="archive_name",package_size_megabyte=100,filenumbers=2,path="./"):
    outfile = fn   #your zip file name  "--------.zip"
    packet_size = ceil(1024*1024*package_size_megabyte)   # bytes
    filenumbers=int(os.path.getsize(path+outfile+'.zip')/packet_size)   #number of files you want to join
    for i in range(filenumbers+1):
        with open("{}{}.zip{:03}".format(path,outfile, i), "rb") as packet:
            col=packet.read(packet_size)

            with open("{}{}02.zip".format(path,outfile), "ab+") as mainpackage:
                mainpackage.write(col)
    print("FINISHED")


if __name__ == "__main__":
    join_zipfile()
