import os

path_package = os.path.dirname(os.path.realpath(__file__))
path_file = "\\".join([path_package.rsplit("\\", 1)[0], "file"])
url_student = "\\".join([path_file, "student.txt"])
url_user = "\\".join([path_file, "user.txt"])
