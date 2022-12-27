import os

UserAgrees = input("WARNING! --> This program will create a temporary file named `template.html`. It is the template neccesary for this to work, make sure you have write permissions in the actual directory, otherwise it won't work. Also if there alredy is a file called template.html [IT WILL BE OVERWRITTEN]. If you understant this, please enter any key and press enter to continue, otherwise press N and enter. ==> ")
if UserAgrees == "n" or UserAgrees == "N":
	exit()

# Define the template HTML
template_html = """
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	$if(title)$
  	<title>$title$ - $input-filename$</title>
	$else$
	<title>$input-filename$</title>
	$endif$
	<script>
		$highlighting-js$
	</script>
	<style>
		$highlighting-css$
	</style>
	<style>
		html {
			line-height: 1.15;
			-webkit-text-size-adjust: 100%;
		}

		* {
			margin: 0;
			padding: 0;
			box-sizing: border-box
		}

		main {
			display: block
		}

		h1 {
			font-size: 2em
		}

		hr {
			box-sizing: content-box;
			height: 0;
			overflow: visible;
		}

		pre {
			font-family: monospace, monospace;
			font-size: 1em;
		}

		a {
			background-color: transparent
		}

		abbr[title] {
			border-bottom: none;
			text-decoration: underline;
			text-decoration: underline dotted;
		}

		b,
		strong {
			font-weight: bolder
		}

		code,
		kbd,
		samp {
			font-family: monospace, monospace;
			font-size: 1em;
		}

		small {
			font-size: 80%
		}

		sub,
		sup {
			font-size: 75%;
			line-height: 0;
			position: relative;
			vertical-align: baseline
		}

		sub {
			bottom: -.25em
		}

		sup {
			top: -.5em
		}

		img {
			border-style: none
		}

		button,
		input,
		optgroup,
		select,
		textarea {
			font-family: inherit;
			font-size: 100%;
			line-height: 1.15;
			margin: 0;
		}

		button,
		input {
			overflow: visible
		}

		button,
		select {
			text-transform: none
		}

		button,
		[type="button"],
		[type="reset"],
		[type="submit"] {
			-webkit-appearance: button
		}

		button::-moz-focus-inner,
		[type="button"]::-moz-focus-inner,
		[type="reset"]::-moz-focus-inner,
		[type="submit"]::-moz-focus-inner {
			border-style: none;
			padding: 0
		}

		button:-moz-focusring,
		[type="button"]:-moz-focusring,
		[type="reset"]:-moz-focusring,
		[type="submit"]:-moz-focusring {
			outline: 1px dotted ButtonText
		}

		fieldset {
			padding: .35em .75em .625em
		}

		legend {
			box-sizing: border-box;
			color: inherit;
			display: table;
			max-width: 100%;
			padding: 0;
			white-space: normal;
		}

		progress {
			vertical-align: baseline
		}

		textarea {
			overflow: auto
		}

		[type="checkbox"],
		[type="radio"] {
			box-sizing: border-box;
			padding: 0;
		}

		[type="number"]::-webkit-inner-spin-button,
		[type="number"]::-webkit-outer-spin-button {
			height: auto
		}

		[type="search"] {
			-webkit-appearance: textfield;
			outline-offset: -2px;
		}

		[type="search"]::-webkit-search-decoration {
			-webkit-appearance: none
		}

		::-webkit-file-upload-button {
			-webkit-appearance: button;
			font: inherit;
		}

		details {
			display: block
		}

		summary {
			display: list-item
		}

		template {
			display: none
		}

		[hidden] {
			display: none
		}

		body {
			height: fit-content
		}
	</style>
	<style>
		@font-face {
			font-family: 'JetBrains Mono Cdn Github';
			src: url(https://stefanolomo.github.io/markdown-styling/fonts/JetbrainsMono.ttf);
		}

		.markdown-body {
			padding: 45px;
		}

		@media (max-width: 767px) {
			.markdown-body {
				padding: 15px;
			}
		}

		.markdown-body> :first-child {
			margin-top: 0;
		}

		.markdown-body {
			min-width: 200px;
			max-width: 980px;
			margin: 0 auto;
			font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
			font-size: 16px;
			line-height: 1.3;
			color: #212121;
		}

		.markdown-body p {
			text-align: justify;
			word-spacing: -1.5px;
		}

		.markdown-body h1 {
			font-size: 2.2em;
		}

		.markdown-body h2 {
			font-size: 2em;
		}

		.markdown-body h3 {
			font-size: 1.8em;
		}

		.markdown-body h4 {
			font-size: 1.6em;
		}

		.markdown-body h5 {
			font-size: 1.4em;
		}

		.markdown-body h6 {
			font-size: 1.2em;
		}

		.markdown-body h1,
		.markdown-body h2,
		.markdown-body h3,
		.markdown-body h4,
		.markdown-body h5,
		.markdown-body h6 {
			font-weight: 600;
			color: #282828;
			line-height: 1.25;
			margin-bottom: 16px;
			margin-top: 24px;
		}

		.markdown-body pre {
			white-space: pre-wrap;
		}

		.markdown-body hr {
			border: 0;
			margin: 24px 0;
			background-color: #d7d8d9;
			height: 2px;
		}

		.markdown-body table {
			display: table;
			table-layout: fixed;
			width: 100%;
			border-collapse: collapse;
		}

		.markdown-body table tr {
			background-color: #fff;
			border-top: 1px solid #c6cbd1;
		}

		.markdown-body table th {
			font-weight: normal;
		}

		.markdown-body table td,
		.markdown-body table th {
			border: 1px solid #dfe2e5;
			padding: 6px 13px;
		}

		.markdown-body table tr:nth-child(2n) {
			background-color: #f6f8fa;
		}

		.markdown-body div.sourceCode {
			padding: 0.8rem;
			background-color: #fafbff;
			border: 1px solid #e5e5e5;
		}

		.markdown-body div.sourceCode pre.sourceCode {
			font-size: 0.9em;
		}

		.markdown-body div.sourceCode pre.sourceCode code.sourceCode {
			font-family: "JetBrains Mono", monospace;
		}

		.markdown-body p>span.math.display:only-child {
			text-align: center;
			display: block;
			font-size: 1.3em;
			font-family: Katex_main, 'Times New Roman';
		}

		.markdown-body blockquote {
			margin: 0 0.2rem 16px 0.2rem;
			border-left: #ccc solid 7.5px;
			background-color: #f1f1f1;
			padding: 0.8rem;
			border-radius: 7px;
		}

		.markdown-body blockquote p {
			margin-bottom: 10px;
		}

		.markdown-body blockquote p:last-of-type {
			margin-bottom: 0;
		}

		.markdown-body div.alert-default {
			background-color: #eeeeee;
			border: 2px solid gray;
			border-top: 5px solid gray;
			border-radius: 0 0 7px 7px;
			padding: 0.8rem;
			margin: 0 0.2rem 16px 0.2rem;
		}

		.markdown-body div.alert-default p {
			margin-bottom: 10px;
		}

		.markdown-body div.alert-default p:last-of-type {
			margin-bottom: 0;
		}

		.markdown-body div.alert-error {
			background-color: #eec6c6;
			border: 2px solid #e00505;
			border-top: 5px solid #e00505;
			border-radius: 0 0 7px 7px;
			padding: 0.8rem;
			margin: 0 0.2rem 16px 0.2rem;
		}

		.markdown-body div.alert-error p {
			margin-bottom: 10px;
		}

		.markdown-body div.alert-error p:last-of-type {
			margin-bottom: 0;
		}

		.markdown-body div.alert-warning {
			background-color: #ffe4c3;
			border: 2px solid #f88400;
			border-top: 5px solid #f88400;
			border-radius: 0 0 7px 7px;
			padding: 0.8rem;
			margin: 0 0.2rem 16px 0.2rem;
		}

		.markdown-body div.alert-warning p {
			margin-bottom: 10px;
		}

		.markdown-body div.alert-warning p:last-of-type {
			margin-bottom: 0;
		}

		.markdown-body div.alert-tip {
			background-color: #c4c3ff;
			border: 2px solid #376bb9;
			border-top: 5px solid #376bb9;
			border-radius: 0 0 7px 7px;
			padding: 0.8rem;
			margin: 0 0.2rem 16px 0.2rem;
		}

		.markdown-body div.alert-tip p {
			margin-bottom: 10px;
		}

		.markdown-body div.alert-tip p:last-of-type {
			margin-bottom: 0;
		}

		.markdown-body div.alert-success {
			background-color: #aaffb1;
			border: 2px solid #549e4d;
			border-top: 5px solid #549e4d;
			border-radius: 0 0 7px 7px;
			padding: 0.8rem;
			margin: 0 0.2rem 16px 0.2rem;
		}

		.markdown-body div.alert-success p {
			margin-bottom: 10px;
		}

		.markdown-body div.alert-success p:last-of-type {
			margin-bottom: 0;
		}

		.markdown-body section.footnotes.footnotes-end-of-document hr {
			width: 25%;
		}

		blockquote,
		dl,
		ol,
		p,
		pre,
		table,
		ul {
			margin: 0 0 16px 0;
		}
	</style>
</head>

<body>
	<section class="markdown-body">
		$body$
	</section>

</body>

</html>
"""

# Ask the user for the path to the Markdown file
markdown_path = input("Enter the path to the Markdown file: ")

# Ask the user for the title
title = input("Enter the title [If there is a space in the tittle, put it between quotes]: ")

# Ask the user for the name of the output HTML file
output_file = input("Enter the name of the output HTML file: ")

# Ask the user for the code highlighting style
highlight_style = input("Enter the code highlighting style (e.g. pygments, monochrome) [Leaving this blank selects pygments by default]: ")

# Use the pygments style if the user did not specify a style
if not highlight_style:
    highlight_style = "pygments"

# Write the template HTML to a temporary file
with open("template.html", "w") as f:
    f.write(template_html)

# Build the pandoc command
command = f"pandoc {markdown_path} --template=template.html --metadata title={title} --output={output_file} --highlight-style={highlight_style}"

# Run the pandoc command
os.system(command)

# Delete the temporary template file
os.remove("template.html")
