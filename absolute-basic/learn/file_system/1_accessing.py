import pathlib

# Create a new path object for the current directory

## 1 from a string literal "/Users/aiman/Python/Experiments/path_python_basic/learn/file_system.py"
current_file_path = pathlib.Path(
    "/Users/aiman/Python/Experiments/path_python_basic/learn/file_system.py"
)
print(f"current_file_path: {current_file_path}")

## 2 from Path.cwd() or Path.home() class method
cwd = pathlib.Path.cwd()  # (dynamic) current working directory
print(f"cwd: {cwd}")

home = pathlib.Path.home()  # home directory of the current user
print(f"home: {home}")

## 3 "/" operator: joinpath
learn_path_1 = cwd / "learn"
print(f"learn_path_1: {learn_path_1}")

learn_path_2 = cwd.joinpath("learn")
print(f"learn_path_2: {learn_path_2}")

print("--------------------------------")
# Checking whether a file path exists
print(f"learn_path_1 exists: {learn_path_1.exists()}")
print(f"is cwd a directory: {cwd.is_dir()}")
print(f"is cwd a file: {cwd.is_file()}")
unknown_path = cwd.joinpath("unknown")
print(f"unknown_path exists: {unknown_path.exists()}")
print(f"is unknown_path a directory: {unknown_path.is_dir()}")
print(f"is unknown_path a file: {unknown_path.is_file()}")


print("--------------------------------")
# Absolute vs Relative Paths
absolute_path = pathlib.Path(
    "/Users/aiman/Python/Experiments/path_python_basic/learn/file_system.py"
)
print(f"absolute_path: {absolute_path}")
## check if the path is absolute
print(f"absolute_path is absolute: {absolute_path.is_absolute()}")

relative_path = pathlib.Path("file_system.py")
print(f"relative_path: {relative_path}")
print(f"relative_path is absolute: {relative_path.is_absolute()}")
## resolve relative path to an absolute path
print(f"relative_path is resolved: {relative_path.resolve()}")


print("--------------------------------")
# Accessing Path Components
print(f"absolute_path parent: {absolute_path.parent}")
for parent in absolute_path.parents:
    print(f"parent: {parent}")

print(f"absolute_path anchor: {absolute_path.anchor}")
print(f"relative_path anchor: {relative_path.anchor}")

print(f"absolute_path name: {absolute_path.name}")
print(f"absolute_path stem: {absolute_path.stem}")
print(f"absolute_path suffix: {absolute_path.suffix}")
