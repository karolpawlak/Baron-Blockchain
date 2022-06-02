from app import app

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help="Specify the port to listen to with --port or -p")
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port, debug=True)
