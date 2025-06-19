from streamlit_lottie import st_lottie
import requests

# Load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return None

# Example calming animation
lottie_calm = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_tll0j4bb.json")  # relaxing animation

st_lottie(lottie_calm, height=300, key="calm")
