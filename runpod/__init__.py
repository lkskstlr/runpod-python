""" Allows runpod to be imported as a module. """

from .api_wrapper.ctl_commands import (
    create_pod,
    get_gpu,
    get_gpus,
    get_pod,
    get_pods,
    resume_pod,
    stop_pod,
    terminate_pod,
)

api_key = None  # pylint: disable=invalid-name

api_url_base = "https://api.runpod.io"  # pylint: disable=invalid-name

endpoint_url_base = "https://api.runpod.ai/v2"  # pylint: disable=invalid-name

__version__ = "1.1.3"
