from selenium import webdriver

def main():
    routine = open("routine.txt", "r")
    url_in = routine.readline()[1:]
    url_out = routine.readline()[1:]
    driver_in = webdriver.Firefox()
    driver_in.get(url_in)
    driver_out = webdriver.Firefox()
    driver_out.get(url_out)

    input("Please log in on both windows. Press enter once done.")

    for line in routine:
        if(line[0:1] == "i"):
            exec(driver_in, line[2:])
        elif(line[0:1] == "o"):
            exec(driver_out, line[2:])


def exec(driver, command):
    if(command[0:1] == "g"):
        driver.get(command[2:])

if __name__ == '__main__':
    main()