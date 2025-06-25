import streamlit as st 
from streamlit_echarts import st_echarts
from scores import get_score, get_user, burnout
from fatigue_charts import circular_progress_chart
from gui import get_gui
from burnout import get_burnout, get_sugg

get_gui()

user_data=get_user()
typing, voice, screen= get_score(user_data)
burnout_score=burnout(typing, screen, voice)

st.markdown(
    "<h1 style='color: #866fc6;'>Fatigue Analysis</h1>",
    unsafe_allow_html=True
)

st.markdown("---")
    
st.header("Fatigue Scores")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader(" Typing Score")
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(typing, "Typing")
    st.markdown('</div>', unsafe_allow_html=True)
    
with col2:
    st.subheader(" Voice Score")
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(voice, "Voice")
    st.markdown('</div>', unsafe_allow_html=True)
    
with col3:
    st.subheader(" Screen Score")
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(screen, "Screen")
    st.markdown('</div>', unsafe_allow_html=True)

st.header("Burnout Score") 
st.text("The burnout score is a single metric that reflects your current mental fatigue level based on your typing, voice, and screen activity patterns.")   
get_burnout(burnout_score)

st.header("Suggestion For You:")
get_sugg(burnout_score)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load data
df = pd.read_csv("fused_scores.csv")
X = df[['typing_score', 'voice_score', 'screen_score']]
y = df['burnout_score']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Model
regressor = RandomForestRegressor(random_state=42)
regressor.fit(X_train, y_train)

# Evaluation
y_pred = regressor.predict(X_test) # Predicted Burnout score
rmse=(mean_squared_error(y_test,y_pred)) # How close the predicted burnout scores are to the actual ones
rr=(r2_score(y_test,y_pred)) #  How much of the variation in burnout scores is explained by the model



import seaborn as sns
import matplotlib.pyplot as plt

st.subheader(" Overall Distribution of Burnout Trends ")

fig, ax = plt.subplots()
sns.histplot(df['burnout_score'], bins=10, kde=True, ax=ax)
ax.set_xlabel("Burnout Score")
ax.set_ylabel("Number of Users")
st.pyplot(fig)



def classify_burnout(score):
    if score < 2.0:
        return 'Low'
    elif score < 3.5:
        return 'Moderate'
    else:
        return 'High'
    
burnout_level=df['burnout_score'].apply(classify_burnout)
# Plot
st.subheader(" Burnout Severity Classification (Across Users)")
level_counts = burnout_level.value_counts()
level_counts=level_counts.reindex(['Low','Moderate','High'], fill_value=0)
st.bar_chart(level_counts)

st.subheader(" Common Fatigue Patterns Among Users")
st.markdown('<div class="subtitle">Based on patterns from multiple users like you, we have identified common burnout patterns. Each color represents a group of users with similar fatigue combinations.</div>', unsafe_allow_html=True)

import numpy as np
from scipy.spatial import ConvexHull
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

# Select features
features = df[['typing_score', 'voice_score', 'screen_score']]

# Run KMeans
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(features)

# 2D plot using just 2 features for now (can use PCA for better separation)
x_col = 'typing_score'
y_col = 'voice_score'



fig, ax = plt.subplots()
colors = ['purple', 'gold', 'teal']

# Plot clusters and convex hulls
for cluster_id in df['cluster'].unique():
    cluster_points = df[df['cluster'] == cluster_id][[x_col, y_col]].values
    ax.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {cluster_id}', color=colors[cluster_id])
    
    # Convex hull
    if len(cluster_points) >= 3:
        hull = ConvexHull(cluster_points)
        for simplex in hull.simplices:
            ax.plot(cluster_points[simplex, 0], cluster_points[simplex, 1], color=colors[cluster_id], linewidth=2)

ax.set_xlabel(x_col.replace("_", " ").title())
ax.set_ylabel(y_col.replace("_", " ").title())
ax.set_title("Clusters with Convex Hull Boundaries")
ax.legend()
st.pyplot(fig)

st.markdown("""

### **Cluster Breakdown**

- 🟣 **Cluster 0** — *High Typing Fatigue*  
  These users show high typing scores with varied voice fatigue. This group may be experiencing strain from frequent or extended typing activity (e.g., reports, chatting, documentation).

- 🟡 **Cluster 1** — *Moderate Voice Fatigue with Low Typing*  
  This profile includes users who may have attended several meetings or spoken a lot without much typing — a potential sign of screen meetings or calls.

- 🟢 **Cluster 2** — *Low Overall Fatigue*  
  These users report low fatigue in both typing and voice interactions. This could indicate healthy activity balance or lower screen engagement for the day.

---

 These groupings help us understand general behavioral patterns and can be used to personalize coping recommendations.
""")


