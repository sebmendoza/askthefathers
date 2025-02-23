from setuptools import setup, find_packages

setup(
    name="askthefathers",
    version="0.0",
    packages=find_packages(where="src"),
    # package_dir={"": "src"},  # Tell setuptools where to find them
)

# Run `pip install -e .` from the /server/ directory
