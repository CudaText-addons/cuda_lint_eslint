Linter for CudaLint.
Supports JavaScript lexer, and ReactJS - it's "JavaScript Babel" lexer.

Uses ESLint, it's not included here.
Requires Node.js. (For Windows "node.exe" must be in path, for Linux/OSX "nodejs" must be installed.)

You need to install ESLint globally (one install for all projects):
  npm install -g eslint
Or locally in folder of checked files:
  npm install eslint

ESLint needs config file, else it shows one error "No ESLint configuration found". This file is ".eslintrc" or ".eslintrc.js", you must create it (in dir with checked files). In termilal/console run this command:

for global ESLint ("eslint" must be in path):
  eslint --init
for local ESLint:
  nodejs ./node_modules/eslint/bin/eslint.js --init

In the case "local" it's executable of Node + relative path to eslint.js. This command asks questions in console, and then it creates ESLint config file. With this config, linter should work and show real errors. ESLint needs "package.json" file for Node too, it will show this and how to create it. So you usually
a) run "npm init" to create "package.json"
b) run "....eslint.js --init" to create ESLint config
This was tested on Ubuntu.


Ported from SublimeLinter-eslint by Alexey T.
