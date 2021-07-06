import random


def test_delete_group(app):
    old_list = app.groups.get_group_list()
    # group = random.choice(old_list)
    # print("GROUP   " + group)
    app.groups.delete_group("my group")
    new_list = app.groups.get_group_list()
    old_list.remove("my group")
    assert sorted(old_list) == sorted(new_list)