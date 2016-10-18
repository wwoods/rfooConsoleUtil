from distutils.core import setup
from distutils.extension import Extension
import sys, os

try:
    from Cython.Distutils import build_ext
except ImportError:
    sys.stderr.write("""=============
rfoo (and thus rfooConsoleUtil) depends on Cython - http://cython.org.

Can be installed via pip.
""")
    sys.exit(1)

if __name__ == '__main__':
    version = '0.1'
    setup(
        name = 'rfooConsoleUtil',
        version = version,
        install_requires=[
            "cython>=0.24.0",
            "six>=1.10.0",
        ],
        description = "Helper tools for rfoo.utils.rconsole",
        classifiers = [],
        author = "Walt Woods",
        url = "https://github.com/wwoods/rfooConsoleUtil",
        license = "MIT",
        packages = ['rfoo', 'rfoo.utils', 'rfooConsoleUtil'],
        package_dir = {'rfoo': 'rfoo/rfoo', 'rfoo.utils': 'rfoo/rfoo/utils'},
        scripts = ['rfoo/scripts/rconsole'],
        cmdclass = {'build_ext': build_ext},
        ext_modules = [Extension("rfoo.marsh", ["rfoo/rfoo/marsh.pyx"])],
    )
