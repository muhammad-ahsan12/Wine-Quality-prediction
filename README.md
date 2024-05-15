#Wine Quality Prediction using Random Forest Classifiers
This repository contains code for predicting the quality of wine using random forest classifiers. The dataset used for this project contains various physicochemical properties of wine, such as acidity, pH level, alcohol content, etc., along with a quality rating.

#About the Dataset
The dataset used in this project is publicly available on the UCI Machine Learning Repository. It consists of two datasets, one for red wine and another for white wine. Each dataset contains several attributes along with a quality rating provided by experts.

Red Wine Dataset: link
White Wine Dataset: link
#Dependencies
To run the code in this repository, you'll need the following Python libraries:
pandas
numpy
scikit-learn
streamlit
   You can install these dependencies using pip:

   pip install pandas numpy scikit-learn streamlit
#Usage
To predict the quality of wine using random forest classifiers and provide a user interface for interacting with the model, follow these steps:

Clone this repository to your local machine.
Navigate to the repository directory.
Run the Streamlit app using the following command:

  streamlit run app.py
Open your web browser and go to the provided URL (usually http://localhost:8501) to access the user interface.
Follow the instructions on the interface to input the wine attributes and get predictions for wine quality.
#License
This project is licensed under the MIT License. See the LICENSE file for details.

#Acknowledgements
The wine quality dataset is sourced from the UCI Machine Learning Repository. Citation details are provided in the dataset links above.
This project is inspired by the need to explore machine learning techniques for predicting wine quality based on its physicochemical properties, and providing a user-friendly interface for users to interact with the model.
#Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
