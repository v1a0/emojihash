from setuptools import setup
from os import path
import emojihash

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='emojihash',
    packages=[
        'emojihash',
        'emojihash.classes',

    ],
    version=emojihash.__version__,
    license='gpl-3.0',
    description='Emoji hash functions',
    author='v1a0',
    author_email='contact@v1a0.dev',
    url="https://github.com/v1a0/sqllex",
    download_url=f"https://github.com/V1A0/emojihash/archive/refs/tags/v{emojihash.__version__}.tar.gz",
    keywords=['emoji', 'crypto', 'security', 'cryptography', 'hash', 'sha', 'sha512', 'sha256', 'md5', 'fun'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.9',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
# https://pypi.org/classifiers/
