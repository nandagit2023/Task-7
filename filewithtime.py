# import module for timestamp
from datetime import datetime

# get current timestamp
current_timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def timestamp(x):
    str_current_timestamp = str(x)  # type cast to string
    file_name = str_current_timestamp + ".txt"  # create a file name with timestamp with extension
    file = open(file_name, 'w')
    file.writelines(str_current_timestamp)  # write timestamp inside the file
    print("File created in local with name of the file as : ", file.name)
    file.close()


print(timestamp(current_timestamp))
