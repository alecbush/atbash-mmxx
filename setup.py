from setuptools import setup

setup(
    name='atbashmmxx',
    version='0.1.0',
    packages=['atbashmmxx'],
    include_package_data=True,
    license='MIT License',
    description='Atbash MMXX.',
    author='Alec Bush',
    author_email='alexander.joseph.bush@gmail.com',
    entry_points={
        'console_scripts': [
            'atbashmmxx=atbashmmxx.__main__:run_cli',
        ],
    },
    install_requires=[
    ],
    tests_require=[
    ],
    classifiers=[
        'Intended Audience :: Science/Research'
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Security :: Cryptography'
    ],
    keywords='python modded modified atbash rotation key cipher cli',
)
