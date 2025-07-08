from setuptools import setup, find_packages

setup(
    name="password_strength",
    version="0.1.0",
    description="A simple password strength checker.",
    author="Your Name",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "check-password=password_strength.checker:check_password_strength",
        ],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
