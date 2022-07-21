import sys

from naturecam import NatureCam


def _real_main(argv=None):
    NatureCam().activate()


def main(argv=None):
    try:
        _real_main()
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')