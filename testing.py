import codecs

if __name__ == '__main__':
    # f = codecs.open('C:/Users/ananda/Downloads/flowfile',encoding='utf-8')

    names = ['Anand','Rahul','Fds','Rui']

    filtered_names = []
    for i in range(len(names)):
        if len(names[i]) > 3:
            filtered_names.append(names[i])

    filtered_names = [name for name in names if len(name) > 3]