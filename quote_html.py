import sublime, sublime_plugin, re

class QuoteHtmlCommand(sublime_plugin.TextCommand):

	def run(self, edit, action='single'):
		view = self.view
		selection = view.sel()[0]

		if len(selection) > 0:
			regions = []
			for sel in view.sel():
				region = sublime.Region(
					view.line(min(sel.a, sel.b)).a,  # line start of first line
					view.line(max(sel.a, sel.b)).b   # line end of last line
				)
				code = view.substr(region)
				code = self.quote(code, action)
				view.replace(edit, region, code)

		else:
			region = sublime.Region(0, view.size())
			code = view.substr(region)
			code = self.quote(code, action)
			view.replace(edit, region, code)

	def quote(self, code, action):
		lines = code.split('\n')

		if re.search('-ar', action):
			indentation = '\t'
			connector = ','
		else:
			indentation = ''
			connector = ' +'

		if re.search('single', action):
			for i in range(len(lines)):
				lines[i] = re.sub(r'(?!\\)\'', r"\\'", lines[i])
				if re.search('-ws', action):
					lines[i] = re.sub(r'(\s*)(\S+(\s+\S+)*)\s*', indentation + r"'\1\2'" + connector, lines[i])
				else:
					lines[i] = re.sub(r'(\s*)(\S+(\s+\S+)*)\s*', indentation + r"\1'\2'" + connector, lines[i])
		elif re.search('double', action):
			for i in range(len(lines)):
				lines[i] = re.sub(r'(?!\\)"', r'\\"', lines[i])
				if re.search('-ws', action):
					lines[i] = re.sub(r'(\s*)(\S+(\s+\S+)*)\s*', indentation + r'"\1\2"' + connector, lines[i])
				else:
					lines[i] = re.sub(r'(\s*)(\S+(\s+\S+)*)\s*', indentation + r'\1"\2"' + connector, lines[i])

		code = '\n'.join(lines)

		if re.search('-ar', action):
			code = re.sub(r'^([\s\S]*),$', r'[\n\1\n].join("");', code)
		else:
			code = re.sub(r'(.*) \+$', r'\1;', code)

		return code