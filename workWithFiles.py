def long_long_function(text_file, cutted_file):

    lorem_file = open(text_file)
    list_lorem_file = lorem_file.read()
    list_split = list_lorem_file.split('. ')
    cutted_list_split = '. '.join(list_split[-15:])

    truncated_lorem = open(cutted_file, 'w')
    truncated_lorem.write(cutted_list_split)
    truncated_lorem.close()

    lorem_file.close()



    open_file = open(cutted_file)
    read_file = open_file.read()
    print(read_file)






long_long_function(r'/Users/user/Downloads/lorem_ipsum.txt', r'/Users/user/Downloads/lorem_ipsum1.txt')