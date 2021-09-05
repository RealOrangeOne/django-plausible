from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

setup(
    name="django-plausible",
    version="0.1.0",
    url="https://github.com/RealOrangeOne/django-plausible",
    author="Jake Howard",
    description=" Django module to provide easy Plausible integration, with Wagtail support",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(include=["plausible*"]),
    package_data={"plausible": ["py.typed"]},
    install_requires=["Django>=2.2"],
    python_requires=">=3.6",
    extras_require={"wagtail": ["wagtail>=2.13"]},
    keywords="django plausible wagtail analytics",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development",
        "Typing :: Typed",
    ],
)
