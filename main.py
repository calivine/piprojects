import sys

from naturepi.naturecam import NatureCam


def _real_main(argv=None):
    NatureCam().activate()


try:
    _real_main()
except KeyboardInterrupt:
    sys.exit('\nERROR: Interrupted by user')
