from setuptools import setup

requirements = [
    # TODO: put your package requirements here
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-faulthandler',
    'pytest-mock',
    'pytest-qt',
    'pytest-xvfb',
]

setup(
    name='pyente',
    version='0.0.1',
    description="Ente that interacts with pywaschedv",
    author="TvK Wasch-AG",
    author_email='wag@tvk.rwth-aachen.de',
    url='https://github.com/waschag-tvk/pyente',
    packages=['pyente', 'pyente.images',
              'pyente.tests'],
    package_data={'pyente.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'Ente=pyente.app:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='pyente',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
