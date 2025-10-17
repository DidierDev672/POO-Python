def main():
    try:
        print(1/0)
    except ZeroDivisionError:
        print("You cannot divide a value with zero")
    except:
        print("Something else went wrong")


def dataCSV():
    try:
        with open('data.csv') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        print("Explanation: We cannot load the 'data.csv' file")


def result():
    try:
        result = 1/3
    except ZeroDivisionError as err:
        print(err)
    else:
        print(f"Your answer is {result}")


x = [5, 8, 9, 13]


def find_nth_value(x, n):
    try:
        result = x[n]
    except IndexError as err:
        print(err)
    else:
        print("Your answer is ", result)


def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Please change 'y' argument to no-zero value")
    except:
        print("Something went wrong")
    else:
        print(f"Your answer is {result}")
    finally:
        print("\033[92m Code by DataCamp\033[00m")


def new_divide(x, y):
    try:
        value = 50
        x.append(value)

    except ArithmeticError as atr_err:
        print(atr_err)

    else:
        try:
            result = [i / y for i in x]
            print(result)
        except ZeroDivisionError:
            print("Please change 'y' argument to non-zero value")

        finally:
            print("\033[92m Code by DataCamp\033[00m")


def file_editor(path, text):
    try:
        data = open(path)

        try:
            data.write(text)

        except:
            print("Unable to write the data. Please add an append: 'a' or write: 'w'")

        finally:
            data.close()

    except:
        print(f"{path} file is not found!!")


def get_result():
    value = 2_000
    if value > 1_000:
        # ? Raise the ValueError
        raise ValueError("Please add a value lower than 1,000")
    else:
        print("Congratulations! You are the winner!")


def new_get_result():
    try:
        value = 2_000
        if value > 1_000:
            raise Exception("Please add a value lower than 1, 000")
        else:
            print("Congratulations! You are the winner!!")
    except ValueError as e:
        print(e)


def new_get_result_3_11():
    try:
        result = 1 / 0
    except Exception as e:
        match e:
            case ZeroDivisionError():
                print("You cannot divide by zero.")
            case NameError():
                print("Variable not defined.")

            case _:
                print("An unexpected error occurred.")


def group_exception():
    try:
        raise ExceptionGroup("Multiple errors", [
            ValueError("Bad value"), TypeError("Bad type")])

    except* ValueError as ve:
        print(f"Handling ValueError: {ve}")
    except* TypeError as te:
        print(f"Handling TypeError: {te}")


def add_note():
    try:
        raise ValueError("Invalid input")

    except ValueError as e:
        e.add_note("This happened while processing user input.")
        e.add_note("Consider validating input before processing.")
    raise


# main()

# dataCSV()
# result()

# find_nth_value(x, 6)
# find_nth_value(x, 2)

# divide(5, 3)
# divide(15, 3)

# new_divide(x, 4)
# new_divide(x, 3)

# path = "data.txt"
# text = "DataLab: Share your data analysis in a cloud-based environment--no installation required."

# file_editor(path, text)

# get_result()
# new_get_result()

# new_get_result_3_11()
# group_exception()
add_note()
