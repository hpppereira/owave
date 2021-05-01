import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='owave',  
     version='0.0',
     scripts=['owave'] ,
     author="Henrique Pereira",
     author_email="pereira.henriquep@gmail.com",
     description="Ocean Wave Data Processing",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/pereira.henrique/owave",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: LICENSE",
         "Operating System :: OS Independent",
     ],
 )