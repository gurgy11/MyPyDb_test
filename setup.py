import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	name="mypydb_gurgy11",
	version="0.0.1",
	author="Gregory Bockus",
	author_email="gregory.bockus@gmail.com",
	description="A small package to help manage a MySQL database.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/gurgy11/MyPyDb",
	project_urls={
		"Bug Tracker": "https://github.com/gurgy11/MyPyDb/issuess",
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	license="GNU General Public",
	package_dir={"": "src"},
	packages=setuptools.find_packages(where="src"),
	python_requires=">=3.6",
)