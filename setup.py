from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path, name as os_name, listdir
from shutil import copy2
from sys import exit as sys_exit
import re

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def read(*parts):
    with open(path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def get_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r'Version\s(.*)',
                              version_file, re.M)
    if version_match:
        return version_match.group(1)


def copy_files():
    # Try to build the paths depending on OS
    home = path.expanduser("~")
    if os_name == "posix":
        user_dir = "Library/Application Support"
        executable = "Autodesk Fusion 360.app"
        extra = "Autodesk Fusion 360.app/Contents"
    elif os_name == "nt":
        user_dir = "AppData/Local"
        executable = "Fusion360.exe"
        extra = ""
    else:
        sys_exit(-1)
        return

    executable_path = path.realpath(path.join(home, user_dir, "Autodesk", "webdeploy", "production", executable))
    parent = path.dirname(executable_path)
    packages_location = path.join(parent, extra, "APi", "Python", "packages", "adsk")
    api_location = path.join(packages_location, "defs", "adsk")

    # Copy the files to our local directory
    for x in listdir(api_location):
        copy2(path.join(api_location, x), path.join(here, "adsk"))

    # Get the version from adsk files (hopefully it is the correct version string)
    # and add it to our package.
    version_from = path.join(packages_location, "core.py")
    with open(path.join(here, "adsk", "__init__.py"), "w") as fp:
        st = '__version__ = "{}"\n'.format(get_version(version_from))
        fp.write(st)


copy_files()

setup(
    name='adsk',
    version=find_version("adsk/__init__.py"),
    description='Stub implementation of Fusion 360 adsk',
    long_description=long_description,
    url='https://www.autodesk.com/products/fusion-360',
    author='Mattias.Hedberg',
    author_email='hedberg.a.mattias@gmail.com',
    python_requires='>=3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
    ],

    keywords='fusion 360 stub',
    packages=["adsk"]

)
