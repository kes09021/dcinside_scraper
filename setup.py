from setuptools import setup, find_packages

setup(
    name='dcinside_scraper',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'dcinside-scraper=dcinside_scraper.scraper:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package to scrape posts from DCInside',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/dcinside_scraper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
