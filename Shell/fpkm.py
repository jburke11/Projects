fp = open("genes.fpkm_tracking", "r")
output = open("fpkm_values.txt", "w")
if not fp.closed:
    with open("genes.fpkm_tracking", "r") as fp:
        header = fp.readline()
        header_list = header.rstrip().split()
        print ("\t".join((header_list[0], header_list[9])), file=output)
        for line in fp:
            list1 = line.rstrip().split()
            print ("\t".join((list1[0], list1[9])), file=output)
output.close()
