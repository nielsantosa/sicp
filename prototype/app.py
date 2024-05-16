class Application:
    def define(self, name, value):
        """
        Define a variable
        """
        setattr(self, name, value)

    def call(self, name):
        """
        Calling variable
        """
        if hasattr(self, name):
            return getattr(self, name)
        else:
            print("Error")
            return None

    def f(self, func, *args):
        return func(*args)


if __name__ == "__main__":
    app = Application()

    # Define variable
    app.define("x", 5)
    print(app.call("x"))
