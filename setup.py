from setuptools import setup

import os, re

os.environ['COPYFILE_DISABLE'] = 'true'  # this disables including resource forks in tar files on os x


def long_description():
    with open('README.md') as readme, open('CHANGELOG.txt') as changelog:
        return readme.read() + '\n' + changelog.read()


def version():
    with open('js_min/__init__.py') as f:
        return re.search(r'__version__ = ["\']([^"\']+)', f.read()).group(1)


setup(
    name="min-js",
    version=version(),
    packages=['js_min'],
    description='JavaScript minifier.',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    author='Dave St.Germain',
    author_email='dave@st.germa.in',
    maintainer='Tikitu de Jager',
    maintainer_email='tikitu+jsmin@logophile.org',
    test_suite='js_min.test',
    license='MIT License',
    url='https://github.com/QQSHI13/js-min/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Text Processing :: Filters',
    ]
)
