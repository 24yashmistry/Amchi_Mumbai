# Amchi Mumbai

<a href="https://amchi-mumbai.onrender.com/" target="_blank">amchi-mumbai.onrender.com</a>

<img src="logo.png" width="350px" height="auto">

## Description

The Mumbai House Price Prediction App is a web application built with Flask that predicts house prices in Mumbai based on user-provided inputs. The application utilizes a machine learning model trained on a dataset from Kaggle. The model is capable of making accurate predictions based on factors such as area, number of bedrooms, and bathrooms.

## Installation Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/mumbai-house-price-prediction.git
    ```

2. Navigate to the project directory:

    ```bash
    cd mumbai-house-price-prediction
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Download the trained machine learning model (`Aamchi_Mumbai_joblib.pkl`) from the repository and place it in the `Model` directory.

5. Download the dataset (`Final Cleaned data.csv`) from the repository and place it in the root directory.

## Usage Guide

1. Run the Flask web application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://localhost:5000](http://localhost:5000).

3. Use the navigation to access the prediction page.

4. Enter the necessary details in the input form, including the location, area, number of bedrooms, and bathrooms.

5. Submit the form to get a predicted house price for the specified location and input parameters.

## Configuration

Adjust the Flask app configuration in `app.py` if needed. Ensure that the paths to the model file (`Aamchi_Mumbai_joblib.pkl`) and the dataset file (`Final Cleaned data.csv`) are correct.

## Contributing Guidelines

We welcome contributions! If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Contact Information

For any questions or concerns, please contact `Yash Mahendra Mistry` at `24yashmistry@gmail.com`

<br /><br />
I Took This Dataset From [Here](https://www.kaggle.com/datasets/goelyash/housing-price-data-of-mumbai?rvi=1)