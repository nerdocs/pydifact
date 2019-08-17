from setuptools import setup

setup(
    name="pydifact",
    version="0.0.1",
    author="Christian González",
    author_email="office@nerdocs.at",
    description="A Python EDI file parser.",
    # install_requires=[],
    url="https://github.com/nerdocs/pydifact",
    packages=["pydifact", "pydifact.control"],
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        # 'Topic :: Documentation :: Sphinx',
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Software Development :: Libraries",
    ],
)
