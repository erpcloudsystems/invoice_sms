from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in invoice_sms/__init__.py
from invoice_sms import __version__ as version

setup(
	name="invoice_sms",
	version=version,
	description="ecs",
	author="info@erpcloud.systems",
	author_email="info@erpcloud.systems",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
