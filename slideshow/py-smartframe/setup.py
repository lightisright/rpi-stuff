import setuptools
from sphinx.setup_command import BuildDoc

from emv import name
from emv import __version__

pkg_name = name
pkg_version = __version__

requires_install = [
    "bottle=*",
    "configparser=*",
]

cmdclass = {
    'build_sphinx': BuildDoc,
}

setupargs = dict(
    name=pkg_name,
    version=pkg_version,
    description="Py-SmartFrame - RPi + Python based Photo Viewer",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="git@github.com:lightisright/rpi-stuff.git",
    packages=[pkg_name],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: private",
        "Operating System :: OS Independent",
    ),
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'source_dir': ('setup.py', 'docs/source'),
            'version': ('setup.py', pkg_version),
        }
    },
    install_requires=requires_install,
)

if __name__ == "__main__":
    setuptools.setup(**setupargs)
