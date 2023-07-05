import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

# Step 1: Load the dataset
data = pd.read_csv('news_dataset.csv')

# Step 2: Split the dataset into training and testing sets
X = data['text']
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Convert the text into numerical features using TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Step 4: Train a Support Vector Machine (SVM) classifier
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, y_train)

# Step 5: Make predictions on the test set
y_pred = classifier.predict(X_test)

# Step 6: Evaluate the model
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

