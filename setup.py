from setuptools import setup, find_packages

setup(
    name='Gengo Amazon SNS Publisher',
    version='0.1',
    description='',
    author='Gengo Dev',
    author_email='dev@gengo.com',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'flask',
        'marshmallow',
        'python-dotenv',
        'webargs',
    ]
)
