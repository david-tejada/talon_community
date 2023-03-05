window (new|open): app.window_open()
glide: app.window_next()
slide: app.window_previous()
window close: app.window_close()
focus <user.running_applications>: user.switcher_focus(running_applications)
# following only works on windows. Can't figure out how to make it work for mac. No idea what the equivalent for linux would be.
# focus$: user.switcher_menu()
running list: user.switcher_toggle_running()
running close: user.switcher_hide_running()
launch <user.launch_applications>: user.switcher_launch(launch_applications)

snap <user.window_snap_position>: user.snap_window(window_snap_position)
snap next [screen]: user.move_window_next_screen()
snap last [screen]: user.move_window_previous_screen()
snap screen <number>: user.move_window_to_screen(number)
snap <user.running_applications> <user.window_snap_position>:
    user.snap_app(running_applications, window_snap_position)
snap <user.running_applications> [screen] <number>:
    user.move_app_to_screen(running_applications, number)

flip it: key(cmd-tab)
^coder: user.switcher_launch("/Applications/Visual Studio Code.app")
^foxy: user.switcher_launch("/Applications/Firefox.app")
^crome: user.switcher_launch("/Applications/Google Chrome.app")
^browser: user.switcher_launch("/Applications/Brave Browser.app")
^bitwarden: user.switcher_launch("/Applications/Bitwarden.app")
^warpy: user.switcher_launch("/Applications/Warp.app")

^code (knausj | mouse | naus): user.system_command("/opt/homebrew/bin/code /Users/david/.talon/user/knausj_talon")
^code rango: user.system_command("/opt/homebrew/bin/code /Users/david/Code/rango")
^code (knausj | mouse | naus) work tree: user.system_command("/opt/homebrew/bin/code /Users/david/Code/knausj_worktree")
^code rango talon: user.system_command("/opt/homebrew/bin/code /Users/david/.talon/user/rango-talon")
