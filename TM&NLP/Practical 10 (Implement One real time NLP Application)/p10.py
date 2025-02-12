# Import required libraries
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from imblearn.over_sampling import SMOTE
import seaborn as sns
import matplotlib.pyplot as plt

# --- Step 1: Download NLTK Resources ---
nltk.download('stopwords')

# --- Step 2: Load External CSV Dataset ---
data_path = "D:/MSCPRACS/Sem3/TM&NLP/Practical 10 (Implement One real time NLP Application)/NewsCategorizer.csv"
external_data = pd.read_csv(data_path)

# Ensure the dataset has the required columns
if 'text' not in external_data.columns or 'label' not in external_data.columns:
    raise ValueError("Dataset must contain 'text' and 'label' columns.")

# Extract texts and labels
texts = external_data['text'].tolist()
labels = external_data['label'].tolist()
print(f"Loaded {len(texts)} samples from the dataset.")

# --- Step 3: Preprocess Text Data ---
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    """Preprocess the text: lowercase, remove special characters, tokenize, remove stopwords, and apply stemming."""
    text = re.sub(r'[^\w\s]', '', text.lower())  # Lowercase and remove special characters
    text = ' '.join([stemmer.stem(word) for word in text.split() if word not in stop_words])
    return text

# Apply preprocessing to all texts
preprocessed_texts = [preprocess_text(doc) for doc in texts]

# --- Step 4: Vectorize Text Data ---
vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1, 3))
X = vectorizer.fit_transform(preprocessed_texts)
y = labels
print(f"TF-IDF Vectorization Complete: {X.shape[0]} samples, {X.shape[1]} features.")

# --- Step 5: Split Data into Training and Testing Sets ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training Set Size: {X_train.shape[0]}, Test Set Size: {X_test.shape[0]}")

# --- Step 6: Train the Model with Logistic Regression ---
# Define parameter grid for GridSearch
param_grid = {'C': [0.1, 1, 10], 'solver': ['liblinear', 'lbfgs']}
grid_search = GridSearchCV(LogisticRegression(max_iter=1000), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Use the best model
model = grid_search.best_estimator_
print("Best Parameters:", grid_search.best_params_)

# --- Step 7: Evaluate the Model ---
# Predict on the test set
y_pred = model.predict(X_test)

# Print evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# --- Step 8: Visualize the Confusion Matrix ---
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=set(labels), yticklabels=set(labels))
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
