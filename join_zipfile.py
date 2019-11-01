outfile = "archive_name"
packet_size = int(1024*1024*100)   # bytes
filenumbers=9   #number of files you want to join
for i in range(filenumbers):
    with open("{}.zip{:03}".format(outfile, i), "rb") as packet:
        col=packet.read(packet_size)

        with open("{}02.zip".format(outfile), "ab+") as mainpackage:
            mainpackage.write(col)
