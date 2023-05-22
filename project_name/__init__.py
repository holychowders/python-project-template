import logging


def main() -> None:
    logging.basicConfig(
        format="[%(levelname)s] %(filename)s %(funcName)s(): %(message)s",
        level=logging.INFO,
    )

    logging.info("Hello, world!")


if __name__ == "__main__":
    main()
