import logging
logging.basicConfig(level=logging.DEBUG)

#Task 1: Hello: Write a hello function that takes no arguments and returns Hello!.
def hello():
    return("Hello!")


#Task 2: Greet with a Formatted String
def greet(name):
    return("Hello, " + name + "!") 


#Task 3: Calculator
# def calc(num1, num2, action="multiply"):
#     try: 
#         num1 = int(num1)
#         num2 = int(num2)
#     except Exception:
#         return "You can't multiply those values!"       
#     try:
#         if action == "add":
#             return num1 + num2
#         elif action=="subtract":
#             return num1 - num2
#         elif action == "multiply":
#             return num1 * num2
#         elif action =="power":
#             return num1 ** num2   
#         elif action == "modulo":
#             return num1 % num2
#         elif action == "int_divide":
#             return num1 // num2
#         elif action =="power":
#             return num1 ** num2
#         elif action == "divide":
#             return num1 / num2          
#         else:
#             return num1 * num2
#     except ZeroDivisionError:
#         return "You can't divide by 0!"
    
def calc(num1, num2, action="multiply"):
    try: 
        num1 = int(num1)
        num2 = int(num2)
    except Exception:
        return (f"Invalid numeric input")       
    try:
        match action:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "power":
                return num1 ** num2   
            case "modulo":
                return num1 % num2
            case "int_divide":
                return num1 // num2
            case "divide":
                return num1 / num2          
            case _:
                return num1 * num2
    except ZeroDivisionError:
        return "You can't divide by 0!"


# Task 4: Data Type Conversion
def data_type_conversion(value, type_name):
    try:
        match type_name:
            case "int":
                return int(value)
            case "str":
                return str(value)
            case "float":
                return float(value)
    except Exception:
        return (f"You can't convert {value} into a {type_name}")


# Task 5: Grading System, Using *args
def grade(*args):
    try:
        return "A" if sum(args) >= 90 \
        else "B" if sum(args) >= 80 \
        else "C" if sum(args) >=70 \
        else "D" if sum(args) >= 60 \
        else "F" 
    except Exception:
        return "Invalid data was provided."


# Task 6: Use a For Loop with a Range
def repeat(string, count):    
    result = ""
    for i in range(count):
        result += string
    return result


# Task 7: Student Scores, Using **kwargs
def student_scores(request="best", **kwargs):  
        try:               
            if request == "mean":
                return int(sum(kwargs.values())/len(kwargs))
            else:
                return max(kwargs, key=kwargs.get)
        except ZeroDivisionError:
            return "Provide scores"
                  

# Task 8: Titleize, with String and List Operations
def titleize(string):
    words = string.split()
    littleWords = ["a", "on", "an", "the", "of", "and", "is", "in"]
    result = []

    for i, word in enumerate(words):           
        if word.lower() not in littleWords or i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return " ".join(result)
        
# print(titleize("someday IS somehow on"))


# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:       
        if letter in guess:
             result += letter
        else:
            result += "_"
    return result


# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(string):
    vowels = "aeiou"
    words = string.lower().split()
    result = []
    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        elif word.startswith("qu"):
            result.append(word[2:] + "quay")
        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    result.append(word[i:] + word[:i] + "ay")
                    break
    return " ".join(result)

print(pig_latin("the quick brown fox"))