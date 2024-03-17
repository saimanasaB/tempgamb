import streamlit as st
import gambit

def solve_peace_war(peace_payoff, war_payoff, strategy_A, strategy_B):
    # Define the game
    g = gambit.Game.new_table([2, 2])
    g.title = "Peace War Game"
    g.players[0].label = "Country A"
    g.players[1].label = "Country B"

    # Set the payoff values
    g[0, 0][0] = peace_payoff[0]
    g[0, 0][1] = peace_payoff[1]
    g[1, 1][0] = war_payoff[0]
    g[1, 1][1] = war_payoff[1]
    g[0, 1][0] = war_payoff[0] / 2  # Assume half the war payoff for country A
    g[0, 1][1] = war_payoff[1] / 2  # Assume half the war payoff for country B
    g[1, 0][0] = war_payoff[0] / 2  # Assume half the war payoff for country A
    g[1, 0][1] = war_payoff[1] / 2  # Assume half the war payoff for country B

    # Set the strategies
    g[0].set_strategy(strategy_A)
    g[1].set_strategy(strategy_B)

    # Solve the game
    solver = gambit.nash.ExternalEnumMixedSolver()
    solver.quiet = True
    solution = solver.solve(g)

    # Display the results
    st.subheader("Equilibrium Strategy")
    for i, player in enumerate(g.players):
        st.write(f"{player.label}: {', '.join([f'{s:.2f}' for s in solution[i].support()])}")

    st.subheader("Payoff Matrix")
    st.dataframe(g.payoff_matrices[0])

def main():
    st.title("Peace War Game Solver")

    st.write("""
    In the Peace War game, two countries must decide whether to cooperate (peace) or to fight (war). 
    The payoffs depend on the strategies chosen by both countries.
    """)

    peace_payoff_A = st.slider("Peace Payoff for Country A", min_value=0, max_value=10, value=3)
    peace_payoff_B = st.slider("Peace Payoff for Country B", min_value=0, max_value=10, value=3)
    war_payoff_A = st.slider("War Payoff for Country A", min_value=0, max_value=10, value=1)
    war_payoff_B = st.slider("War Payoff for Country B", min_value=0, max_value=10, value=1)
    strategy_A = st.number_input("Strategy for Country A (0-1)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    strategy_B = st.number_input("Strategy for Country B (0-1)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    if st.button("Solve"):
        solve_peace_war((peace_payoff_A, peace_payoff_B), (war_payoff_A, war_payoff_B), (strategy_A, 1 - strategy_A), (strategy_B, 1 - strategy_B))

if __name__ == "__main__":
    main()
import streamlit as st
import gambit

def solve_peace_war(peace_payoff, war_payoff, strategy_A, strategy_B):
    # Define the game
    g = gambit.Game.new_table([2, 2])
    g.title = "Peace War Game"
    g.players[0].label = "Country A"
    g.players[1].label = "Country B"

    # Set the payoff values
    g[0, 0][0] = peace_payoff[0]
    g[0, 0][1] = peace_payoff[1]
    g[1, 1][0] = war_payoff[0]
    g[1, 1][1] = war_payoff[1]
    g[0, 1][0] = war_payoff[0] / 2  # Assume half the war payoff for country A
    g[0, 1][1] = war_payoff[1] / 2  # Assume half the war payoff for country B
    g[1, 0][0] = war_payoff[0] / 2  # Assume half the war payoff for country A
    g[1, 0][1] = war_payoff[1] / 2  # Assume half the war payoff for country B

    # Set the strategies
    g[0].set_strategy(strategy_A)
    g[1].set_strategy(strategy_B)

    # Solve the game
    solver = gambit.nash.ExternalEnumMixedSolver()
    solver.quiet = True
    solution = solver.solve(g)

    # Display the results
    st.subheader("Equilibrium Strategy")
    for i, player in enumerate(g.players):
        st.write(f"{player.label}: {', '.join([f'{s:.2f}' for s in solution[i].support()])}")

    st.subheader("Payoff Matrix")
    st.dataframe(g.payoff_matrices[0])

def main():
    st.title("Peace War Game Solver")

    st.write("""
    In the Peace War game, two countries must decide whether to cooperate (peace) or to fight (war). 
    The payoffs depend on the strategies chosen by both countries.
    """)

    peace_payoff_A = st.slider("Peace Payoff for Country A", min_value=0, max_value=10, value=3)
    peace_payoff_B = st.slider("Peace Payoff for Country B", min_value=0, max_value=10, value=3)
    war_payoff_A = st.slider("War Payoff for Country A", min_value=0, max_value=10, value=1)
    war_payoff_B = st.slider("War Payoff for Country B", min_value=0, max_value=10, value=1)
    strategy_A = st.number_input("Strategy for Country A (0-1)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    strategy_B = st.number_input("Strategy for Country B (0-1)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    if st.button("Solve"):
        solve_peace_war((peace_payoff_A, peace_payoff_B), (war_payoff_A, war_payoff_B), (strategy_A, 1 - strategy_A), (strategy_B, 1 - strategy_B))

if __name__ == "__main__":
    main()
