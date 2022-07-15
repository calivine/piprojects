import sys

from naturecam import NatureCam


def _real_main():
    NatureCam().activate()


try:
    _real_main()
except KeyboardInterrupt:
    sys.exit('\nERROR: Interrupted by user')