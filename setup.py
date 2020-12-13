from setuptools import setup, find_packages

setup(
    name="define",
    version='1.1',
    description='Define system',
    author="Pavel Oborin",
    author_email="pavel@oborin.xyz",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "define=define.cli:main"
        ]
    },
    package_data={'': ['data/*.csv']}
)
