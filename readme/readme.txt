Linter for CudaLint.
Supports JavaScript lexer, and ReactJS ("JavaScript Babel" lexer).

Requires Node.js.
Uses ESLint, you need to install ESLint locally in the linter's folder
"(CudaText)/py/cuda_lint_eslint":
$ npm install eslint


Config file
-----------

ESLint needs config file, otherwise it shows single error "No ESLint configuration found".
This file is ".eslintrc" or ".eslintrc.js", you must create it (in the folder with checked files).
In the linter's folder run this command:
$ npm init @eslint/config
or
$ node ./node_modules/eslint/bin/eslint.js --init

This command asks questions in console, and then it creates ESLint config file.
With this config, linter should work and show real errors.
This was tested on Ubuntu.

  user@PC:~/.config/cudatext/py/cuda_lint_eslint$ npm init @eslint/config
  ...
  Local ESLint installation not found.
  ...
  Successfully created .eslintrc.js file in /home/user/.config/cudatext/py/cuda_lint_eslint


Ported from SublimeLinter-eslint by Alexey Torgashin
License: MIT
