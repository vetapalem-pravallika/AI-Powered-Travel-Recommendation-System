**AI-Powered Travel Recommendation System**
**Project Overview**
The AI-Powered Travel Recommendation System recommends tourist destinations in India based on the similarity of features such as type, city, significance, and ratings. Users can select a place and get personalized recommendations for other similar places.
Live Demo: [Click Here to View](https://ai-powered-travel-recommendation-system-ibqx2aqgzadgacqyk3wxwz.streamlit.app/)
GitHub Repository: Click Here
**Features**
Recommend similar tourist destinations across India.
Adjustable number of recommendations (3–10) using a slider.
Scrollable and clean interface for easy viewing.
Filter recommendations based on place features such as type and significance.
**System Architecture**
+-----------------+
|   User Input    |
| (Selected Place)|
+--------+--------+
         |
         v
+-----------------+
| Preprocessed    |
| Dataset (travel_df.pkl) |
+--------+--------+
         |
         v
+-----------------+
| TF-IDF Features |
| & Cosine Similarity |
+--------+--------+
         |
         v
+-----------------+
| Recommendation  |
| Engine           |
+--------+--------+
         |
         v
+-----------------+
|   Streamlit UI  |
| Displays Results|
+-----------------+
**Explanation:**
Users select a tourist destination from a dropdown.
The system calculates similarity using TF-IDF and Cosine Similarity on features like Type, City, Significance, and Best Time to Visit.
Top-N similar places are recommended.
Recommendations are displayed in a scrollable, user-friendly interface.
**System Requirements**
Hardware:
Processor: Intel i3 or higher
RAM: Minimum 4 GB
Storage: Minimum 10 GB free space
Software:
Operating System: Windows
Programming Language: Python 3.x
Development Environment: Google Colab / Notepad
Web Framework: Streamlit
Libraries Used:
NumPy – Numerical computations
Pandas – Data handling & preprocessing
Scikit-learn – TF-IDF & Cosine Similarity
Matplotlib – Visualization
Streamlit – Web app development
OS & Pickle – File handling & model saving/loading
**How to Run Locally**
**Clone the repository:*
git clone https://github.com/vetapalem-pravallika/AI-Powered-Travel-Recommendation-System.git
**Navigate to the project folder:**
cd AI-Powered-Travel-Recommendation-System
**Install dependencies:**
pip install -r requirements.txt
**Run the Streamlit app:**
streamlit run app.py
Open the URL shown in the terminal to access the app locally.
**Future Scope**
Add more features such as budget, distance, and user preferences.

Integrate real-time data from travel APIs for hotels, transport, and weather.

Add multi-language support for better accessibility.
