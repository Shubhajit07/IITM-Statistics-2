import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Monte Carlo Simulation For Dice Roll")


def roll_dice(num):
    """Simulate a dice roll by randomly selecting from 1 to 6."""
    simulations = dict([(x,0) for x in range(1,7)])
    for _ in range(num):
        sim = random.choice([1,2,3,4,5,6])
        simulations[sim] = simulations.get(sim,0)+1

    return simulations


with st.container(border=True):
    num_sims = st.number_input(
        "Enter the number of simulations", min_value=1, step=1, placeholder="Enter a number"
    )
    if num_sims:
        simulations = roll_dice(num_sims)
        st.bar_chart(simulations)
        df = pd.DataFrame.from_dict(simulations, orient="index", columns=["Occurances"])
        df["Probability"] = df["Occurances"] / num_sims * 100
        df["Probability"] = df["Probability"].apply(lambda x: "{:.3f}%".format(x))
        st.table(df)
