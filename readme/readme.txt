Linter for CudaLint.
Supports JavaScript lexer, and ReactJS ("JavaScript Babel" lexer).

Requires Node.js.
Uses ESLint, ie "eslint" standalone program, so "eslint" must run from the command line.
Why it doesn't use Node package in a local folder? To share the single "eslint" program
with the CudaFormatter's formatter, which will also run "eslint".

For example, to install ESLint on Ubuntu, one has to run:
$ sudo apt install eslint


Config file
-----------
ESLint needs config file, otherwise it shows single error "No ESLint configuration found".
This file is ".eslintrc" or ".eslintrc.js".
To create this config, in the folder of your JS project, run this command:
$ npm init @eslint/config

This command asks questions in console, and then it creates ESLint config file.
With this config, linter should work and show real errors.
This was tested on Ubuntu.


Ported from SublimeLinter-eslint by Alexey Torgashin
License: MIT
