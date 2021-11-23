from setuptools import setup, find_packages

short_description = "OpenShift Project Manager"

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except:
    long_description = short_description

setup(
    name="ospmasten",
    version="0.1.0",
    author="Guillaume BITON",
    author_email="guillaume.biton@groupe-asten.fr",
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astenmco/ospm",
    project_urls={
        "Bug Tracker": "https://github.com/astenmco/ospm/issues",
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        'Intended Audience :: System Administrators',
        'Environment :: Console',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Linux",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    package_data={'ospm': ['data/*']},
    python_requires=">=3.6",
    install_requires=[
        'Click',
        'click_log',
        'pyyaml',
        'jsonschema'
    ],
    entry_points={
        'console_scripts': [
#            'ospmsudo = cli:sudo'
            'ospm = cli:cli',
        ],
    },
)