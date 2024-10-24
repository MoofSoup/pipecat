#
# Copyright (c) 2024, Daily
#
# SPDX-License-Identifier: BSD 2-Clause License
#

from loguru import logger

logger.warning("DEPRECATED: Package `pipecat.vad` is deprecated, use `pipecat.audio.vad` instead.")

from ..audio.vad.silero import SileroVADAnalyzer
from ..processors.audio.vad.silero import SileroVAD
