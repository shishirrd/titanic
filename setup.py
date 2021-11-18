from setuptools import setup

setup(
	name='titanic_predictor',
	author = 'Shishir Deshpande',
	packages = ['titanic_predictor',],
	package_dir = {'titanic_predictor':'titanic_predictor',},
	package_data = {'titanic_predictor':['mappings/*.csv','sql/*.txt']},
	version='0.0.1',
	description = 'library to help predict whether a passenger survived the sinking of the RMS Titanic in 1912',
	install_requires=[
        'pandas>=1.1.3',
        'numpy>=1.17',
        'pyodbc',
    ],

)
