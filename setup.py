from setuptools import setup, find_packages

setup(
    name='OmniHubAI',
    version='0.1.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your dependencies here, e.g.,
        'numpy',
        'pandas',
        'torch',  # or other required libraries
    ],
    author='Lokesh Yarramallu',
    description='A comprehensive AI library.',
    license='MIT',
    keywords='AI GENAI',
    url='https://github.com/ACM-Amrita-Amritapuri/OmniHubAI',
)
