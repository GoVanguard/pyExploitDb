import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyExploitDb",
    version="0.2.28",
    author="Shane William Scott",
    author_email="sscott@gotham-security.com",
    description="An optimized Python3 library to fetch the most recent exploit-database, create searchable indexes for CVE->EDBID and EDBID -> CVE, and provide methods to perform searches.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GoVanguard/pyExploitDb",
    packages=['pyExploitDb'],
    package_data={'pyExploitDb': ['cveToEdbid.json', 'edbidToCve.json', 'pyExploitDb/*.json']},
    install_requires=['GitPython', 'requests'],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ),
)
