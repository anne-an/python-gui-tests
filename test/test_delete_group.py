import random


def test_delete_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) == 1:
        app.groups.add_new_group("my group")
    groups_with_ids = app.groups.get_group_list_with_ids()
    group = random.choice(groups_with_ids)
    app.groups.delete_group_by_id(group[0])
    new_list = app.groups.get_group_list()
    old_list.remove(group[1])
    assert sorted(old_list) == sorted(new_list)