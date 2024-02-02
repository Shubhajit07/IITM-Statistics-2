import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Monte Carlo Simulation For Coin Toss")


def toss_coin(num):
    """Simulate a coin toss by randomly selecting heads or tails."""
    simulations = {"Heads": 0, "Tails": 0}
    mapping = {0: "Tails", 1: "Heads"}
    for _ in range(num):
        sim = random.randint(0, 1)
        simulations[mapping[sim]] += 1

    return simulations


with st.container(border=True):
    num_sims = st.number_input(
        "Enter the number of simulations", min_value=1, step=1, placeholder="Enter a number"
    )
    if num_sims:
        simulations = toss_coin(num_sims)
        st.bar_chart(simulations)
        df = pd.DataFrame.from_dict(simulations, orient="index", columns=["Occurances"])
        df["Probability"] = df["Occurances"] / num_sims * 100
        df["Probability"] = df["Probability"].apply(lambda x: "{:.3f}%".format(x))
        st.table(df)
