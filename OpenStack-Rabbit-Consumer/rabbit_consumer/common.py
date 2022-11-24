import logging
import os

from configparser import ConfigParser

logger = logging.getLogger(__name__)
CONFIG_FILE_PATH = "consumer.ini"


class _ConfigMeta(type):
    """
    Wraps a given class to provide the .config property
    for a static type
    """

    # pylint: disable=no-value-for-parameter
    def get_config(cls):
        # Stub to satiate the linter
        raise NotImplementedError()

    @property
    def config(cls):
        return cls.get_config()


class RabbitConsumer(metaclass=_ConfigMeta):
    """
    Class to hold the configuration
    for the consumer application and other future global attrs
    """

    __config_handle = None

    @classmethod
    def get_env_str(cls, key) -> str:
        """
        Get an environment variable
        """
        return os.environ[key]

    @classmethod
    def get_env_int(cls, key) -> int:
        """
        Get an environment variable
        """
        return int(os.environ[key])

    @staticmethod
    def get_config() -> ConfigParser:
        if RabbitConsumer.__config_handle is None:
            RabbitConsumer.__config_handle = RabbitConsumer.__load_config()
        return RabbitConsumer.__config_handle

    @staticmethod
    def reset():
        """
        Resets the currently parsed configuration file.
        Mostly used for testing
        """
        RabbitConsumer.__config_handle = None

    @staticmethod
    def __load_config() -> ConfigParser:
        logger.debug("Reading config from: %s", CONFIG_FILE_PATH)
        config = ConfigParser()
        config.read(CONFIG_FILE_PATH)
        return config
