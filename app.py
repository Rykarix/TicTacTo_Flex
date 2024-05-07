# app.py
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, callback

from src.naughtscrosses.game_logic import NaughtsAndCrosses, Player
from src.webapp.layout import generate_layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

player1 = Player("Player 1", 1, "X")
player2 = Player("Player 2", 2, "O")
game = NaughtsAndCrosses(player1, player2)

app.layout = generate_layout(game)


@callback(
    [
        Output({"type": "cell", "index": f"{i}-{j}"}, "children")
        for i in range(3)
        for j in range(3)
    ]
    + [Output("game-status", "children"), Output("current-player", "children")],
    [
        Input({"type": "cell", "index": f"{i}-{j}"}, "n_clicks")
        for i in range(3)
        for j in range(3)
    ],
    prevent_initial_call=True,
)
def cell_click(*args):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    index_str = eval(button_id)["index"]
    i, j = map(int, index_str.split("-"))
    game.update(i, j)
    board_flat = [
        game.players[game.board[i, j]].symbol if game.board[i, j] != 0 else ""
        for i in range(3)
        for j in range(3)
    ]
    status = (
        f"{game.players[game.winner].name} Wins!"
        if game.game_over and game.winner
        else ("Game Draw!" if game.game_over else "")
    )
    current_player = f"Current Player: {game.players[game.current_player].name}"
    return board_flat + [status, current_player]


if __name__ == "__main__":
    app.run_server(debug=True)
