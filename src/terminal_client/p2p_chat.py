#!/usr/bin/env python3
import typer

import p2p_client

app = typer.Typer()


@app.command()
def start():
    p2p_client.start()


if __name__ == '__main__':
    app()
