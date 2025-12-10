import logging
logging.basicConfig(level=logging.INFO)


#Task 1: Writing and Testing a Decorator
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        positional = list(args) if args else "none"
        keyword = kwargs if kwargs else "none"
        result = func(*args, **kwargs)

        with open("decorator.log", "a") as f:
            f.write(f"function: {func.__name__}\n")
            f.write(f"positional parameters: {positional}\n")
            f.write(f"keyword parameters: {keyword}\n")
            f.write(f"return: {result}\n\n")

        return result
    return wrapper

@logger_decorator
def greet():
    print("Python turn")

greet()