from setuptools import setup, find_packages


setup(name='web_calculator',
      version='0.1.0',
      author='Sergey Sharay',
      author_email='sergeysharay1987@gmail.com',
      description='A simple online calculator',
      long_description='The application web_calculator allow you to calculate expressions, using five operators "+", '
                       '"-", "*", "/", "**"',
      long_description_content_type='text/restructuredtext',
      url='https://github.com/sergeysharay1987/web_calculator',
      packages = find_packages(), install_requires=['pytest']
      )

