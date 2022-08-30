from setuptools import setup

setup(
    name='YamlChecker',
    version='0.1.0',
    packages=['yaml_checker'],
    license='GNU GPLv3',
    author='Joshua Laughner',
    author_email='jllacct119@gmail.com',
    description='A command line utility to check YAML files',
    install_requires=['PyYAML>=6.0'],
    entry_points={'console_scripts': ['yaml-checker=yaml_checker.__main__:main']}
)
