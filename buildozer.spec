# Buildozer spec file for My Application

[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts =

# (list) List of directories to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, venv

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pillow,kivymd,requests,datetime

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (str) Presplash image of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (str) Application versioning (method 1)
version = 0.1

# (list) List of services to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

# (str) Python version to use (by default, it's 3.9 for macOS)
osx.python_version = 3

# (str) Kivy version to use
osx.kivy_version = 2.1.0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions for Android (adjust for your app needs)
android.permissions = android.permission.INTERNET,WRITE_EXTERNAL_STORAGE

# (list) Android features (add tags to the manifest)
# android.features = android.hardware.usb.host

# (int) Target Android API level (must be as high as possible for latest features)
android.api = 31

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (str) Android SDK directory (automatically downloaded if empty)
# android.sdk_path =

# (str) Android NDK directory (automatically downloaded if empty)
# android.ndk_path =

# (str) Android entry point (default is fine for Kivy-based app)
android.entrypoint = org.kivy.android.PythonActivity

# (list) Android architectures to build for (adjust as per target devices)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable auto backup feature for Android (only for API >= 23)
android.allow_backup = True

# (str) Format for APK or AAB packaging (choose "apk" for APK, "aab" for Android App Bundle)
android.release_artifact = aab

# (bool) Skip byte compile for .py files (set to True for faster builds)
# android.no-byte-compile-python = True

#
# iOS specific
#

# (str) Kivy-iOS directory (automatically cloned if empty)
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# (bool) Whether or not to sign the code for iOS
ios.codesign.allowed = false

# (str) Name of the certificate to use for signing the debug version
# ios.codesign.debug = "iPhone Developer: <name> (<hexstring>)"

# (str) The development team to use for signing the debug version
# ios.codesign.development_team.debug = <hexstring>

# (bool) iOS deployment flag (True if using custom iOS deploy)
# ios.deploy = False

# (str) Application version (same as in the app section for consistency)
ios.version = 0.1

# (str) Full name including package path for Java activity in case of custom setups
# android.activity_class_name = org.kivy.android.PythonActivity

# (str) Screen orientation for iOS, can be 'portrait' or 'landscape'
ios.orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# (int) Warn on root execution (default: True)
warn_on_root = 1

# (str) Path to build artifact storage
build_dir = ./.buildozer

# (str) Path to build output storage for APK, AAB, or IPA
bin_dir = ./bin

# (list) Include any extra dependencies (if needed for your app)
# buildozer.extra_requirements =

#
# Profiles for different environments (for testing and release setups)

[app@demo]
title = My Application (Demo)

[app@release]
# title = My Application (Release)
# Optional for Release: Include any additional configurations needed for the production environment
# e.g., stricter exclusions, performance optimization flags, etc.
# source.exclude_patterns = .git, .github
