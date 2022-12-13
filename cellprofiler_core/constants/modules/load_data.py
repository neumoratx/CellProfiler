from cellprofiler_core.constants.measurement import (
    C_URL,
    C_FILE_NAME,
    C_PATH_NAME,
    C_OBJECTS_URL,
    C_OBJECTS_FILE_NAME,
    C_OBJECTS_PATH_NAME,
)
from cellprofiler_core.preferences import (
    DEFAULT_INPUT_FOLDER_NAME,
    DEFAULT_OUTPUT_FOLDER_NAME,
    NO_FOLDER_NAME,
    ABSOLUTE_FOLDER_NAME,
)

IMAGE_CATEGORIES = (
    C_URL,
    C_FILE_NAME,
    C_PATH_NAME,
)
OBJECTS_CATEGORIES = (
    C_OBJECTS_URL,
    C_OBJECTS_FILE_NAME,
    C_OBJECTS_PATH_NAME,
)
DIR_NONE = "None"
DIR_OTHER = "Elsewhere..."
DIR_ALL = [
    DEFAULT_INPUT_FOLDER_NAME,
    DEFAULT_OUTPUT_FOLDER_NAME,
    NO_FOLDER_NAME,
    ABSOLUTE_FOLDER_NAME,
]
PATH_PADDING = 20