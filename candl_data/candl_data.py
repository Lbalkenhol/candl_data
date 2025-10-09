"""
Short cuts to ``.yaml`` files for released data sets.

Overview:
------------------------

* :const:`SPT3G_2018_TTTEEE`: SPT3G 2018 TTTEEE data set.
* :const:`SPT3G_2018_Lens`: SPT3G 2018 Lensing data set.
* :const:`SPT3G_2018_Lens_and_CMB`: SPT3G 2018 Lensing data set, with transformations for combined constraints with primary CMB.
* :const:`ACT_DR6_Lens`: ACT DR6 Lensing data set.
* :const:`ACT_DR6_Lens_and_CMB`: ACT DR6 Lensing data set, with transformations for combined constraints with primary CMB.
* :const:`ACT_DR6_TTTEEE`: ACT DR6 TTTEEE data set.
* :const:`ACT_DR4_TTTEEE`: ACT DR4 TTTEEE data set.
* :const:`SPTpol_BB`: SPTpol BB data set.
* :const:`SPT3G_D1_BB_lite`: SPT-3G D1 BB lite data set.
"""

# Grab Data Path
import os

data_path = os.path.dirname(os.path.realpath(__file__))

# --------------------------------------#
# DATA SETS
# --------------------------------------#

# SPT-3G 2018 TT/TE/EE
SPT3G_2018_TTTEEE = f"{data_path}/SPT3G_2018_TTTEEE_v0/SPT3G_2018_TTTEEE_index.yaml"
SPT3G_2018_TTTEEE_multifreq = f"{data_path}/SPT3G_2018_TTTEEE_v0/SPT3G_2018_TTTEEE.yaml"
SPT3G_2018_TTTEEE_lite = f"{data_path}/SPT3G_2018_TTTEEE_v0/SPT3G_2018_TTTEEE_lite.yaml"

# SPT-3G 2018 Lensing
SPT3G_2018_Lens = f"{data_path}/SPT3G_2018_Lens_v0/SPT3G_2018_PP_index.yaml"
SPT3G_2018_Lens_only = f"{data_path}/SPT3G_2018_Lens_v0/SPT3G_2018_PP_lens_only.yaml"
SPT3G_2018_Lens_and_CMB = (
    f"{data_path}/SPT3G_2018_Lens_v0/SPT3G_2018_PP_lens_and_CMB.yaml"
)

# ACT DR4 TT/TE/EE
ACT_DR4_TTTEEE = f"{data_path}/ACT_DR4_CMB_only_v0/ACT_DR4_CMB_only.yaml"

# ACT DR6 TT/TE/EE
ACT_DR6_TTTEEE = f"{data_path}/ACT_DR6_CMB_only_v0/ACT_DR6_CMB_only.yaml"

# ACT DR6 Lensing
ACT_DR6_Lens = f"{data_path}/ACT_DR6_Lens_v1/ACT_DR6_KK_index.yaml"
ACT_DR6_Lens_only = f"{data_path}/ACT_DR6_Lens_v1/ACT_DR6_KK_lens_only.yaml"
ACT_DR6_Lens_and_CMB = f"{data_path}/ACT_DR6_Lens_v1/ACT_DR6_KK_lens_and_CMB.yaml"

# SPTpol BB
SPTpol_BB = f"{data_path}/SPTpol_BB_v0/SPTpol_BB_index.yaml"
SPTpol_BB_multifreq = f"{data_path}/SPTpol_BB_v0/SPTpol_BB.yaml"
SPTpol_BB_lite = f"{data_path}/SPTpol_BB_v0/SPTpol_BB_lite.yaml"

# SPT-3G D1 BB lite
SPT3G_D1_BB_lite = f"{data_path}/SPT3G_D1_BB_lite_v0/SPT3G_D1_BB_lite.yaml"

# --------------------------------------#
# PREPARE SHORCUTS AND INFO
# --------------------------------------#

# Define Shortcuts
shortcuts = {
    "SPT-3G 2018 TT/TE/EE": {
        "index": "SPT3G_2018_TTTEEE",
        "multifreq": "SPT3G_2018_TTTEEE_multifreq",
        "lite": "SPT3G_2018_TTTEEE_lite",
    },
    "SPT-3G 2018 Lensing": {
        "index": "SPT3G_2018_Lens",
        "lens_only": "SPT3G_2018_Lens_only",
        "use_cmb": "SPT3G_2018_Lens_and_CMB",
    },
    "ACT DR4 TT/TE/EE": "ACT_DR4_TTTEEE",
    "ACT DR6 TT/TE/EE": "ACT_DR6_TTTEEE",
    "ACT DR6 Lensing": {
        "index": "ACT_DR6_Lens",
        "lens_only": "ACT_DR6_Lens_only",
        "use_cmb": "ACT_DR6_Lens_and_CMB",
    },
    "SPTpol BB": {
        "index": "SPTpol_BB",
        "multifreq": "SPTpol_BB_multifreq",
        "lite": "SPTpol_BB_lite",
    },
    "SPT-3G D1 BB lite": "SPT3G_D1_BB_lite",
}

# Additional Information
info = {
    "SPT-3G 2018 TT/TE/EE": {
        "index": None,
        "multifreq": "default, original multi-frequency likelihood",
        "lite": "foreground-marginalised CMBlite version",
    },
    "SPT-3G 2018 Lensing": {
        "index": None,
        "lens_only": "default",
        "use_cmb": "for combining with primary CMB",
    },
    "ACT DR4 TT/TE/EE": None,
    "ACT DR6 TT/TE/EE": None,
    "ACT DR6 Lensing": {
        "index": None,
        "lens_only": "default",
        "use_cmb": "for combining with primary CMB",
    },
    "SPTpol BB": {
        "index": None,
        "multifreq": "default, original multi-frequency likelihood",
        "lite": "foreground-marginalised CMBlite version",
    },
    "SPT-3G D1 BB lite": None,
}

# --------------------------------------#
# PRINT SHORTCUTS
# --------------------------------------#


def print_all_shortcuts():
    """
    Prints all available shortcuts to data sets.
    """
    for ky in list(shortcuts.keys()):
        # Check if we are dealing with an index file
        if isinstance(shortcuts[ky], dict):
            print(
                f"{ky}: 'candl_data.{shortcuts[ky]['index']}' (index file)\n  Multiple variants available, access with index file (above) and 'variant' keyword or with specific shortcut for desired variant."
            )
            for subky in list(shortcuts[ky].keys()):
                if subky == "index":
                    continue
                info_str = ""
                if info[ky][subky]:
                    info_str = f" ({info[ky][subky]})"
                print(
                    f"  'variant = {subky}' or 'candl_data.{shortcuts[ky][subky]}'{info_str}\n  (data files located at: {globals()[shortcuts[ky][subky]]})"
                )
        else:
            print(
                f"{ky}: 'candl_data.{shortcuts[ky]}'\n  (data files located at: {globals()[shortcuts[ky]]})"
            )

# --------------------------------------#
# TESTS
# --------------------------------------#

def run_all_tests():
    """
    Runs all tests.
    See candl.test.run_test().
    """

    from candl.tests import run_test

    # Grab all test yaml files
    
    all_test_yaml_files = [
        f for f in os.listdir(f"{data_path}/tests/") if f.endswith(".yaml")
    ]

    # Loop over all tests
    for test_file in all_test_yaml_files:
        run_test(f"{data_path}/tests/{test_file}")
