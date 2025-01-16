import os
import pkgutil
import argparse

def execute_file(file_path):
    """Execute a Python file by its file path."""

    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return

    try:
        print(f"Execution Started: {file_path}")
        with open(file_path, 'r') as file:
            file_content = file.read()
        exec(file_content, {'__name__': '__main__'})
        print(f"Successfully executed: {file_path}")
    except Exception as e:
        print(f"Error executing file {file_path}: {e}")

def execute_package(package_path):
    """Execute all Python files in a package directory."""
    if not os.path.isdir(package_path):
        print(f"Error: '{package_path}' is not a valid package.")
        return

    for _, module_name, is_pkg in pkgutil.iter_modules([package_path]):
        if is_pkg:
            continue

        file_path = os.path.join(package_path, f"{module_name}.py")
        execute_file(file_path)

def main():
    parser = argparse.ArgumentParser(description="Execute Python files or packages dynamically.")
    parser.add_argument(
        '--file-path',
        type=str,
        help="The path to a single Python file to execute."
    )
    parser.add_argument(
        '--package-name',
        type=str,
        help="The path to a package directory containing multiple Python files to execute."
    )

    args = parser.parse_args()

    if args.file_path and args.package_name:
        print("Error: Provide either --file-path or --package-name, not both.")
    elif args.file_path:
        execute_file(args.file_path)
    elif args.package_name:
        execute_package(args.package_name)
    else:
        print("Error: either --file-path or --package-name must be provided.")

if __name__ == "__main__":
    main()
