Future Ideas
- Server Client Model to host game
- Thread (player) can be a computer (AI agent)
    - Thread is signaled to decide whether to bet, fold, or call
    - Player is attempting to maximize money at the end of round
- Develop Game Analysis tool 
    - What is Expected Value of Player tendencies
    - Range predictor (of opponent)
    - Whether play is +/- EV / what bet amount would make it + EV
    - Recommendation System

Consider alternating suite representation (one hot encoder)

===============
AI ideas
Measures of success:
    1. Final Profit (Financial)
    2. Final Profit (Poker)
    3. Expected Value Play
    4. Reinforcement Learning

2 agent ideas
    - best current situation decision based on no history
    - best decision taking into account history of players
===============
inputs to agent
    - current pot size
    - curent bet amount
    - number people left in the round
        - someway to play based on history of player's behavior