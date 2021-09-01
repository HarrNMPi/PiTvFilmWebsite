import simplenote

sn = simplenote.Simplenote("email", "*************")

# print(sn.get_note_list())


def get_list(content):
    item = ""
    item_list = []
    for i in range(len(content)):
        if content[i] == "[":
            item_list.append(item)
            item = "["
        else:
            item = item + content[i]
    item_list.append(item)
    for i in range(len(item_list)):
        item_list[i] = item_list[i].replace('\n', '')
        item_list[i] = item_list[i].replace('-', '')
        item_list[i] = item_list[i].rstrip()
    return item_list


def remove_watched(item_list):
    wheel_list = []
    for i in range(len(item_list)):
        if item_list[i][1] == ' ':
            wheel_list.append(item_list[i])
    return wheel_list


def remove_brackets(item_list):
    for i in range(len(item_list)):
        item_list[i] = item_list[i].replace('[', '')
        item_list[i] = item_list[i].replace(']', '')
        item_list[i] = item_list[i].strip()
    return item_list


def get_list_formatted(content):
    raw_list = get_list(content)
    no_watched_list = remove_watched(raw_list)
    formatted = remove_brackets(no_watched_list)
    return formatted


def get_film_list():
    content = sn.get_note("a74f34d0-6494-4388-8206-eac773459ed9")[0].get("content")
    film_list = get_list_formatted(content)
    return film_list


def get_tv_list():
    content = sn.get_note("a1dac99ff06d4e39a50dee8b8f61e9c8")[0].get("content")
    tv_list = get_list_formatted(content)
    return tv_list


def get_book_list():
    content = sn.get_note("d37783453d284856bb3846d684c0a9cc")[0].get("content")
    book_list = get_list_formatted(content)
    return book_list

