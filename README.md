# Phishing Website Detection Using Machine Learning (Content-Based)

https://deerajgr-phishing-website-detection-using-machine-learning.streamlit.app/

This is an educational project focused on detecting phishing websites using a content-based machine learning approach. Unlike traditional methods that rely on URL features (e.g., domain length), this project analyzes HTML content to classify websites as phishing or legitimate. The project uses Streamlit for an interactive web interface, Scikit-learn for machine learning, BeautifulSoup for HTML parsing, and Requests for web scraping. The dataset is custom-built from legitimate websites (Tranco List) and a simulated phishing dataset, with features extracted from HTML structure.

**Note**: The phishing dataset in this version is simulated by prefixing legitimate URLs with HTTP, which often redirects to HTTPS, resulting in similar content to legitimate sites. This is a known limitation for educational purposes, and real phishing data (e.g., from PhishTank) is recommended for production use.

## Project Overview

The project aims to classify websites as phishing (label: 1) or legitimate (label: 0) by extracting features from HTML content. It includes:

- **Data Collection**: Scrapes websites from the Tranco List (top 1M websites) for legitimate data and simulates phishing data (with limitations).
- **Feature Extraction**: Extracts 43 HTML-based features (e.g., presence of `<input>`, `<button>`, `<iframe>`, counts of tags) using BeautifulSoup.
- **Machine Learning**: Trains seven classifiers (Gaussian Naive Bayes, SVM, Decision Tree, Random Forest, AdaBoost, Neural Network, K-Neighbors) with k-fold cross-validation.
- **Streamlit App**: Provides a user interface to input URLs, select models, and predict phishing/legitimate status, with dataset visualization and download options.

## Key Features

- **Content-Based Approach**: Focuses on HTML structure, avoiding URL-based features.
- **Dataset**: 10,00,000 websites (5,60,000 legitimate, 4,40,000 phishing, collected October 2025).
- **Models**: Seven scikit-learn classifiers, evaluated via accuracy, precision, and recall.
- **Interactive UI**: Streamlit app for predictions, dataset exploration, and results visualization.
- **Open Source**: Code and datasets available for educational use.

## Dataset

The dataset is split into two parts:

- **Legitimate**: Sourced from Tranco List (top 100 websites in this implementation). Fetched with HTTPS, labeled 0.
- **Phishing**: Simulated by fetching Tranco URLs with HTTP, labeled 1. **Caveat**: HTTP requests often redirect to HTTPS, making this data similar to legitimate, which limits model effectiveness for real phishing detection.

### Statistics

- **Total**: 10,00,000 websites (56% legitimate, 44% phishing).
- **Features**: 43 HTML-based (e.g., `has_title`, `number_of_inputs`, `length_of_text`) + URL + label.
- **Available as**: `phishing_legitimate_structured_data.csv` via the Streamlit app.

### Sources

- **Legitimate**: Tranco List (top 1M websites, limited to 100 here).
- **Phishing**: Simulated (intended from PhishTank but not implemented in code).

## Features

The project extracts 43 content-based features from HTML, including:

- **Binary Features**: Presence of `<title>`, `<input>`, `<button>`, `<iframe>`, `<form>`, etc.
- **Count Features**: Number of `<input>`, `<button>`, `<img>`, `<div>`, `<script>`, etc.
- **Text Features**: Length of title, total text length.

Extracted using BeautifulSoup’s `find_all()` and custom logic in `features.py`.

**Note**: Features like `has_image` check `<image>` (likely a typo; should be `<img>`). Dynamic content (e.g., JavaScript-rendered) isn’t captured.

## Machine Learning Models

Seven scikit-learn classifiers are implemented:

- Gaussian Naive Bayes (NB)
- Support Vector Machine (SVM, LinearSVC)
- Decision Tree (DT)
- Random Forest (RF)
- AdaBoost (AB)
- Neural Network (NN, MLPClassifier)
- K-Neighbors (KN)

### Evaluation

- **K-Fold Cross-Validation**: K=5, with accuracy, precision, and recall computed.
- **Results**: Displayed in a table and bar chart in the Streamlit app. Random Forest and Neural Network typically perform best, but results may be skewed due to the phishing data issue.

## Project Structure
phishing-website-detection-content-based/
- ├── app.py                          # Streamlit application
- ├── data_collector_for_legitimate.py # Scrapes legitimate websites
- ├── data_collector_for_phishing.py  # Simulates phishing websites
- ├── feature_extraction.py           # Processes HTML into feature vectors
- ├── features.py                    # Defines feature extraction functions
- ├── machine_learning.py            # Trains and evaluates ML models
- ├── exercises.py                   # Practice script for scraping
- ├── tranco_list.csv                # Source URLs (top 1M websites)
- ├── structured_data_legitimate.csv  # Legitimate dataset
- ├── structured_data_phishing.csv    # Simulated phishing dataset
- ├── requirements.txt               # Dependencies
- ├── mini_dataset/                  # Sample HTML files (from exercises.py)
- └── README.md                     # This file


## Usage

Run the Streamlit App:

`streamlit run app.py`

This opens the app in your browser (default: http://localhost:8501).

Explore the App:

- Project Details: Expand to view the approach, dataset stats (with pie chart), features, and model results.
- Dataset: Use the slider to display rows of the legitimate dataset; download the full dataset as CSV.
- Model Selection: Choose a classifier (e.g., Random Forest) from the dropdown.
- URL Prediction: Enter a URL, click "Check!" to predict if it’s phishing or legitimate.
- Output: "Legitimate" (with balloons) or "Phishing" (with snow animation).
- Example Phishing URLs: Provided in the app, but outdated (from 2022). Update with active phishing URLs for testing.

Efficient Usage Tips:

- Test with Recent URLs: Phishing sites have short lifecycles. Use fresh URLs from PhishTank or similar for accurate testing.
- Model Choice: Random Forest or Neural Network often yield better results for structured data.
- Check Redirects: If URLs redirect (e.g., HTTP to HTTPS), predictions may be inaccurate due to the simulated phishing dataset.
- Extend Dataset: Increase end in data_collector_for_*.py to scrape more URLs (e.g., 1000 instead of 100).
- Debug Failures: If a URL fails, check logs for timeout or SSL errors. Consider adding headers or Selenium for dynamic content.

Re-run Data Collection (if needed):

`python data_collector_for_legitimate.py`
`python data_collector_for_phishing.py`

Warning: Disable SSL verification (verify=False) is used; enable verify=True in production with proper certificates.

Train Models:

`python machine_learning.py`

Outputs metrics and a bar chart (closes after 5 seconds).

## Limitations

- Phishing Dataset: Simulated by using HTTP on legitimate URLs, often redirecting to HTTPS, making it similar to legitimate data. This reduces model effectiveness for real phishing detection.
- Dataset Age: Collected in October 2022; many URLs may be inactive.
- Static HTML: Features miss JavaScript-rendered content (e.g., React apps). Consider Selenium for dynamic sites.
- Security: Disabling SSL verification (verify=False) is insecure for production.
- Features: Some (e.g., has_image checking `<image>`) may be incorrect; `<img>` is standard.

## Future Improvements

- Real Phishing Data: Integrate PhishTank or other verified phishing URL sources.
- Dynamic Content: Use Selenium or Playwright to capture JavaScript-rendered HTML.
- Feature Expansion: Add URL-based features (e.g., domain entropy) for a hybrid approach.
- Hyperparameter Tuning: Optimize ML models for better performance.
- Update Dependencies: Use latest versions of Streamlit, scikit-learn, etc.
- Real-Time Scraping: Enhance app to fetch and process URLs dynamically with anti-scraping measures (e.g., headers, proxies).

## Contributing

Contributions are welcome! To contribute:

- Fork the repository.
- Create a branch (git checkout -b feature/your-feature).
- Commit changes (git commit -m "Add your feature").
- Push to the branch (git push origin feature/your-feature).
- Open a pull request.

Please report bugs or suggest features via GitHub Issues.

## Contact

For questions or feedback, contact deerajgr or open a GitHub Issue.

## Acknowledgments

- Tranco List: For legitimate website rankings.
- PhishTank: Referenced for phishing data (though not implemented).
- Streamlit & Scikit-learn: For making UI and ML accessible.

Happy Detecting! Stay safe from phishing attacks.
