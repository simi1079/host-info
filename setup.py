from setuptools import setup
setup(
    name = 'hostinfo',
    version = '0.0.1',
    packages = ['hostinfo'],
    entry_points = {
        'console_scripts': [
            'hostinfo = hostinfo.__main__:main'
        ]
    })
