from app import create_app


app = create_app()


def main():
    app.run(
        host="127.0.0.1",
        port=3001,
        debug=True,
        load_dotenv=True,
    )


if __name__ == "__main__":
    main()
