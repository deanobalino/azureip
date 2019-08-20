import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='azureip',  

     version='0.1.1',

     scripts=['azureip'] ,

     author="Dean Bryen",

     author_email="dean.bryen@microsoft.com",

     description="A Simple tool to check if an IP address is within an Azure subnet",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/deanobalino/azureip",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )