from setuptools import setup, find_packages

setup(
    name="proyecto_anuncios_publicitarios",
    version="0.1.0",
    description="Sistema de gestión de anuncios publicitarios",
    author="TheGodsOfProgramming",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        # Este proyecto no requiere dependencias externas
    ],
    entry_points={
        "console_scripts": [
            "anuncios=src.main:main",
        ],
    },
)