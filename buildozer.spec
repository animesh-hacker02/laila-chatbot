[app]
# Title of your application
title = Laila Chatbot

# Package name (should be unique)
package.name = laila_chatbot

# Package domain (reverse of your website)
package.domain = org.animesh

# Source directory
source.dir = .

# Files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,ttf,json

# Application version
version = 1.0

# Requirements
requirements = python3,kivy,requests

# Main entry point
source.main = main.py

# Orientation
orientation = portrait

# Fullscreen or not
fullscreen = 0

# Presplash (loading screen)
presplash.filename = %(source.dir)s/presplash.png

# Icon
icon.filename = %(source.dir)s/icon.png

[buildozer]
# Log level (2 = info, 1 = warning, 0 = error)
log_level = 2

# Skip build if needed
# buildozer.skip_update = yes

[android]
# Android SDK path (auto-detected)
# android.sdk_path =

# Android NDK path (auto-detected)  
# android.ndk_path =

# API level
api = 33

# Minimum SDK version
minapi = 21

# Target SDK version  
targetapi = 33

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Features
android.features = android.hardware.touchscreen

# Accept licenses automatically
android.accept_sdk_license = true

# Architectures
android.arch = arm64-v8a, armeabi-v7a

[android:entrypoint]
# Main activity class
main_activity = org.animesh.laila_chatbot.MainActivity

[android:gradle]
# Gradle configuration
gradle.version = 7.5
gradle.plugins_version = 1.5.0

[ios]
# iOS settings (if needed later)
version = 1.0
requirements = kivy

[loggers]
# Logging configuration
root = kivy

[presets]
# Build presets
debug = debug
release = release