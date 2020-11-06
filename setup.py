import setuptools
import os

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
README = os.path.join(CUR_DIR, "README.md")
with open("README.md", "r") as fd:
    long_description = fd.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setuptools.setup(
    name="troopclient",
    version="0.1.3",
    description="Troop Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/troopstack/troopclient",
    author="KurolZ",
    author_email="kurolz@163.com",
    packages=["client"],
    install_requires=[
        "requests>=2.23.0",
        "colorama>=0.4.1"
    ],
    entry_points={
        'console_scripts': [
            'troopclient=troopclient:main'
        ],
    },
    classifiers=(
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Programming Language :: Python",
    ),
    keywords='ssh linux',
)
