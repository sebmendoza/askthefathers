from setuptools import setup, find_packages

setup(
    name="askthefathers",
    version="0.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "fastapi[standard]==0.135.3",
        "chromadb",
        "google-genai",
        "python-dotenv",
    ],
)
