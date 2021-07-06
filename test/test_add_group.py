def test_add_group(app, xl_groups):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(xl_groups)
    new_list = app.groups.get_group_list()
    old_list.append(xl_groups)
    assert sorted(old_list) == sorted(new_list)
