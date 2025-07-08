import logging

from common import configure_logging
logger = logging.getLogger(__name__)

def do_something():
    logger.debug("Prepare to do something")
    logger.info("Doing something")
    logger.warning("Done doing something")

def main():
    configure_logging(level = logging.INFO)
    logger.warning("Hello! Strat")
    do_something()
    logger.warning("Bye! Finish")

if __name__ == "__main__":
    main() 