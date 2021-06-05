import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "Apollo",
    version = "0.0.1",
    author = "Ommar Shaikh",
    author_email = "ommarhshaikh@gmail.com",
    description = "Apollo is a Open-Source music player for playback and organization of audio files on Microsoft Windows, built using Python.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/UGLYclown999/Apollo",
    project_urls = {
        "Bug Tracker": "https://github.com/UGLYclown999/Apollo/issues",
    },
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "Programming Language :: Python :: 3",
        "Framework :: Pytest",
        "Framework :: Setuptools Plugin",
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Multimedia :: Sound/Audio",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    package_dir = {"": "apollo"},
    packages = setuptools.find_packages(where = "apollo"),
    python_requires = ">=3.8",
    install_requires=[
        "mutagen==1.45.1",
        "av==8.0.3",
        "pathvalidate==2.4.1",
        "pyo==1.0.3",
        "PySide6==6.1.0"
    ],
    extras_require={
        'development': [
            "coverage==5.5",
            "pytest==6.2.4",
            "pytest-html==3.1.1",
            "Sphinx==4.0.2",
            "sphinx-rtd-theme==0.5.2"
        ],
    },
)
