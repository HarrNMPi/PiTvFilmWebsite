import random

from AdventureChallenge import adventures


def format_input(x):
    if x == "indoors" or x == "daytime" or x == "Yes":
        return "true"
    elif x == "Either":
        return "N/A"
    else:
        return "false"


def check_indoors(adventure_answer, web_answer):
    if adventure_answer == web_answer:
        return True
    elif adventure_answer == "N/A" or web_answer == "N/A":
        return True
    else:
        return False


def check_daytime(adventure_answer, web_answer):
    if adventure_answer == web_answer:
        return True
    elif adventure_answer == "N/A" or web_answer == "N/A":
        return True
    else:
        return False


def check_supplies(adventure_answer, web_answer):
    if adventure_answer == web_answer:
        return True
    elif adventure_answer == "N/A" or web_answer == "N/A":
        return True
    else:
        return False


def diff(li1, li2):
    return list(list(set(li1) - set(li2)) + list(set(li2) - set(li1)))


def get_adventure(indoors, daytime, supplies_required):
    f = open("AdventureChallenge/completedNumbers.txt", )
    data = f.read()
    f.close()
    form_indoors = format_input(indoors)
    form_daytime = format_input(daytime)
    form_supplies = format_input(supplies_required)
    adventures_list = adventures.adventuresArray
    correct_list = []
    u = open("AdventureChallenge/completedNumbers.txt", "a")
    for adventure in adventures_list:
        if check_indoors(adventure.indoors, form_indoors) and check_daytime(adventure.daytime,
                                                                            form_daytime) and check_supplies(
            adventure.suppliesRequired, form_supplies): correct_list.append(adventure)
    rand_num = random.randint(0, len(correct_list) - 1)
    challenge_num = correct_list[rand_num].name
    check_num = "," + str(challenge_num) + ","
    if check_num in data and len(data) >= 136:
        u.close()
        return "Completed"
    elif check_num in data:
        num_found = []
        for adventure in correct_list:
            format_ad = "," + str(adventure.name) + ","
            if format_ad in data: num_found.append(adventure)
        if len(num_found) == len(correct_list):
            u.close()
            return "Please select new criteria"
        else:
            num_left = diff(correct_list, num_found)
            if len(num_left) == 1:
                u.write(str(num_left[0].name) + ",")
                u.close()
                return num_left[0].name
            else:
                rand_x = random.choice(num_left)
                u.write(str(rand_x.name) + ",")
                u.close()
                return rand_x.name
    else:
        u.write(str(challenge_num) + ",")
        u.close()
        return challenge_num
