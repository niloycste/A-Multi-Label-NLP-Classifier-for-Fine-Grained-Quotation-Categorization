# MultiLabel-Quotes-Classifier 

## Objective
This project presents an end-to-end text classification system covering data collection, model training, and deployment. The model is designed to classify 138 distinct quotation genres. For a comprehensive list of identified quote genres, please refer to the keys in `deployment\tag_types_encoded.json`.

## Data Collection
The dataset used for training this model was obtained by scraping quotes from the [Goodreads website](https://www.goodreads.com/quotes) using the Selenium web automation tool. The data includes quotes from various genres such as:

- Love Quotes
- Life Quotes
- Inspirational Quotes
- Humor Quotes
- Philosophy Quotes
- Inspirational Quotes Quotes
- God Quotes
- Truth Quotes
- Wisdom Quotes
- Romance Quotes
- Poetry Quotes
- Death Quotes
- Happiness Quotes
- Hope Quotes
- Faith Quotes

In total, approximately 38,611 quotes were collected. The dataset consists of three main columns: author name, quotation text, and genres.

