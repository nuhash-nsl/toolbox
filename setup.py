import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='nuhash_toolbox',
    version='0.0.3',
    author='Md. Afnan Ul Haque',
    author_email='nuhash97afnan@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nuhash-nsl/toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/Muls/toolbox/issues"
    },
    license='MIT',
    packages=['nuhash_toolbox'],
    install_requires=['requests'],
)
