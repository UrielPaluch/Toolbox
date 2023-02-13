import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.3',
    author='Uriel Paluch',
    author_email='uripaluch2@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/UrielPaluch/Toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/UrielPaluch/Toolbox/issues"
    },
    packages=['toolbox'],
    install_requires=['requests'],
)
