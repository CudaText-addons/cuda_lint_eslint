Linter for CudaLint.
Supports JavaScript lexer, and ReactJS ("JavaScript Babel" lexer).

Requires Node.js.
Uses ESLint package for Node.js.

Installation: *nix OS
---------------------
It uses ESLint installed for the home dir: ~/node_modules/eslint/bin/eslint.js
So you must install ESLint using NPM from the home dir.

Ensure that 'compact ESLint' is installed too. To test it, run in Terminal with some file "test.js":
$ node ~/node_modules/eslint/bin/eslint.js --format compact test.js 

If you see such error:
  "The compact formatter is no longer part of core ESLint. Install it manually with `npm install -D eslint-formatter-compact`""
Then run the suggested command:
$ npm install -D eslint-formatter-compact


Installation: Windows OS
------------------------
You need 'eslint' program installed and be in the system PATH.


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
