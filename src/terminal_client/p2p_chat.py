#!/usr/bin/env python3
import typer

import p2p_client

app = typer.Typer()


@app.command()
def hello():
    print("Hello world!")


@app.command()
def goodbye():
    print("Goodbye world!")


@app.command()
def listen():
    p2p_client.listen()


@app.command()
def send(ip_address):
    p2p_client.send(ip_address)


if __name__ == '__main__':
    app()
