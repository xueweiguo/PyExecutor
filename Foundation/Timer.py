class Timer:
    def __init__(self, wnd, ms, call):
        self.__wnd = wnd
        self.__ms = ms
        self.__call = call
        self.__running = False

    def start(self):
        if not self.__running:
            self.__wnd.after(0, self.__on_timer)
            self.__running = True

    def stop(self):
        if self.__running:
            self.__running = False

    def is_running(self):
        return self.__running

    def __on_timer(self):
        if self.__running:
            self.__call()
            self.__wnd.after(self.__ms, self.__on_timer)
