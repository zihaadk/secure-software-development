#!bin/env python3
# Author(s): cryptopal85
# Version history: April 09 2022 - Initialising main structure
#                                = Setting default group ID creation
#
# Remarks: Assuming this CLI-based tool will be used for administrating users
# alongside with 'usermanagementutil.py'.

from werkzeug.security import generate_password_hash
import getpass
import usermanagementutil


