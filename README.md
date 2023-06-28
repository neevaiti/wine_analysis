
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

# My Plan for Executing this Project and Process Explanation:

### First, the cleanup of the initial provided dataset `Flux_HistoPrice_example.csv`:

As we can see, the dataset is relatively light (not many rows), consisting of three columns (`vnid`: a wine identifier, `vintage`: the year of bottling, `PriceHistory`: the evolution of price over time).

__Accomplishment:__ The dataset presented some complexity when converting the `PriceHistory` column (changing to date and integer formats), as well as separating the date and price stored in false dictionaries within a list.

Next, I performed a comprehensive analysis of the data available, within the limited time I had to work on this project (there were many complex projects: Computer Vision and Azure CI/CD).

### Dataset Research for Cross-Analysis:

For this part of the project, I unfortunately did not have the time to perform the analysis as I prioritized working on web scraping. However, with the web scraping not functioning as planned, I had already begun research on [Kaggle](https://www.kaggle.com/).

I found some relevant datasets that included ratings, domain names, and components:

- https://www.kaggle.com/datasets/budnyak/wine-rating-and-price
- https://www.kaggle.com/datasets/zynicide/wine-reviews
- https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009

### Scraping w/ Scrapy:

The site targeted for scraping was: [Website](https://www.idealwine.com/fr/saga_millesime/table_notation.jsp).

Scraping can sometimes be a labor-intensive and time-consuming task, which was the case for this project! The extent of the task depends on the structure of the sites. With very limited time, I attempted to retrieve the ratings of various wines by `vintage`, with the aim to cross-reference the data in meaningful analyses to potentially explain price fluctuations. 

In total, I spent 1.5 days on this project. The most time-consuming aspect was the conversion work on the initial dataset, but I eventually succeeded thanks to a conversion technique with the datetime package.


## Useful Documentation

- [Kaggle](https://www.kaggle.com/)
- [Pandas](https://pandas.pydata.org/docs/index.html)
- [Matplotlib](https://matplotlib.org/)
- [Scikit-learn](https://scikit-learn.org/stable/) 
- [Python](https://docs.python.org/3/)

