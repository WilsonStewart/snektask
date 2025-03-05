from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static, ListItem, Label, OptionList
from textual.containers import Grid
from snektask.db import Task, db


class Snektask(App):
    """The main snektask app."""

    CSS_PATH = "grid_layout_main.tcss"

    def get_tasks():
        for t in Task.select():
            return t.name

    def compose(self) -> ComposeResult:
        yield Static("Tasks", classes="column-heading")
        # yield Static("Hold", classes="column-heading")
        # yield Static("Today", classes="column-heading")
        yield OptionList(get_tasks())
        # yield OptionList()
        # yield OptionList()
        yield Header()
        yield Footer()

    # BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    # def compose(self) -> ComposeResult:
    #     """Create child widgets for the app."""
    #     yield Header()
    #     yield Footer()

    # def action_toggle_dark(self) -> None:
    #     """An action to toggle dark mode."""
    #     self.theme = (
    #         "textual-dark" if self.theme == "textual-light" else "textual-light"
    #     )


def get_tasks():
    for task in Task.select():
        return task


def start_app():
    db.connect()
    db.create_tables([Task])
    for r in Task.select():
        print(r.name)
    app = Snektask()
    app.run()


if __name__ == "__main__":
    start_app()
