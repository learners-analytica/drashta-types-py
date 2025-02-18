from setuptools import setup, find_packages

setup(
    name='drashta_types_py',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=open('requirements.txt').read().splitlines(),
    include_package_data=True,
)
