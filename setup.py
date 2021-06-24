from setuptools import setup, find_packages

setup(
    name='py-allenite',
    version='0.1',
    description='Python wrapper for Allenite\'s API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Harsh Patil',
    author_email='ifung230@gmail.com',
    url='https://github.com/lamergameryt/py-allenite',
    download_url='https://github.com/lamergameryt/py-allenite',
    keywords=['python', 'allenite'],
    license='GNU General Public License v3 (GPLv3)',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=['requests'],
    packages=find_packages(),
    include_package_data=True,
)
