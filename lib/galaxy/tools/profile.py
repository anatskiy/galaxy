import logging

from .test import _process_raw_inputs

log = logging.getLogger(__name__)


def parse_profiles(tool, profiles_source):
    """
    Build ToolProfileBuilder objects for each "<profile>" elements and
    return default interactor (if any).
    """
    raw_profiles_dict = profiles_source.parse_profiles_to_dict()
    profiles = []
    for i, raw_profile_dict in enumerate(raw_profiles_dict.get('profiles', [])):
        profile = description_from_tool_object(tool, i, raw_profile_dict)
        profiles.append(profile)

    print('PROFILES', profiles)

    return profiles


def description_from_tool_object(tool, profile_index, raw_profile_dict):
    return None
