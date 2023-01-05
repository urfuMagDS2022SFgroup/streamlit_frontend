import json
import logging
from typing import Any

import requests
import streamlit as st
from requests import Response

from frontend.constants import BACKEND_URL

logging.basicConfig(level=logging.DEBUG)

url = BACKEND_URL


def load_sentence() -> str | None:
    text_input = st.text_input(label="Text input")
    if text_input:
        return text_input
    return None


@st.cache
def get_project_info() -> Any:
    return requests.request(method="GET", url=url)


def draw_title_and_authors(response: Response) -> None:
    response_text = json.loads(response.text)
    st.title(response_text["message"])
    st.markdown(body=f"""
    ### Authors:
    - {response_text["authors"][0]}
    - {response_text["authors"][1]}
    - {response_text["authors"][2]}
    - {response_text["authors"][3]}
            """)


def draw_git_hub_info(response: Response) -> None:
    response_text = json.loads(response.text)
    st.markdown(f"[our Git Hub]({response_text['git_hub']})")


def post_text_to_predict(to_predict: dict) -> Response:
    return requests.request(method="POST", url=f"{url}predict", json=to_predict)


def draw_sentiment(sentiment: str, lang: str, score: float) -> None:
    report = f"Your language predicted as {lang.upper()} and with probability {score} " \
             f"the sentiment was {sentiment}"
    if sentiment == "NEGATIVE":
        st.error(report, icon="💩")
    elif sentiment == "NEUTRAL":
        st.warning(report, icon="🤔")
    else:
        st.success(report, icon="😇")


def predict_user_sentiment(response: Response) -> None:
    resp_text = json.loads(response.text)
    response_status_code = response.status_code
    if response_status_code == 200:
        draw_sentiment(sentiment=resp_text["sentiment"], lang=resp_text["lang"], score=resp_text["score"])
    elif response_status_code == 400 or response_status_code == 504:
        try:
            st.error(resp_text.error)
        except AttributeError:
            st.error("Sorry, something went wrong")
    else:
        st.error("Sorry, something went wrong")
    st.info("You can try another sentence", icon="ℹ️")


def app():
    project_info_resp = get_project_info()
    draw_title_and_authors(project_info_resp)
    st.markdown(body="## Please enter your phrase in Russian or English and we will try to predict it's sentiment.")
    text = load_sentence()
    draw_git_hub_info(project_info_resp)
    if text:
        with st.spinner("JWST..."):
            payload = {"sentence": text}
            response = post_text_to_predict(payload)
            predict_user_sentiment(response)


app()
