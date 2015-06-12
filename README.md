QuoteHTML for Sublime Text
==========================


Description
-----------

Quote HTML snippet as a string.

**Example:**

* Original HTML:

	```html
	<div class="demo">
		<ol>
			<li>3</li>
			<li><a href='#'>2</a></li>
			<li><a href="#">3</a></li>
		</ol>
	</div>
	```

* Quote HTML with Single Quotes:

	```js
	'<div class="demo">' +
		'<ol>' +
			'<li>3</li>' +
			'<li><a href=\'#\'>2</a></li>' +
			'<li><a href="#">3</a></li>' +
		'</ol>' +
	'</div>';
	```

* Quote HTML with Double Quotes:

	```js
	"<div class=\"demo\">" +
		"<ol>" +
			"<li>3</li>" +
			"<li><a href='#'>2</a></li>" +
			"<li><a href=\"#\">3</a></li>" +
		"</ol>" +
	"</div>";
	```

* Quote HTML with Single Quotes include Space:

	```js
	'<div class="demo">' +
	'    <ol>' +
	'        <li>3</li>' +
	'        <li><a href=\'#\'>2</a></li>' +
	'        <li><a href="#">3</a></li>' +
	'    </ol>' +
	'</div>';
	```

* Quote HTML with Double Quotes include Space:

	```js
	"<div class=\"demo\">" +
	"    <ol>" +
	"        <li>3</li>" +
	"        <li><a href='#'>2</a></li>" +
	"        <li><a href=\"#\">3</a></li>" +
	"    </ol>" +
	"</div>";
	```


Installation
------------

**OPTION 1 - with Package Control (recommended)**

The easiest way to install this package is through Package Control.

1. Install [Package Control](https://sublime.wbond.net/installation), follow instructions on the website.

2. Open command panel: `Ctrl+Shift+P` (Linux/Windows) or `Cmd+Shift+P` (OS X) and select **Package Control: Install Package**.

3. When packages list appears, type `QuoteHTML` and select it.


**OPTION 2 - with Git**

Clone the repository in your Sublime Text "Packages" directory:

```shell
git clone git://github.com/mutian/Sublime-Quote-HTML.git "QuoteHTML"
```

You can find your "Packages" inside the following directories:

* OS X:
    `~/Library/Application Support/Sublime Text 2/Packages/`

* Windows:
    `%APPDATA%/Sublime Text 2/Packages/`

* Linux:
    `~/.Sublime Text 2/Packages/`


**OPTION 3 - without Git**

Download the latest source zip from [Github](https://github.com/mutian/Sublime-Quote-HTML) and extract it into a new folder named `QuoteHTML` in your Sublime Text "Packages" folder.


Usage
-----

Select the code, or place cursor in the document, and execute commands in one of the following ways:

* Command Panel: Open command panel: `Ctrl+Shift+P` (Linux/Windows) or `Cmd+Shift+P` (OS X) and select **Quote HTML**.


Shortcuts
---------

By default QuoteHTML provides no keyboard shortcuts to avoid conflicts, but you can view the included `Example.sublime-keymaps` file to get an idea how to set up your own.


Author
------

Created by **Mutian** ([http://mutian.wang](http://mutian.wang/)).

For more info, you can send email to me: mutian(a)me.com!
