import re

pattern = "[]$()*+?.\^{}|"
escaped_pattern = re.escape(pattern)

print("Pattern:", pattern)
print("Escaped pattern:", escaped_pattern)
