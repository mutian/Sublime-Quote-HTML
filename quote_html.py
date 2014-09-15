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

		if action == 'single':
			for i in range(len(lines)):
				lines[i] = re.sub(r'(?!\\)\'', r"\\'", lines[i])
				lines[i] = re.sub(r'(\s*)(\S+(\s+\S+)*)\s*', r"\1'\2' +", lines[i])

		elif action == 'double':
			for i in range(len(lines)):
				lines[i] = re.sub(r'(?!\\)"', r'\\"', lines[i])
				lines[i] = re.sub(r'(\s*)(\S+(\s+\S+)*)\s*', r'\1"\2" +', lines[i])

		elif action == 'single-ws':
			for i in range(len(lines)):
				lines[i] = re.sub(r'(?!\\)\'', r"\\'", lines[i])
				lines[i] = re.sub(r'(\s*)(\S+(\s+\S+)*)\s*', r"'\1\2' +", lines[i])

		elif action == 'double-ws':
			for i in range(len(lines)):
				lines[i] = re.sub(r'(?!\\)"', r'\\"', lines[i])
				lines[i] = re.sub(r'(\s*)(\S+(\s+\S+)*)\s*', r'"\1\2" +', lines[i])

		code = '\n'.join(lines)
		code = re.sub(r'(\s\S)*? \+$', r"\1;", code)

		return code