# -*- coding: utf-8 -*-

name = "make"

version = "4.3.0"

authors = [
    "GNU",
    "javrin"
]

description = \
    """
    Make is a tool which controls the generation of executables and other non-source files
    of a program from the program's source files.
    """

help = "http://www.gnu.org/software/make"

tools: ["make"]

variants = [
    ["os-Windows-10"]
]

private_build_requires = []

with scope('config') as config:
    config.release_packages_path = '${SYSTEM_REZ_EXTERNAL_PACKAGES}'


def pre_build_commands():
    import os

    source_archive = '{}-{}.{}-without-guile-w32-bin.zip'.format(
        this.name,
        this.version.major,
        this.version.minor
    )

    env.REZ_BUILD_SOURCE_ARCHIVE = os.path.join(
        "${REZ_BUILD_SOURCE_PATH}",
        "rel",
        source_archive
    ).replace("\\", "/")


build_command = """ \
unzip -o $REZ_BUILD_SOURCE_ARCHIVE -d $REZ_BUILD_PATH

if [ $REZ_BUILD_INSTALL == 1 ]
then
    echo -e "\e[1m\e[32mInstalling...\e[0m"
    for item in $REZ_BUILD_PATH/*
    do
        if [ -d "$item" ]
        then
            cp -rv $item $REZ_BUILD_INSTALL_PATH
        fi
    done
else
    echo -e "\e[1m\e[33mNothing more to do. Run ""rez-build -i"" to install\e[0m"
fi
"""


def commands():
    import os

    env.PATH.prepend(os.path.join("{root}", "bin").replace("\\", "/"))
