from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name='test_for_jelle',
    version='0.1',
    description='Test Dataset Extension for Jelle',
    url='https://github.com/VeenDuco/test_for_jelle',
    author='Veen, D.',
    author_email='d.veen@uu.nl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systematic review',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    python_requires='~=3.6',
    install_requires=[
        'asreview>=1.0',
    ],

    entry_points={
        "asreview.datasets": [
            "example_dataset_local = asreviewcontrib.dataset_name.your_dataset:example_dataset_local", # noqa
            "example_dataset_remote = asreviewcontrib.dataset_name.your_dataset:example_dataset_remote", # noqa
            "example_dataset_group = asreviewcontrib.dataset_name.your_dataset:example_dataset_group" # noqa
        ]

    },

    project_urls={
        'Bug Reports': 'https://github.com/asreview/template-extension-new-dataset/issues',
        'Source': 'https://github.com/asreview/template-extension-new-dataset/',
    },
)
