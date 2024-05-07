import dash_bootstrap_components as dbc
from dash import dcc, html


def generate_layout(game):
    def generate_board():
        board = html.Table(
            [
                html.Tr(
                    [
                        html.Td(
                            dbc.Button(
                                game.players[game.board[i, j]].symbol
                                if game.board[i, j] != 0
                                else "",
                                id={
                                    "type": "cell",
                                    "index": f"{i}-{j}",
                                },
                                color="light",
                                disabled=game.game_over,
                                n_clicks=0,
                            ),
                            style={
                                "border": "1px solid black",
                                "width": "100px",
                                "height": "100px",
                                "textAlign": "center",
                            },
                        )
                        for j in range(3)
                    ]
                )
                for i in range(3)
            ]
        )
        return board

    return dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    html.H3("Naughts and Crosses Game"), width={"size": 6, "offset": 3}
                )
            ),
            dbc.Row(dbc.Col(generate_board(), width={"size": 6, "offset": 3})),
            dbc.Row(
                dbc.Col(html.Div(id="game-status"), width={"size": 6, "offset": 3})
            ),
            dbc.Row(
                dbc.Col(
                    html.Div(
                        f"Current Player: {game.players[game.current_player].name}",
                        id="current-player",
                    ),
                    width={"size": 6, "offset": 3},
                )
            ),
        ]
    )
