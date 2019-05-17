#! /usr/bin/env python3

import os
from setuptools import setup


def get_long_description(file_name: str) -> str:
    """Gets the long description from the specified file's name.

    :param file_name: The file's name
    :type file_name: str
    :return: The content of the file
    :rtype: str
    """
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


if __name__ == '__main__':
    setup(
        name='cmus-notify',
        version='1.4.0',
        description='A package for displaying Cmus current status in notifications',
        author='Antoine Gagne',
        keywords='utilities application cli hook cmus notifications',
        author_email='antoine.gagne.2@ulaval.ca',
        url='https://github.com/AntoineGagne/cmus-notify',
        packages=['cmus_notify'],
        entry_points={
            'console_scripts': ['cmus_notify = cmus_notify.cmus_notify:main']
        },
        license='MIT',
        data_files=[],
        include_package_data=True,
        long_description=get_long_description('README.rst'),
        setup_requires=['pytest-runner', 'flake8'],
        tests_require=['pytest'],
        test_suite='tests',
        scripts=[],
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Development Status :: 5 - Production/Stable',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.5',
            'Topic :: Multimedia :: Sound/Audio'
        ],
        install_requires=['notify2>=0.3']
    )
