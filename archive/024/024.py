# file-syntax


# WRITE
the_file = open("./archive/024/the_file.txt", mode="w")
command = the_file.write("hi, world!")
the_file.close()


# READ
the_file = open("./archive/024/the_file.txt", mode="r")
contents = the_file.read()

a = contents.find(',')
b = contents[:a]
c = contents[a+1:]

print(b)
print(c)
the_file.close()


# MAIL
# GET_FORMAT
open_mail_format = open("./archive/024/mail/mail_format.txt", mode="r")
mail_format = open_mail_format.read()

# GET_NAMES
open_names = open("./archive/024/mail/names.txt", mode="r")
string_names = open_names.read()
names = (string_names.split("\n"))


# MAGIC
for i in range(names.__len__()):
    new_mail_format = mail_format.replace("{name}", names[i])
    print("\n" + new_mail_format)
