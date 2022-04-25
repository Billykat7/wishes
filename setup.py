from setuptools                         import setup, find_packages


setup(
    name='realmz',
    version='0.0.8',
    license='MIT',
    author='Billy Katalayi',
    author_email='billysbn7@gmail.com',
    packages=find_packages('src'),
    package_dir={'' : 'src'},
    url='https://github.com/Billykat7/wishes',
    keywords='employees birthday, anniversary automated wishes',
    install_requires=[
        # 'celery',
        # 'redis',
        'requests',
        'SQLAlchemy'
    ],
    # include_package_data=True,
)
