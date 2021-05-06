import logging, sys, argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "-log", 
    "--log", 
    default="warning",
    help=(
        "Provide logging level. "
        "Example --log debug', default='warning'"),
    )


options = parser.parse_args()
levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}
level = levels.get(options.log.lower())
if level is None:
    raise ValueError(
        f"log level given: {options.log}"
        f" -- must be one of: {' | '.join(levels.keys())}")

logging.basicConfig(level=level)
logger = logging.getLogger(__name__)

logging.info("this is INFO level")
logging.warning("this is WARNING level")
logging.error("this is ERROR level")
