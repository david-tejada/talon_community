tag: user.tabs
-
tabby: app.tab_open()
tab left: app.tab_previous()
tab up: app.tab_previous()
tab right: app.tab_next()
tab down: app.tab_next()
tab close: user.tab_close_wrapper()
tab (reopen|restore): app.tab_reopen()
tab <number>: user.tab_jump(number)
tab (last | final): user.tab_final()
tab duplicate: user.tab_duplicate()
pick up <number_small>: key("up:{number_small} enter")
