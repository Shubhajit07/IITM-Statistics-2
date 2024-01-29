import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Monte Carlo Simulation For Coin Toss")


def roll_dice(num):
    """Simulate a coin toss by randomly selecting heads or tails."""
    simulations = dict([(x,0) for x in range(1,7)])
    for _ in range(num):
        sim = random.choice([1,2,3,4,5,6])
        simulations[sim] = simulations.get(sim,0)+1

    return simulations


with st.container(border=True):
    num_sims = st.slider(
        "Select the number of simulations", min_value=10, max_value=10_00_000, step=1
    )
    if num_sims:
        simulations = roll_dice(num_sims)
        st.bar_chart(simulations)
        df = pd.DataFrame.from_dict(simulations, orient="index", columns=["Occurances"])
        df["Probability"] = df["Occurances"] / num_sims * 100
        df["Probability"] = df["Probability"].apply(lambda x: "{:.3f}%".format(x))
        st.table(df)
