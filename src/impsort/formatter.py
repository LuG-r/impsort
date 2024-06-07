import ast


class Formatter:
    def __init__(self) -> None:
        pass

    def format_file(self, path_to_file: str, check_semantic: bool = False):
        if path_to_file[-3:] != ".py":
            raise ValueError("The file provided does not appear to be a Python file")
        if check_semantic:
            with open(path_to_file, "r") as f:
                code_tree = ast.parse(f.read())
                self.ast_start = compile(code_tree, filename="<ast>", mode="exec")
        self.organise_packages(self.get_package_info(path_to_file))
        if check_semantic:
            with open(path_to_file, "r") as f:
                code_tree = ast.parse(f.read())
                self.ast_end = compile(code_tree, filename="<ast>", mode="exec")
            print(self.ast_start == self.ast_end)

    def get_package_info(self, file_path: str) -> object:
        packages = {"import": [], "from": [], "import_lines": [], "lines": []}
        line_number = 1
        with open(file_path, "r") as f:
            for line in f:
                line_contents = line.split(" ")
                if line_contents[0] == "import":
                    packages["import"].append(
                        {"package_name": line_contents[1], "line": line}
                    )
                    packages["import_lines"].append(line_number)
                elif line_contents[0] == "from":
                    packages["from"].append(
                        {"package_name": line_contents[1], "line": line}
                    )
                    packages["import_lines"].append(line_number)
                else:
                    packages["lines"].append(line)
                line_number += 1
        packages["import"].sort(key=lambda x: x["package_name"])
        packages["from"].sort(key=lambda x: x["package_name"])
        packages["import"].extend(packages["from"])

        return {
            "file_path": file_path,
            "packages": packages["import"],
            "line_numbers": packages["import_lines"],
            "lines": packages["lines"],
        }

    def organise_packages(self, packages: object) -> None:
        base_content_position = 0
        current_line_number = 1
        with open(packages["file_path"], "w") as f:
            for index, target_line_number in enumerate(packages["line_numbers"]):
                while current_line_number != target_line_number:
                    f.write(packages["lines"][base_content_position])
                    base_content_position += 1
                    current_line_number += 1
                f.write(packages["packages"][index]["line"])
                current_line_number += 1
            if base_content_position < len(packages["lines"]):
                f.writelines(packages["lines"][base_content_position:])
