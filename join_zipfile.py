def split_zipfile(fn="archive_name",package_size_megabyte=100,path="./"):
    inputfile = fn   #your zip file name  "--------.zip"
    packet_size = int(1024*1024*package_size_megabyte)   # bytes

    with open(path+inputfile+'.zip', "rb") as output:
        filecount = 0
        while True:
            data = output.read(packet_size)
            if not data:
                print("FINISHED")
                break   # we're done
            print("{}{}.zip{:03}".format(path,inputfile, filecount))
            with open("{}{}.zip{:03}".format(path,inputfile, filecount), "wb") as packet:
                packet.write(data)
            filecount += 1


if __name__ == "__main__":
    split_zipfile()
