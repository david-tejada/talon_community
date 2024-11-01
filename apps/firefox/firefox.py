from talon import Context, Module, actions, app, ui, skia
from talon.experimental.locate import locate
import numpy as np

ctx = Context()
mod = Module()
apps = mod.apps
apps.firefox = "app.name: Firefox"
apps.firefox = "app.name: Firefox Developer Edition"
apps.firefox = "app.name: firefox"
apps.firefox = "app.name: Firefox-esr"
apps.firefox = "app.name: firefox-esr"
apps.firefox = "app.name: LibreWolf"
apps.firefox = "app.name: waterfox"
apps.firefox = r"""
os: windows
and app.name: Firefox
os: windows
and app.exe: /^firefox\.exe$/i
"""
apps.firefox = """
os: mac
and app.bundle: org.mozilla.firefox
"""

# Make the context match more specifically than anything else. This is important, eg. to
# override the browser.go_home() implementation in tags/browser/browser_mac.py.
ctx.matches = r"""
os: windows
os: linux
os: mac
tag: browser
app: firefox
"""


@mod.action_class
class Actions:
    def firefox_bookmarks_sidebar():
        """Toggles the Firefox bookmark sidebar"""

    def firefox_history_sidebar():
        """Toggles the Firefox history sidebar"""


@ctx.action_class("user")
class UserActions:
    def tab_close_wrapper():
        actions.sleep("180ms")
        actions.app.tab_close()


@mod.action_class
class Actions:
    def run_devtools_command(command: str) -> None:
        """Run a command in the devtools console"""


@ctx.action_class("user")
class user_actions:
    def tab_close_wrapper():
        actions.sleep("300ms")
        actions.app.tab_close()

    # Doesn't always focus the pane. If the split console is open it focuses it.
    def devtools_console_pane():
        actions.key("cmd-alt-k")

    def devtools_debugger_pane():
        actions.key("cmd-alt-z")

    def devtools_inspector_pane():
        actions.key("cmd-alt-c")

    def devtools_search_file(name: str) -> None:
        actions.user.devtools_click_file_area()
        actions.key("cmd-p")
        actions.sleep("200ms")
        actions.user.paste(name)

    def devtools_click_file_area() -> None:
        path = f"{actions.path.talon_user()}/images/breakpoints-pane-button.png"
        matches = locate(path, threshold=0.90)

        if len(matches) == 0:
            path = f"{actions.path.talon_user()}/images/collapsed-breakpoints-pane-button.png"
            matches = locate(path, threshold=0.90)

        if len(matches) == 0:
            actions.user.devtools_debugger_pane()
            actions.sleep("200ms")
            # raise Exception("Breakpoints pane button not found. Make sure you are in the debugger panel.")

        match = matches[0]

        actions.mouse_move(match.x - 50, match.y + 50)
        actions.mouse_click(0)

    def devtools_go_to_line(number: int) -> None:
        actions.user.devtools_click_file_area()
        actions.key("cmd-j")
        actions.insert(number)
        actions.key("enter")

    def devtools_conditional_breakpoint():
        # This doesn't work at the moment because of this bug:
        # https://bugzilla.mozilla.org/show_bug.cgi?id=1840390
        actions.key("cmd-shift-b")

    def devtools_add_watch_expression(name: str) -> None:
        path = f"{actions.path.talon_user()}/images/watch-expression-plus.png"
        matches = locate(path, threshold=0.95)

        if len(matches) == 0:
            raise Exception(
                "Add expression button not found. Make sure you are in the debugger panel."
            )

        match = matches[0]
        x, y, width, height = match.x, match.y, match.width, match.height
        actions.mouse_move(x + width - 20, y + height / 2)
        actions.mouse_click(0)
        camel = actions.user.formatted_text(name, "PRIVATE_CAMEL_CASE")
        actions.insert(camel)


@ctx.action_class("browser")
class BrowserActions:
    def focus_page():
        actions.browser.focus_address()
        actions.edit.find()
        actions.sleep("180ms")
        actions.key("escape")

    def go_home():
        actions.key("alt-home")
