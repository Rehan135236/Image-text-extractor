[app]
title = Text Extractor
package.name = textextractor
package.domain = org.textextractor

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,pillow,pyjnius,android

orientation = portrait
fullscreen = 0

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
