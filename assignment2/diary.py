try:
    with open("diary.txt", "a") as file:
        firstLine = True
        while True:
            if firstLine:
                prompt = "What happened today? "
            else:
                prompt = "What else? "
            message = input(prompt)
            file.write(message + "\n")

            if message.lower() == "done for now":
                break
            firstLine = False
except Exception as e:
    print(f"An exception occurred: {e}")