from talon import Context, Module, actions

ctx = Context()
mod = Module()
apps = mod.apps
apps.firefox = "app.name: Firefox"
apps.firefox = "app.name: Firefox Developer Edition"
apps.firefox = "app.name: firefox"
apps.firefox = """
os: windows
and app.name: Firefox
os: windows
and app.exe: firefox.exe
"""
apps.firefox = """
os: mac
and app.bundle: org.mozilla.firefox
"""

apps.firefox = """
os: linux
and app.name: firefox-aurora
"""

ctx.matches = r"""
app: firefox
"""

@mod.action_class
class Actions:
    def run_devtools_command(command: str) -> None:
        """Run a command in the devtools console"""

@ctx.action_class("user")
class user_actions:
    def tab_close_wrapper():
        actions.sleep("300ms")
        actions.app.tab_close()
    def run_devtools_command(command: str) -> None:
        actions.key("cmd-alt-k")
        actions.edit.delete_line()
        actions.user.paste(command)
        actions.key("enter")
    

@ctx.action_class('browser')
class BrowserActions:
    # TODO
    # action(browser.address):
    # action(browser.title):
    def go(url: str):
        actions.browser.focus_address()
        actions.sleep("50ms")
        actions.insert(url)
        actions.key("enter")

    def focus_search():
        actions.browser.focus_address()

    def submit_form():
        actions.key("enter")
