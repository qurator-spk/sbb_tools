from io import open
from setuptools import find_packages, setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name="qurator-sbb-tools",
    version="0.0.4",
    author="Kai Labusch, The Qurator Team",
    author_email="Kai.Labusch@sbb.spk-berlin.de",
    description="Qurator",
    long_description=open("README.md", "r", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    keywords='Qurator',
    license='Apache',
    url="https://github.com/qurator-spk/sbb_tools",
    packages=find_packages(exclude=["*.tests", "*.tests.*",
                                    "tests.*", "tests"]),
    install_requires=install_requires,
    entry_points={
      'console_scripts': [
        "altotool=qurator.sbb.xml:altotool",
        "alto-annotator=qurator.sbb.xml:altoannotator",
        "corpusentropy=qurator.sbb.entropy:main",
        "corpuslanguage=qurator.sbb.language:main",
        "select-by-lang-and-entropy=qurator.sbb.select:by_lang_and_entropy",
        "select-by-lang=qurator.sbb.select:by_lang",

        "batchner=qurator.sbb.ner:on_db_file",
        "ned-statistics=qurator.sbb.ned:ned_statistics",
        "show-ner-models=qurator.sbb.ner:show_models",

        "batchel=qurator.sbb.ned:run_on_corpus",

        "datasette-setup-fulltext=qurator.sbb.datasette:setup_datasette_fulltext"
      ]
    },
    python_requires='>=3.6.0',
    tests_require=['pytest'],
    classifiers=[
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
