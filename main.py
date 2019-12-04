from selenium import webdriver

buffer = []

def main():
    with open("routine.txt", "r") as routine:
        url_in = routine.readline()[1:]
        url_out = routine.readline()[1:]
        driver_in = webdriver.Firefox()
        driver_in.get(url_in)
        driver_out = webdriver.Firefox()
        driver_out.get(url_out)

        input("Please log in on both windows. Press Enter once done.\n")

        for line in routine:
            if(line[0:1] == "i"):
                exec_routine(driver_in, line[2:])
            elif(line[0:1] == "o"):
                exec_routine(driver_out, line[2:])


def exec_routine(driver, command):
    if(command[0:1] == "g"):
        driver.get(command[2:])
    elif(command[0:1] == "c"):
        driver.find_element_by_xpath(command[2:]).click()
    elif(command[0:1] == "r"):
        buffer.append(driver.find_element_by_xpath(command[2:]).text)
    elif(command[0:1] == "w"):
        driver.find_element_by_xpath(command[2:]).send_keys(buffer.pop())


if __name__ == '__main__':
    main()