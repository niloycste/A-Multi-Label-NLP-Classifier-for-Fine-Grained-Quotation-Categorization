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
- Success Quotes
-Life Quotes Quotes 
-Time Quotes 
-Motivation Quotes etc.

In total, approximately 38,611 quotes were collected. The dataset consists of three main columns: author name, quotation text, and genres. the data are stored in **`Dataset/dataquotes.csv`**.

## Data Preprocessing
At first, there were 23,415 different kinds of genres in the dataset. After looking closely, I noticed many of them were rare, so I got rid of those uncommon ones. In the end, I settled on 138 genres. Also, I removed some quotes that didn't have any genre assigned, leaving me with a total of 38,607 data points.The preprocessing can be found in **`notebook/NLP_Multilabel_Classification.ipynb`**.
