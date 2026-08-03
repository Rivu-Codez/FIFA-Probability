# FIFA-Probability
Simulating the 2026 FIFA World Cup in Python using a custom mathematical model, evaluating predicted tournament progression against real-world performance.

This project builds an end-to-end Python pipeline and custom mathematical model to simulate the 2026 FIFA World Cup and evaluate prediction accuracy against actual tournament outcomes:

**1. Data Ingestion & Cleaning (Filter_data.py): Processes raw international football match data from (recents.csv) Johns Hopkins, filtering it into a cleaned dataset (recent_data.csv).**

**2. Qualification Filtering: Extracts match histories strictly for 2026 World Cup qualified teams to produce WC_data.csv.**

**3. Feature Engineering: Aggregates performance metrics into World Cup Final Data.csv, computing each team's total matches, wins, losses, ties, win/loss/draw percentages, and goals scored per match.** 

**4. Tournament Simulation (Main.py): Feeds these processed metrics into a custom mathematical model to calculate match probabilities and simulate tournament results and store this results in the Championship_Simulation_Results.csv file.**

**EXPLANATION OF THE MATHEMATICAL MODEL**
