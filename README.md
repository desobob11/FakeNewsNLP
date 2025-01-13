
<a id="readme-top"></a>





<br />
<div align="center">
  <a href="https://github.com/desobob11/SDLDoom">
  </a>

  <h3 align="center">Conventional NLP vs LLM Techniques for Fake News Detection</h3>

</div>





## About The Project

This project compares conventional NLP techniques (text preprocessing, manual lemmatization, polarity and sentiment calculations) against LLM embeddings, the detection of fake news articles.

### Built With

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
 	![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
  ![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Data

* Found in the data/ directory

* data/sentiment_anaylsis_classifier
	* includes IMDB and TWEETS datasets

* data/fake_news_conventional
	* contains ISOT, WELFAKE, and LIAR raw datasets
	* once dataset processing script(s) are run, processed version of datasets end up here
	* once classifier models have run, results files end up here (xlsx)


### Scripts

* All scripts are Python scripts or Jupyter notebooks
* Found in the src/ directory

* src/Process_dataset.py
	* Processes a single fake news dataset (ISOT, LIAR, or WELFAKE)
	* Variable 'argv' must be set to one of [ISOT, LIAR, WELFAKE) if running solo
	* this script is run once for each dataset when executing run_conventional_nlp.py

* src/run_conventional_nlp.py
	* runs all Jupyter notebooks that process fake new datasets and perform classification models
	* run this script to process raw ISOT, WELFAKE, and LIAR datasets, and produce classification results
	* results and processed datasets are outputted to data/fake_new_conventional

* src/fake_news_classifiers/
	* contains individual Jupyter notebooks that perform classification for a given dataset

* src/fake_news_dataset_summaries/
	* contains notebooks that perform summary analysis of datasets
	* wordclouds and polarity distributions of articles

* src/sentiment_classifier/
	* two Jupyer notebooks that perform sentiment classification models on TWEETS and IMDB datasets

### Python Packages

* requirements.txt is a pip compatible list of required Python packages
* use pip to install these requirements
*	https://docs.python.org/3/installing/index.html

