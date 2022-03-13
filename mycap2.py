filename=input("Input the filename : ")
x=list(filename.split("."))
del x[0]
if x==['py']:
    print("The extension of the file is python")
elif x==['cpp']:
    print("The extension of the file is c++")
elif x==['c']:
    print("The extension of the file is c")
elif x==['html']:
    print("The extension of the file is Hyper text markup language")
else:
    print("No extensions matched")
