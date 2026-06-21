# Blood Donation Prediction System

## Description

The Blood Donation Prediction System is a Machine Learning project that predicts whether a person is likely to donate blood again based on their previous donation history.

The project helps blood banks identify potential donors and improve blood availability.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit

---

## Features

* Predict future blood donation behavior
* Simple user interface
* Fast and accurate predictions
* Easy to use

---

## Dataset Features

* Recency (Months since last donation)
* Frequency (Total donations made)
* Monetary (Total blood donated)
* Time (Months since first donation)

---

## How to Run

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python train_model.py
```

### Run the Application

```bash
streamlit run app.py
```
or

```bash
python -m streamlit run app.py
```
---

## Sample Input

* Month since last donation = 2
* Total Donations = 30
* Totoal Blood Donated = 7500
* Month since First Donation = 70

OR

* For bulk prediction : Bulk_example.csv

## Sample Output

Likely to Donate Blood Again

---

## Future Improvements

* Email notifications
* SMS reminders
* Mobile application
* Hospital integration

---

