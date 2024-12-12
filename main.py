import re
import xml.etree.ElementTree as ET

class ConfigParser:
    def __init__(self):
        self.constants = {}

    def remove_comments(self, text):
        # Remove single-line comments
        text = re.sub(r"::.*", "", text)
        # Remove multi-line comments
        text = re.sub(r"\{-.*?-\}", "", text, flags=re.DOTALL)
        return text

    def parse_value(self, value):
        value = value.strip()
        if value.startswith("list(") and value.endswith(")"):
            return self.parse_list(value)
        elif value.startswith("table([") and value.endswith(")"):
            return self.parse_table(value)
        elif value.isdigit():
            return int(value)
        elif self.is_float(value):
            return float(value)
        elif (value.startswith("\"") and value.endswith("\"")) or (value.startswith("'") and value.endswith("'")):
            return value[1:-1]
        elif value in self.constants:
            return self.constants[value]
        else:
            raise ValueError(f"Invalid value: {value}")

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def parse_list(self, value):
        content = value[5:-1].strip()
        return [self.parse_value(v.strip()) for v in self.split_arguments(content)]

    def parse_table(self, value):
        content = value[7:-2].strip()
        table = {}
        for entry in self.split_arguments(content):
            key, val = entry.split("=", 1)
            table[key.strip()] = self.parse_value(val.strip())
        return table

    def split_arguments(self, content):
        brackets = 0
        current = []
        result = []

        for char in content:
            if char in "([{":
                brackets += 1
            elif char in ")]}":
                brackets -= 1
            elif char == "," and brackets == 0:
                result.append("".join(current).strip())
                current = []
                continue

            current.append(char)

        if current:
            result.append("".join(current).strip())

        return result

    def parse_set(self, line):
        match = re.match(r"set\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+);", line)
        if not match:
            raise ValueError(f"Invalid set syntax: {line}")
        name, value = match.groups()
        self.constants[name] = self.parse_value(value)

    def parse(self, text):
        text = self.remove_comments(text)
        lines = text.splitlines()
        for line in lines:
            line = line.strip()
            if line.startswith("set"):
                self.parse_set(line)

    def evaluate_constant(self, expression):
        match = re.match(r"\|([a-zA-Z_][a-zA-Z0-9_]*)\|", expression)
        if not match:
            raise ValueError(f"Invalid constant evaluation syntax: {expression}")
        name = match.group(1)
        if name not in self.constants:
            raise ValueError(f"Constant not defined: {name}")
        return self.constants[name]

    def to_xml(self, output_file):
        root = ET.Element("config")
        for key, value in self.constants.items():
            self.add_to_xml(root, key, value)
        tree = ET.ElementTree(root)
        tree.write(output_file, encoding="utf-8", xml_declaration=True)

    def add_to_xml(self, parent, key, value):
        element = ET.SubElement(parent, key)
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                self.add_to_xml(element, sub_key, sub_value)
        elif isinstance(value, list):
            for item in value:
                self.add_to_xml(element, "item", item)
        else:
            element.text = str(value)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python config_parser.py <output_file>")
        sys.exit(1)

    output_file = sys.argv[1]

    parser = ConfigParser()
    input_text = sys.stdin.read()
    parser.parse(input_text)
    parser.to_xml(output_file)
    print(f"Configuration written to {output_file}")
