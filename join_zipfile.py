def join_zipfile(path=./,fn=archive_name.zip,package_size_megabyte=100,filenumbers)
    outfile = filename   #your zip file name  "--------.zip"
        packet_size = int(1024*1024*package_size_megabyte)   # bytes
    filenumbers=fn   #number of files you want to join
    for i in range(filenumbers+1):
        with open("{}{}.zip{:03}".format(path,outfile, i), "rb") as packet:
            col=packet.read(packet_size)

            with open("{}{}02.zip".format(path,outfile), "ab+") as mainpackage:
                mainpackage.write(col)
