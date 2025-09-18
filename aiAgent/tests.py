from functions.run_python_file import run_python_file

print(run_python_file("calculator", "main.py"))                       # should show usage instructions
print(run_python_file("calculator", "main.py", ["3 + 5"]))            # run calculator with arg
print(run_python_file("calculator", "tests.py"))                      # run the calculator’s unit tests
print(run_python_file("calculator", "../main.py"))                    # outside working dir error
print(run_python_file("calculator", "nonexistent.py"))                # missing file error



