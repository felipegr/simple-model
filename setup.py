from setuptools import setup, find_packages

setup(
    name='pysimplemodel',
    version='0.15.0',
    description='Simple Models for Python',
    url='https://github.com/lamenezes/simple-model',
    author='Luiz Menezes',
    author_email='luiz.menezesf@gmail.com',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests*']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
)
