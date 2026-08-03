# 🏆 FIFA-Probability
Simulating the 2026 FIFA World Cup in Python using a custom mathematical model, evaluating predicted tournament progression against real-world performance.

**📌 Author's Note**
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Project Background & Model Performance: Developed as a first-year student fresh out of high school board exams, this project served as an exploratory application of data ingestion, feature engineering, and Monte Carlo statistical mechanics. Generative AI assistants (including Gemini, Claude, and ChatGPT) were leveraged across select sections of the codebase to assist with module structuring and optimization. Despite structural simplifications, such as omitting real-time squad dynamics or in-game variables—the model demonstrated strong alignment with real-world results:

**Actual Tournament Outcome:** Spain won the 2026 FIFA World Cup, defeating Argentina 1–0 after extra time in the final.  
**Simulation Predictions:** The 100,000-run simulation identified Spain and Argentina as the 2nd and 3rd favorite contenders to win the trophy overall, finishing just behind Portugal (1st favorite).


**⚙️ Overall Summary of the project**
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**1. Data Ingestion & Cleaning (Filter_data.py): Processes raw international football match data from (recents.csv) Johns Hopkins, filtering it into a cleaned dataset (recent_data.csv).**

**2. Qualification Filtering: Extracts match histories strictly for 2026 World Cup qualified teams to produce WC_data.csv.**

**3. Feature Engineering: Aggregates performance metrics into World Cup Final Data.csv, computing each team's total matches, wins, losses, ties, win/loss/draw percentages, and goals scored per match.** 

**4. Tournament Simulation (Main.py): Feeds these processed metrics into a custom mathematical model to calculate match probabilities and simulate tournament results and store this results in the Championship_Simulation_Results.csv file.**


**📐 EXPLANATION OF THE MATHEMATICAL MODEL:**
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**1. FIFA Tier & Multiplier System (Adjusting for Competition)**
Not all wins are created equal—a victory against a top-tier national team tells us more about a team's strength than a win against a lower-ranked opponent.
Ranking Tiers: Teams are grouped into four tiers based on their official FIFA World Ranking. Top-10 teams belong to Tier 1, while teams ranked outside the top 50 fall into Tier 4.
Stage-Based Boosts: A team’s historical win, loss, and draw rates are scaled up or down based on their tier. Higher-ranked teams get stronger rating boosts during the group stage and early knockout rounds.
Level Playing Field: By the time teams reach the Semifinals and Final, all artificial multipliers are dropped so the final matches are decided purely on raw performance metrics without extra weighting.

**2. Tug-of-War Match Outcome Model (Offense vs. Defense)**
To determine the odds of any individual match outcome—Team A winning, Team B winning, or a Draw—the model pairs one team’s attacking capability directly against the other team’s defensive vulnerability.
Team A Win Odds: Calculated by combining Team A’s boosted win tendency with Team B’s boosted loss tendency (representing Team B's likelihood to give up games).
Team B Win Odds: Calculated by combining Team B’s boosted win tendency with Team A’s boosted loss tendency.
Draw Odds: Calculated by combining the draw rates of both teams.
Normalizing to 100%: The three raw outcome scores are added together and converted into clean percentages that total 100%.

**3. Tournament Progression & Tie-Breakers**
Group Stage Scoring: Teams earn standard group points: 3 for a win, 1 for a draw, and 0 for a loss.
Breaking Group Ties: If two or more teams finish the group stage with the exact same number of points, the model uses their historical average goals per match as the primary tie-breaker to determine who advances. The logic behind this is that a team having more goals scored per match can be considered as a aggressive team which leads to more chances of having a higher goal difference.
Knockout Penalty Shootouts: If a knockout match finishes in a draw, extra time dynamics are bypassed and the match outcome is decided by simulating a 50/50 coin flip representing a penalty shootout.

**4. Monte Carlo Simulation Engine (Running 100,000 World Cups)**
Single football matches are inherently random—an early red card or a deflection can change everything. To account for this variance, the computer doesn't just run the tournament once.
Massive Iteration: The model simulates the entire 48-team World Cup 100,000 times from start to finish.
Calculating Championship Probability: Each team's overall chance of lifting the trophy is calculated simply as the number of times they won the tournament divided by 100,000.
Statistical Stability: Running tens of thousands of simulations ensures that short-term luck evens out, leaving behind a reliable, statistically stable prediction of every team's true championship odds.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
**⚖️ Model Evaluation: Strengths & Limitations**


**⚖️ Advantages**
---Strength-Adjusted: Multipliers account for quality of opposition, so weak-schedule records aren't overvalued.

---Balanced Evaluation: The Tug-of-War model factors in both attacking strength and defensive vulnerability.

---Statistically Stable: 100,000 Monte Carlo runs smooth out single-match flukes to reveal true odds.

---Fast & Decisive: Simple mathematical weights allow rapid multi-run computing and clean group tie-breaking.

**⚖️ Disadvantages**
---Ignores Current Form: Relies on historical averages, missing recent momentum, squad injuries, or tactical changes.

---Oversimplified Shootouts: Knockout ties use a basic 50/50 flip, ignoring keeper skill and penalty history.

---No In-Game Realism: Omits crucial variables like red cards, weather, fatigue, or home-continent advantage.

---Arbitrary Tier Cutoffs: A hard boundary separates 10th and 11th rank, creating artificial strength gaps.







