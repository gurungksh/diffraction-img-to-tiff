from setuptools import setup, find_packages

setup(
    name='img-to-tiff-exe',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'tifffile',
        'tkinter'
    ],
    entry_points={
        'console_scripts': [
            'img-to-tiff=smv_to_tiff:start_gui',
        ],
    },
    python_requires='>=3.6',
)