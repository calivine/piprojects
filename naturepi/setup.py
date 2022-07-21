from setuptools import setup


setup(
    name='naturepi',
    version='0.1',
    description='raspberry pi nature cam',
    install_requires=['picamera', 'gpiozero'],
    entry_points={
        'console_scripts': ['naturepi=naturepi.cli:main'],
    }
)
