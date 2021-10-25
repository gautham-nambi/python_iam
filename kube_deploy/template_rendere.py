from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os

if __name__ == "__main__":
	values = yaml.load(open('variables.yaml'))
	env = Environment(loader = FileSystemLoader(os.getcwd()), trim_blocks = True, lstrip_blocks = True)
	temp = env.get_template(sys.argv[1])
	print(temp.render(values))
