from os import listdir, system

PACKAGE_NAME = "piskvorky-client"

def compile_ui():
    for file in listdir("ui/"):
        out_filename = file.split(".ui")[0] + ".py"
        system(f"pyside6-uic ui/{file} -o {PACKAGE_NAME}/ui/generated/{out_filename}")


if __name__ == "__main__":
    compile_ui()

