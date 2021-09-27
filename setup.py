from setuptools import setup

setup(
    name='AWS_IAM',
    packages=['AWS_IAM'],
    include_package_data=True,
    install_requires=[
        'flask',
        'broto3',
        'awscli',
    ],
)
