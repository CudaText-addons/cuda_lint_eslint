# Written by roadhump
# Copyright (c) 2014 roadhump
# License: MIT
# Change for CudaLint: Alexey T.

import os
import re
from cuda_lint import Linter, util
from cudax_nodejs import NODE_FILE

IS_WIN = os.name=='nt'

if not IS_WIN:
    import cudatext as app
    _js = os.path.join(os.path.expanduser('~'), 'node_modules', 'eslint', 'bin', 'eslint.js')
    if not os.path.exists(_js):
        app.msg_box('ESLint linter cannot find file:\n'+_js, app.MB_OK+app.MB_ICONERROR)


class ESLint(Linter):
    """Provides an interface to the eslint executable."""

    syntax = ('JavaScript', 'JavaScript Babel')
    if IS_WIN:
        cmd = ('eslint', '--format', 'compact', '--stdin', '--stdin-filename', '@')
    else:
        cmd = (NODE_FILE, _js, '--format', 'compact', '--stdin', '--stdin-filename', '@')
    
    regex = (
        r'^.+?: line (?P<line>\d+), col (?P<col>\d+), '
        r'(?:(?P<error>Error)|(?P<warning>Warning)) - '
        r'(?P<message>.+)'
    )
    config_fail_regex = re.compile(r'^Cannot read config file: .*\r?\n')
    crash_regex = re.compile(
        r'^(.*?)\r?\n\w*Error: \1',
        re.MULTILINE
    )
    line_col_base = (0, 0)


    def find_errors(self, output):
        """
        Parse errors from linter's output.

        We override this method to handle parsing eslint crashes.
        """

        match = self.config_fail_regex.match(output)
        if match:
            return [(match, 0, None, "Error", "", match.group(0), None)]

        match = self.crash_regex.match(output)
        if match:
            msg = "ESLint crashed: %s" % match.group(1)
            return [(match, 0, None, "Error", "", msg, None)]

        return super().find_errors(output)


    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method to silent warning by .eslintignore settings.
        """

        v1message = 'File ignored because of your .eslintignore file. Use --no-ignore to override.'
        v2message = 'File ignored because of a matching ignore pattern. Use --no-ignore to override.'

        match, line, col, error, warning, message, near = super().split_match(match)
        if message and (message == v1message or message == v2message):
            return match, None, None, None, None, '', None

        return match, line, col, error, warning, message, near

