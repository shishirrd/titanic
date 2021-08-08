from setuptools import setup

setup(
	name='stock_predictor',
	author = 'Shishir Deshpande',
	packages = ['stock_predictor',],
	package_dir = {'stock_predictor':'stock_predictor',},
	package_data = {'stock_predictor':['mappings/*.csv','sql/*.txt']},
	version='0.0.1',
	description = 'library to help predict stock prices',
	install_requires=[
        'pandas>=1.1.3',
        'numpy>=1.17',
        'pyodbc',
    ],

)
