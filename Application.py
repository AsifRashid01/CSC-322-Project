from tkinter import *

class Application(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self._frame = None
        self.show_frame(LoginPage)

    def show_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

        if frame_class == LoginPage:
            Tk.wm_title(self, "Login Page")
        elif frame_class == GuestUserPage:
            Tk.wm_title(self, "Guest User Page")
        elif frame_class == OrdinaryUserPage:
            Tk.wm_title(self, "Ordinary User Page")
        elif frame_class == SuperUserPage:
            Tk.wm_title(self, "Super User Page")
        else:
            Tk.wm_title(self, "DSS")

    current_logged_in_user = '' # variable to keep track of a currently logged in user

if __name__ == "__main__":
    from Pages.LoginPage import LoginPage
    from Pages.GuestUserPage import GuestUserPage
    from Pages.OrdinaryUserPage import OrdinaryUserPage
    from Pages.SuperUserPage import SuperUserPage
    app = Application()
    app.mainloop()
