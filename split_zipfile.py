outfile = archive_name   #your zip file name  "--------.zip"
packet_size = int(1.5 * 1024**3)   # bytes

with open(outfile, "rb") as output:
    filecount = 0
    while True:
        data = output.read(packet_size)
        print(len(data))
        if not data:
            break   # we're done
        with open("{}{:03}".format(outfile, filecount), "wb") as packet:
            packet.write(data)
        filecount += 1
