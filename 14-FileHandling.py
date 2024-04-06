
if __name__ == '__main__':


    # Using 'with' ensures the file is closed when out of with block
    with open('C:/Users/ananda/Downloads/message.json','r') as f:
        # read() method reads the file contents in a string
        json_as_string = f.read()
        print(json_as_string)

    # different read modes are: r,w,a,x (create), + (update)
    # default mode for file open is text (t), we can specify binary (b) also

    # code to copy an image
    with open('C:/Users/ananda/Downloads/Untitled Diagram.jpg', 'rb') as img:
        with open('C:/Users/ananda/Desktop/VPC-Flow-Diagram.jpg','wb') as img_copy:
            for c in img:
                img_copy.write(c)

    # reading file line by line
    with open('C:/Users/ananda/Downloads/message.json') as f:
        line = f.readline()
        while line:
            print(line)
            line = f.readline()

    # storing lines in a list
    with open('C:/Users/ananda/Downloads/message.json','r') as f:
        lines = f.readlines()
        print(lines)


    ## ---------------- CSV Files ---------------------------------
    import csv
    with open('C:/Users/ananda/Downloads/2015-summary.csv','r') as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            print(row)  # each row is a list, we can use index to get col

    # To use name of the columns instead of index
    with open('C:/Users/ananda/Downloads/2015-summary.csv', 'r') as f:
        dict_reader = csv.DictReader(f,delimiter=',')
        for i, row in enumerate(dict_reader):
            print(f"Desination country {i} is {row['DEST_COUNTRY_NAME']}")


    ## ---------------- JSON Files --------------------------------
    import json
    with open('C:/Users/ananda/Downloads/message.json','r') as f:
        # load json into a dictionary
        reader = json.load(f)
        print(reader['protoPayload']['resourceName'])

    # there's another method json.loads which
    # is used to parse json from a string
    reader = json.loads(json_as_string)
    print(reader)
