import importlib
import sys
from pynetboxquery.utils.error_classes import UserMethodNotFoundError


def main():
    """
    This function will run the correct user method for the action specified in the CLI.
    """
    user_methods_names = ["upload_devices_to_netbox", "validate_data_fields_in_netbox"]
    found = False
    for user_method in user_methods_names:
        user_method_module = importlib.import_module(
            f"pynetboxquery.user_methods.{user_method}"
        )
        aliases = getattr(user_method_module, "aliases")()
        if sys.argv[1] in aliases:
            user_method_module.main()
            found = True
    if not found:
        raise UserMethodNotFoundError(f"The user method {sys.argv[1]} was not found.")


if __name__ == "__main__":
    main()
