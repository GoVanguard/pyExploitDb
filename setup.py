import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyExploitDb",
    version="0.2.5",
    author="Shane William Scott",
    author_email="sscott@govanguard.com",
    description="An optimized Python3 library to fetch the most recent exploit-database, create searchable indexes for CVE->EDBID and EDBID -> CVE, and provide methods to perform searches.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GoVanguard/pyExploitDb",
    packages=['pyExploitDb'],
    package_data={'pyExploitDb': ['cveToEdbid.json', 'edbidToCve.json', 'pyExploitDb/*.json']},
    install_requires=['GitPython', 'requests'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ),
)
