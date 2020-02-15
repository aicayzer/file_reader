# def line_count():
#     count = 0
#     for line in file:
#         count += 1
#     file.seek(0)
#     return(count)


with open("story.txt", "r") as file:
    #     lines = (line_count())
    print(file.read())
#     for c in file.read():
#         print(c)
#     # characters_with_spaces = (character_count_ws())

# # print(lines)
