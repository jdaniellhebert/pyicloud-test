# https://github.com/picklepete/pyicloud/blob/master/CODE_SAMPLES.md

import os
import click
import time
import datetime
from pyicloud import PyiCloudService


print("Setup Time Zone")
time.strftime("%X %x %Z")
os.environ["TZ"] = "America/New_York"


print("Py iCloud Services")
userid = input("iCloud UserID: ")
userpwd = input("iCloud Pwd: ")
api = PyiCloudService(userid, userpwd)

print(api)

time.sleep(3)

if api.requires_2sa:
    print("Two-factor authentication required. Your trusted devices are:")

    devices = api.trusted_devices
    for i, device in enumerate(devices):
        print(
            "  %s: %s"
            % (i, device.get("deviceName", "SMS to %s" % device.get("phoneNumber")))
        )

    device = click.prompt("Which device would you like to use?", default=0)
    device = devices[device]
    if not api.send_verification_code(device):
        print("Failed to send verification code")
        sys.exit(1)

    code = click.prompt("Please enter validation code")
    if not api.validate_verification_code(device, code):
        print("Failed to verify verification code")
        sys.exit(1)

#
# Devices
#
print("Devices")
print(api.devices)
print(api.devices[0])
print(api.iphone)


#
# Location
#
print("Location")
print(api.iphone.location())


#
# Status
#
print("Status")
print(api.iphone.status())

#
# Play Sound
#
# api.iphone.play_sound()


#
# Events
#
print("Events")
print(api.calendar.events())
from_dt = datetime.date(2018, 1, 1)
to_dt = datetime.date(2018, 1, 31)
print(api.calendar.events(from_dt, to_dt))


# ========
# Contacts
# ========
print("Contacts")
for c in api.contacts.all():
    print(c.get("firstName"), c.get("phones"))


# =======================
# File Storage (Ubiquity)
# =======================

# You can access documents stored in your iCloud account by using the
# ``files`` property's ``dir`` method:
print("File Storage")
print(api.files.dir())

#some more changes to test github
