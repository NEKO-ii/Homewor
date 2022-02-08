import os

path_package = os.path.dirname(os.path.realpath(__file__))
path_file = "\\".join([path_package.rsplit("\\", 1)[0], "file"])
path_import = "\\".join([path_file, "import"])
path_export = "\\".join([path_file, "export"])
url_student = "\\".join([path_file, "SU", "student.txt"])
url_user = "\\".join([path_file, "SU", "user.txt"])
