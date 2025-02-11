from setuptools import setup, find_packages

setup(
    name="vector_store",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "sentence-transformers",
        "numpy",
        "scipy",
        "sqlite",
        "chromadb"
    ],
    entry_points={
        "console_scripts": [
            "add-doc=scripts.add_document:add_document",
        ],
    },
)
