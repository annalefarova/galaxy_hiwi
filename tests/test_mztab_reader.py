import os
import pandas
from mztab_processing.mztab_reader import read_mztab
from mztab_processing.column_filter_sml import column_filter_on_sml
 
def test_mztab_reader():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data", 
        "accurate_mass_search.mztab"
    )
    _, _, _, _, sml = read_mztab(file_path)
    assert sml.shape == (33464, 41)
    list_of_columns = ["identifier", "chemical_formula", "smiles", "description", "exp_mass_to_charge", "calc_mass_to_charge", "charge", "retention_time", "opt_global_id_group"]
    assert column_filter_on_sml(sml, list_of_columns).shape == (33464, 9)

