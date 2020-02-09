from setuptools import setup, find_packages


setup(name="datetime-quarter",
      version="1.0.3",
      url="https://github.com/BetaS/datetime-quarter",
      author="BetaS",
      author_email="thou1999@gmail.com",
      description="Simple and lightweight quarter support for python datetime",
      packages=find_packages(),
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License"
      ]
)