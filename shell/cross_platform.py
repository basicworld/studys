#!/usr/bin/python
import platform

profile=[
platform.architecture(),
platform.dist(),
platform.libc_ver(),
platform.mac_ver(),
platform.machine(),
platform.node(),
platform.platform(),
platform.version(),
platform.uname(),

]
for item in profile:
    print item
