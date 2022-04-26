from setuptools                         import setup, find_packages


setup(
    name='realmz',
    version='0.0.10',
    license='MIT',
    author='Billy Katalayi',
    author_email='billysbn7@gmail.com',
    packages=find_packages('src'),
    package_dir={'' : 'src'},
    url='https://github.com/Billykat7/wishes',
    keywords='employees birthday, anniversary automated wishes',
    # classifiers=[
    #     "License :: OSI Approved :: MIT License",
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.9",
    # ],
    install_requires=[
        # 'celery',
        'python-dotenv',
        # 'redis',
        'requests',
        'SQLAlchemy'
    ],
    # entry_points={
    #     "console_scripts": [
    #         "realmz.__main__:main",
    #     ]
    # },
    # include_package_data=True,
)
