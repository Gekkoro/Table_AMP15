[app]

title = TimeTableApp
package.name = timetableapp
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.0

# Kivy version to use
osx.python_version = 3.8.10
osx.kivy_version = 2.0.0
osx.sdks = 10.14

# List requirements here, separated by commas (e.g. requirements = python3,kivy)
requirements = python3,kivy,requests,beautifulsoup4

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
#requirements = python3,kivy,requests,beautifulsoup4

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 23.0.7599858

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (list) Application meta-data for the manifest
# android.meta_data =

# (list) Android additional libraries to copy into libs/armeabi
android.add_libs_armeabi = libs/android/*.a

# (list) Android additional libraries to copy into libs/armeabi-v7a
android.add_libs_armeabi_v7a = libs/android-v7/*.a

# (list) Android additional libraries to copy into libs/arm64-v8a
android.add_libs_arm64_v8a = libs/android-64/*.a

# (list) Android additional libraries to copy into libs/x86
android.add_libs_x86 = libs/android-x86/*.a

# (list) Android additional libraries to copy into libs/x86_64
android.add_libs_x86_64 = libs/android-64/*.a

# (list) Android additional Java classes to include
# android.add_jars = foo.jar,bar.jar

# (list) Android additional Java classes to include, separated by ';'
android.add_jars = foo.jar;bar.jar

# (list) Android shared libraries to add (will copy to libs/arm64-v8a, libs/armeabi-v7a, libs/x86, libs/x86_64)
android.add_libs = libs/android/*.so

# (str) Android app theme, default is "import your_style_theme"
android.theme = "@android:style/Theme.NoTitleBar.Fullscreen"

# Android entry point
android.entrypoint = org.example.TimeTableApp

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (bool) Turn on the small python3 and uncrustify
#android.need_sdl2_ttf = False
#android.need_pygame = False

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = False

# (str) iOS App bundle identifier
# ios.bundleid = org.test
# (str) iOS App app name
# ios.appname = TestApp
# (str) iOS App SDK
# ios.iossdk = 10.1
# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path = /opt/android-sdk-linux/ndk-bundle

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path = /opt/android-sdk-linux

# (str) python-for-android branch to use, defaults to master
# p4a.branch = master

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# arch = armeabi-v7a

# (int) SDL2_mixer precompile version (for sdl2_mixer only), should match the version in buildozer
# sdl2_mixer_version = ~2.0.0

# (int) SDL2 precompile version (for sdl2 only), should match the version in buildozer
# sdl2_version = ~2.0.14

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# requirements = python3,kivy

# (str) Package name
package.name = time_table_app

# (str) Android NDK version to use
android.ndk = 21.4.7075529

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path = /opt/android-sdk-linux/ndk-21.4.7075529

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path = /opt/android-sdk-linux

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (bool) Indicate whether the application should be fullscreen or not
# fullscreen = 0

# (string) splash background color (for example  "#000000" or "black")
# android.splash_color = #FFFF00

# (string) splash image
# android.splash_path = %(source.dir)s/data/splash.png

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process.
#buildozer android debug