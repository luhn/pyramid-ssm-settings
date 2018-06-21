from setuptools import setup


REQUIRES = ['boto3']


setup(
    name='pyramid-ssm-settings',
    version='0.1.0',
    description='Pull settings into Pyramid from Amazon EC2 Parameter Store.',
    long_description=open('README.rst').read(),
    license='MIT',
    author='Theron Luhn',
    author_email='theron@luhn.com',
    url='https://github.com/luhn/pyramid-ssm-settings',
    py_modules=['pyramid_ssm_settings'],
    install_requires=REQUIRES,
)
