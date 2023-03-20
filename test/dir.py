import os

print(os.getcwd())

script_path = os.path.realpath(os.path.dirname(__file__))
print(f"script path: {script_path}")
path = os.path.join(script_path, "recipes")

if os.path.exists(path):
    print('folder exists')
else:
    print(f"new folder path: {path}")
    os.mkdir(path)

