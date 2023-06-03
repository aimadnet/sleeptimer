from setuptools import setup, find_packages

setup(
    name='sleeptimer',
    version='1.0.0',
    description='A sleep timer package with live timer and progress bar',
    author='Aimadnet',
    author_email='contact@aimadnet.com',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'termios',
    ],
)
