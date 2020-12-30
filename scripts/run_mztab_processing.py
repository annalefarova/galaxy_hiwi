import os
from mztab_processing.mztab_reader import read_mztab
from mztab_processing.column_filter_sml import column_filter_on_sml


if __name__ == "__main__":
    file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data", 
        "accurate_mass_search.mztab"
    )

    _, _, _, _, sml = read_mztab(file_path)
    #run mztab_reader
    print(sml)

    list_of_columns = ["identifier", "chemical_formula", "smiles", "description", "exp_mass_to_charge", "calc_mass_to_charge", "charge", "retention_time", "opt_global_id_group"]
    #run column_filter_sml
    print(column_filter_on_sml(sml, list_of_columns))
