#Jacob Sexton 6/30/25
#defining the read file choice
def read_file(filename):
    try:
        #Open file
        f = open(filename, 'r')
        #proccess file
        print("\nUser Info:")
        for line in f:
            print(line.strip('\n'))
        #close file
        f.close()
    except:
        print("Could not read the file.")
#defining the write file choice and 
def write_file(filename):
    try:
        #the inputs for adding info to the file
        f_name = input("First Name:")
        l_name = input("Last Name: ")
        address = input("Street Address: ")
        city = input("City: ")
        state = input("State:")
        zip_code = input("Zip Code: ")
        #Open
        f = open(filename, 'w')
        #proccess
        f.write(f_name + '\n')
        f.write(l_name + '\n')
        f.write(address + '\n')
        f.write(city + '\n')
        f.write(state + '\n')
        f.write(zip_code + '\n')
        #close
        f.close()
        #user feedback to when file is done
        print("File has been saved")
    except:
        print("Error whilst writing to the file.")
#my main questionare about filename and prompting the user about which they wanna do
def main():
    filename = input("Name of File: ")
    action = input("Read or Write? (R/W): ").lower()
    if action == 'r':
        read_file(filename)
    elif action == 'w':
        write_file(filename)
    else:
        print("Invalid choice.")
if __name__ == '__main__':
    main()
