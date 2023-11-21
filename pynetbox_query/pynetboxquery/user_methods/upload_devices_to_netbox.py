from dataclasses import asdict
from pynetboxquery.utils.read_utils.read_file import ReadFile
from pynetboxquery.netbox_api.validate_data import ValidateData
from pynetboxquery.utils.query_device import QueryDevice
from pynetboxquery.netbox_api.netbox_create import NetboxCreate
from pynetboxquery.netbox_api.netbox_connect import api_object
from pynetboxquery.utils.parsers import Parsers


def upload_devices_to_netbox(url: str, token: str, file_path: str, **kwargs):
    """
    This function does the following:
    Create a Pynetbox Api Object with the users credentials.
    Reads the file data into a list of Device dataclasses.
    Validates the Device names and device types against Netbox.
    Converts the data in the Devices to their Netbox ID's.
    Changes those Device dataclasses into dictionaries.
    Creates the Devices in Netbox.
    :param url: The Netbox URL.
    :param token: The user's Netbox api token.
    :param file_path: The file path.
    """
    api = api_object(url, token)
    device_list = ReadFile().read_file(file_path, **kwargs)
    ValidateData().validate_data(
        device_list, api, **{"fields": ["name", "device_type"]}
    )
    queried_devices = QueryDevice(api).query_list(device_list)
    dictionary_devices = [asdict(device) for device in queried_devices]
    NetboxCreate(api).create_device(dictionary_devices)
    print("Devices added to Netbox.\n")


def _parser():
    """
    This function creates the subparser for this user script inheriting the parent parser arguments.
    """
    parent_parser, main_parser, subparsers = Parsers().arg_parser()
    subparsers.add_parser(
        "create_devices",
        description="Create devices in Netbox from a file.",
        usage="pynetboxquery create_devices <filepath> <url> <token> <options>",
        parents=[parent_parser],
        aliases=["create"],
    )
    return main_parser


def aliases():
    """
    This function returns a list of aliases the script should be callable by.
    """
    return ["create", "create_devices"]


def _collect_args():
    """
    This function calls the parser function and returns the namespace arguments in a dictionary.
    """
    main_parser = _parser()
    kwargs = vars(main_parser.parse_args())
    return kwargs


def main():
    """
    This function collects the arguments and calls the upload function.
    """
    kwargs = _collect_args()
    upload_devices_to_netbox(**kwargs)
