
from pyteomics.mztab import MzTab


def read_mztab(path):
    mztab = MzTab(path)
    mtd = mztab.metadata
    prt = mztab.protein_table
    pep = mztab.peptide_table
    psm = mztab.spectrum_match_table
    sml = mztab.small_molecule_table
    return mtd, prt, pep, psm, sml


