from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

long_description = 'Dev Helper is a CLI utility \
	to help you find answers faster.'

setup(
    name='dev-helper',
    version='1.0.0',
    author='Luis Moreno',
    author_email='luis.cfh.90@gmail.com',
    url='https://github.com/luigicfh/dev-helper',
    description='Dev Helper helps you find answers from your command line',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dh = command_line.parser:main'
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords='stack overflow search CLI',
    install_requires=requirements,
    zip_safe=False
)
