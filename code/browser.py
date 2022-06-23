from urllib.parse import urlparse

from talon import Context, Module, actions, clip

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: browser
"""


@mod.action_class
class Actions:
    def browser_address_fallback() -> str:
        """Retrieves the url using browser.address() with a fallback"""

    def browser_copy_address():
        """Copies the current url to the clipboard"""


def is_url(url):
    try:
        # Valid if url successfully parsed
        result = urlparse(url)
        # and contains both scheme (e.g. http) and netloc (e.g. github.com)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


@ctx.action_class("user")
class UserActions:
    def browser_address_fallback() -> str:
        try:
            address = actions.browser.address()
            if address:
                return address
        except Exception:
            pass
        actions.browser.focus_address()
        actions.sleep("50ms")
        with clip.capture() as s:
            actions.edit.copy()
        actions.key("escape")
        actions.key("tab")
        return s.text()

    def browser_copy_address():
        address = actions.user.browser_address_fallback()
        clip.set_text(address)


@ctx.action_class("browser")
class BrowserActions:
    def address():
        # Split title by space, check each token and token[1: -1] (it might be in brackets) for valid url.
        # Prioritize last one if multiple are valid, return empty string if none is valid.
        tokens = (
            url[1:-1] if not is_url(url) else url
            for url in reversed(actions.win.title().split(" "))
        )
        return next((url for url in tokens if is_url(url)), "")
