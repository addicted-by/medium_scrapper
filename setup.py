from distutils.core import setup
setup(
  name = 'medium_scrapper',         # How you named your package folder (MyLib)
  packages = ['medium_scrapper'],   # Chose the same as "name"
  version = '0.1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Scrapping tools to get information about medium articles',   # Give a short description about your library
  author = 'Aleksey Ryabykin',                   # Type in your name
  author_email = 'ras.unlucky@yandex.ru',      # Type in your E-Mail
  url = 'https://github.com/addicted-by/medium_scrapper',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/addicted-by/medium_scrapper/archive/refs/tags/v0.1.tar.gz',    # I explain this later on
  keywords = ['scrapping', 'medium articles', 'selenium'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'selenium',
          'beautifulsoup4',
          'Pillow',
          'lxml',
          'requests',
          'pandas',
          'tqdm'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)