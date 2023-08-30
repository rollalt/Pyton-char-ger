import tkinter as tk


class ToggleButtonLBL(tk.Label):

    ON_config = {'bg': 'green',
                 'text': 'button is ON',
                 'relief': 'sunken',
                 }
    OFF_config =  {'bg': 'white',
                 'text': 'button is OFF',
                 'relief': 'raised',
                 }

    def __init__(self, parent, *args, command=None, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.toggled = False
        self.config = self.OFF_config
        self.config_button()

        self.bind("<Button-1>", self._toggle_helper)
        self.bind("<ButtonRelease-1>", self._toggle)
        self.command = command

    def _toggle_helper(self, *args):
        return 'break'

    def _toggle(self, dummy_event):
        self.toggle()
        self.cmd()

    def toggle(self, *args):
        if self.toggled:   # True = ON --> toggle to OFF
            self.config = self.OFF_config
        else:
            self.config = self.ON_config
        self.toggled = not self.toggled
        self.config_button()
        return 'break'

    def config_button(self):
        self['bg'] = self.config['bg']
        self['text'] = self.config['text']
        self['relief'] = self.config['relief']
        return "break"

    def __str__(self):
        return f"{self['text']}, {self['bg']}, {self['relief']}"

    def cmd(self):
        self.command()


def button_placeholder():
    print('toggling now!')


if __name__ == '__main__':

    root = tk.Tk()

    button = ToggleButtonLBL(root, command=button_placeholder)
    button.pack()

    root.mainloop()
