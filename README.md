NB I have not included the scraped raw HTML files, which total up to 1GB. Please let me know if you would like me to upload these.

The list of propagandistic movies categorised by theme can be found in a nice readable format in `categories.html`.

Below I briefly describe the structure of this project.

### 00 Data Gathering

As expected our IP was flagged by Douban for spamming their servers.
Generally I tried three approaches around this:

- Rotating through a list of free proxies found on the internet
- Waiting for a randomised amount of time before making another request (slow)
- Making parallel requests that spams all proxies at once, removing jobs from a queue

The last approach turned out to be the fastest. Still took a couple days to finish.

### 01 Data Cleaning

Parsing the scraped HTML files into dataframes suitable for data analysis.

### 02 Understanding the Data

Charts and statistics that describe the characteristics of the movie data, like years, languages and genres.

Here I also discussed and built the "actor effects", which were used as controls in the models later.

### 03 Initial Data Analysis

Building statistical models, examining diagnostics and exploring their initial results, without the propaganda dummy.

### 04 Propaganda Analysis

Identifying which movies are propaganda; adding this as a dummy to the covariates; and running the model.

### 05 Further Propaganda Analysis