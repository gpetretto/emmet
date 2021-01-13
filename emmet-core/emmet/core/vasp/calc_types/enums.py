"""
Autogenerated Enums for VASP RunType, TaskType, and CalcType
Do not edit this by hand. Edit generate.py or run_types.yaml instead
"""
from emmet.core.utils import ValueEnum


class RunType(ValueEnum):
    """ VASP calculation run types """

    AM05 = "AM05"
    GGA = "GGA"
    PBE = "PBE"
    PBESol = "PBESol"
    RevPBE_PADE = "RevPBE+PADE"
    optB86b = "optB86b"
    optB88 = "optB88"
    optPBE = "optPBE"
    revPBE = "revPBE"
    B3LYP = "B3LYP"
    HF = "HF"
    HSE03 = "HSE03"
    HSE06 = "HSE06"
    PB0 = "PB0"
    M06L = "M06L"
    MBJL = "MBJL"
    MS0 = "MS0"
    MS1 = "MS1"
    MS2 = "MS2"
    RTPSS = "RTPSS"
    SCAN = "SCAN"
    TPSS = "TPSS"
    SCAN_rVV10 = "SCAN-rVV10"
    optB86b_vdW = "optB86b-vdW"
    optB88_vdW = "optB88-vdW"
    optPBE_vdW = "optPBE-vdW"
    rev_vdW_DF2 = "rev-vdW-DF2"
    revPBE_vdW = "revPBE-vdW"
    vdW_DF2 = "vdW-DF2"
    AM05_U = "AM05+U"
    GGA_U = "GGA+U"
    PBE_U = "PBE+U"
    PBESol_U = "PBESol+U"
    RevPBE_PADE_U = "RevPBE+PADE+U"
    optB86b_U = "optB86b+U"
    optB88_U = "optB88+U"
    optPBE_U = "optPBE+U"
    revPBE_U = "revPBE+U"
    B3LYP_U = "B3LYP+U"
    HF_U = "HF+U"
    HSE03_U = "HSE03+U"
    HSE06_U = "HSE06+U"
    PB0_U = "PB0+U"
    M06L_U = "M06L+U"
    MBJL_U = "MBJL+U"
    MS0_U = "MS0+U"
    MS1_U = "MS1+U"
    MS2_U = "MS2+U"
    RTPSS_U = "RTPSS+U"
    SCAN_U = "SCAN+U"
    TPSS_U = "TPSS+U"
    SCAN_rVV10_U = "SCAN-rVV10+U"
    optB86b_vdW_U = "optB86b-vdW+U"
    optB88_vdW_U = "optB88-vdW+U"
    optPBE_vdW_U = "optPBE-vdW+U"
    rev_vdW_DF2_U = "rev-vdW-DF2+U"
    revPBE_vdW_U = "revPBE-vdW+U"
    vdW_DF2_U = "vdW-DF2+U"
    LDA = "LDA"
    LDA_U = "LDA+U"


class TaskType(ValueEnum):
    """ VASP calculation task types """

    NSCF_Line = "NSCF Line"
    NSCF_Uniform = "NSCF Uniform"
    Dielectric = "Dielectric"
    DFPT = "DFPT"
    DFPT_Dielectric = "DFPT Dielectric"
    NMR_Nuclear_Shielding = "NMR Nuclear Shielding"
    NMR_Electric_Field_Gradient = "NMR Electric Field Gradient"
    Static = "Static"
    Structure_Optimization = "Structure Optimization"
    Deformation = "Deformation"


class CalcType(ValueEnum):
    """ VASP calculation types """

    AM05_NSCF_Line = "AM05 NSCF Line"
    AM05_NSCF_Uniform = "AM05 NSCF Uniform"
    AM05_Dielectric = "AM05 Dielectric"
    AM05_DFPT = "AM05 DFPT"
    AM05_DFPT_Dielectric = "AM05 DFPT Dielectric"
    AM05_NMR_Nuclear_Shielding = "AM05 NMR Nuclear Shielding"
    AM05_NMR_Electric_Field_Gradient = "AM05 NMR Electric Field Gradient"
    AM05_Static = "AM05 Static"
    AM05_Structure_Optimization = "AM05 Structure Optimization"
    AM05_Deformation = "AM05 Deformation"
    GGA_NSCF_Line = "GGA NSCF Line"
    GGA_NSCF_Uniform = "GGA NSCF Uniform"
    GGA_Dielectric = "GGA Dielectric"
    GGA_DFPT = "GGA DFPT"
    GGA_DFPT_Dielectric = "GGA DFPT Dielectric"
    GGA_NMR_Nuclear_Shielding = "GGA NMR Nuclear Shielding"
    GGA_NMR_Electric_Field_Gradient = "GGA NMR Electric Field Gradient"
    GGA_Static = "GGA Static"
    GGA_Structure_Optimization = "GGA Structure Optimization"
    GGA_Deformation = "GGA Deformation"
    PBE_NSCF_Line = "PBE NSCF Line"
    PBE_NSCF_Uniform = "PBE NSCF Uniform"
    PBE_Dielectric = "PBE Dielectric"
    PBE_DFPT = "PBE DFPT"
    PBE_DFPT_Dielectric = "PBE DFPT Dielectric"
    PBE_NMR_Nuclear_Shielding = "PBE NMR Nuclear Shielding"
    PBE_NMR_Electric_Field_Gradient = "PBE NMR Electric Field Gradient"
    PBE_Static = "PBE Static"
    PBE_Structure_Optimization = "PBE Structure Optimization"
    PBE_Deformation = "PBE Deformation"
    PBESol_NSCF_Line = "PBESol NSCF Line"
    PBESol_NSCF_Uniform = "PBESol NSCF Uniform"
    PBESol_Dielectric = "PBESol Dielectric"
    PBESol_DFPT = "PBESol DFPT"
    PBESol_DFPT_Dielectric = "PBESol DFPT Dielectric"
    PBESol_NMR_Nuclear_Shielding = "PBESol NMR Nuclear Shielding"
    PBESol_NMR_Electric_Field_Gradient = "PBESol NMR Electric Field Gradient"
    PBESol_Static = "PBESol Static"
    PBESol_Structure_Optimization = "PBESol Structure Optimization"
    PBESol_Deformation = "PBESol Deformation"
    RevPBE_PADE_NSCF_Line = "RevPBE+PADE NSCF Line"
    RevPBE_PADE_NSCF_Uniform = "RevPBE+PADE NSCF Uniform"
    RevPBE_PADE_Dielectric = "RevPBE+PADE Dielectric"
    RevPBE_PADE_DFPT = "RevPBE+PADE DFPT"
    RevPBE_PADE_DFPT_Dielectric = "RevPBE+PADE DFPT Dielectric"
    RevPBE_PADE_NMR_Nuclear_Shielding = "RevPBE+PADE NMR Nuclear Shielding"
    RevPBE_PADE_NMR_Electric_Field_Gradient = "RevPBE+PADE NMR Electric Field Gradient"
    RevPBE_PADE_Static = "RevPBE+PADE Static"
    RevPBE_PADE_Structure_Optimization = "RevPBE+PADE Structure Optimization"
    RevPBE_PADE_Deformation = "RevPBE+PADE Deformation"
    optB86b_NSCF_Line = "optB86b NSCF Line"
    optB86b_NSCF_Uniform = "optB86b NSCF Uniform"
    optB86b_Dielectric = "optB86b Dielectric"
    optB86b_DFPT = "optB86b DFPT"
    optB86b_DFPT_Dielectric = "optB86b DFPT Dielectric"
    optB86b_NMR_Nuclear_Shielding = "optB86b NMR Nuclear Shielding"
    optB86b_NMR_Electric_Field_Gradient = "optB86b NMR Electric Field Gradient"
    optB86b_Static = "optB86b Static"
    optB86b_Structure_Optimization = "optB86b Structure Optimization"
    optB86b_Deformation = "optB86b Deformation"
    optB88_NSCF_Line = "optB88 NSCF Line"
    optB88_NSCF_Uniform = "optB88 NSCF Uniform"
    optB88_Dielectric = "optB88 Dielectric"
    optB88_DFPT = "optB88 DFPT"
    optB88_DFPT_Dielectric = "optB88 DFPT Dielectric"
    optB88_NMR_Nuclear_Shielding = "optB88 NMR Nuclear Shielding"
    optB88_NMR_Electric_Field_Gradient = "optB88 NMR Electric Field Gradient"
    optB88_Static = "optB88 Static"
    optB88_Structure_Optimization = "optB88 Structure Optimization"
    optB88_Deformation = "optB88 Deformation"
    optPBE_NSCF_Line = "optPBE NSCF Line"
    optPBE_NSCF_Uniform = "optPBE NSCF Uniform"
    optPBE_Dielectric = "optPBE Dielectric"
    optPBE_DFPT = "optPBE DFPT"
    optPBE_DFPT_Dielectric = "optPBE DFPT Dielectric"
    optPBE_NMR_Nuclear_Shielding = "optPBE NMR Nuclear Shielding"
    optPBE_NMR_Electric_Field_Gradient = "optPBE NMR Electric Field Gradient"
    optPBE_Static = "optPBE Static"
    optPBE_Structure_Optimization = "optPBE Structure Optimization"
    optPBE_Deformation = "optPBE Deformation"
    revPBE_NSCF_Line = "revPBE NSCF Line"
    revPBE_NSCF_Uniform = "revPBE NSCF Uniform"
    revPBE_Dielectric = "revPBE Dielectric"
    revPBE_DFPT = "revPBE DFPT"
    revPBE_DFPT_Dielectric = "revPBE DFPT Dielectric"
    revPBE_NMR_Nuclear_Shielding = "revPBE NMR Nuclear Shielding"
    revPBE_NMR_Electric_Field_Gradient = "revPBE NMR Electric Field Gradient"
    revPBE_Static = "revPBE Static"
    revPBE_Structure_Optimization = "revPBE Structure Optimization"
    revPBE_Deformation = "revPBE Deformation"
    B3LYP_NSCF_Line = "B3LYP NSCF Line"
    B3LYP_NSCF_Uniform = "B3LYP NSCF Uniform"
    B3LYP_Dielectric = "B3LYP Dielectric"
    B3LYP_DFPT = "B3LYP DFPT"
    B3LYP_DFPT_Dielectric = "B3LYP DFPT Dielectric"
    B3LYP_NMR_Nuclear_Shielding = "B3LYP NMR Nuclear Shielding"
    B3LYP_NMR_Electric_Field_Gradient = "B3LYP NMR Electric Field Gradient"
    B3LYP_Static = "B3LYP Static"
    B3LYP_Structure_Optimization = "B3LYP Structure Optimization"
    B3LYP_Deformation = "B3LYP Deformation"
    HF_NSCF_Line = "HF NSCF Line"
    HF_NSCF_Uniform = "HF NSCF Uniform"
    HF_Dielectric = "HF Dielectric"
    HF_DFPT = "HF DFPT"
    HF_DFPT_Dielectric = "HF DFPT Dielectric"
    HF_NMR_Nuclear_Shielding = "HF NMR Nuclear Shielding"
    HF_NMR_Electric_Field_Gradient = "HF NMR Electric Field Gradient"
    HF_Static = "HF Static"
    HF_Structure_Optimization = "HF Structure Optimization"
    HF_Deformation = "HF Deformation"
    HSE03_NSCF_Line = "HSE03 NSCF Line"
    HSE03_NSCF_Uniform = "HSE03 NSCF Uniform"
    HSE03_Dielectric = "HSE03 Dielectric"
    HSE03_DFPT = "HSE03 DFPT"
    HSE03_DFPT_Dielectric = "HSE03 DFPT Dielectric"
    HSE03_NMR_Nuclear_Shielding = "HSE03 NMR Nuclear Shielding"
    HSE03_NMR_Electric_Field_Gradient = "HSE03 NMR Electric Field Gradient"
    HSE03_Static = "HSE03 Static"
    HSE03_Structure_Optimization = "HSE03 Structure Optimization"
    HSE03_Deformation = "HSE03 Deformation"
    HSE06_NSCF_Line = "HSE06 NSCF Line"
    HSE06_NSCF_Uniform = "HSE06 NSCF Uniform"
    HSE06_Dielectric = "HSE06 Dielectric"
    HSE06_DFPT = "HSE06 DFPT"
    HSE06_DFPT_Dielectric = "HSE06 DFPT Dielectric"
    HSE06_NMR_Nuclear_Shielding = "HSE06 NMR Nuclear Shielding"
    HSE06_NMR_Electric_Field_Gradient = "HSE06 NMR Electric Field Gradient"
    HSE06_Static = "HSE06 Static"
    HSE06_Structure_Optimization = "HSE06 Structure Optimization"
    HSE06_Deformation = "HSE06 Deformation"
    PB0_NSCF_Line = "PB0 NSCF Line"
    PB0_NSCF_Uniform = "PB0 NSCF Uniform"
    PB0_Dielectric = "PB0 Dielectric"
    PB0_DFPT = "PB0 DFPT"
    PB0_DFPT_Dielectric = "PB0 DFPT Dielectric"
    PB0_NMR_Nuclear_Shielding = "PB0 NMR Nuclear Shielding"
    PB0_NMR_Electric_Field_Gradient = "PB0 NMR Electric Field Gradient"
    PB0_Static = "PB0 Static"
    PB0_Structure_Optimization = "PB0 Structure Optimization"
    PB0_Deformation = "PB0 Deformation"
    M06L_NSCF_Line = "M06L NSCF Line"
    M06L_NSCF_Uniform = "M06L NSCF Uniform"
    M06L_Dielectric = "M06L Dielectric"
    M06L_DFPT = "M06L DFPT"
    M06L_DFPT_Dielectric = "M06L DFPT Dielectric"
    M06L_NMR_Nuclear_Shielding = "M06L NMR Nuclear Shielding"
    M06L_NMR_Electric_Field_Gradient = "M06L NMR Electric Field Gradient"
    M06L_Static = "M06L Static"
    M06L_Structure_Optimization = "M06L Structure Optimization"
    M06L_Deformation = "M06L Deformation"
    MBJL_NSCF_Line = "MBJL NSCF Line"
    MBJL_NSCF_Uniform = "MBJL NSCF Uniform"
    MBJL_Dielectric = "MBJL Dielectric"
    MBJL_DFPT = "MBJL DFPT"
    MBJL_DFPT_Dielectric = "MBJL DFPT Dielectric"
    MBJL_NMR_Nuclear_Shielding = "MBJL NMR Nuclear Shielding"
    MBJL_NMR_Electric_Field_Gradient = "MBJL NMR Electric Field Gradient"
    MBJL_Static = "MBJL Static"
    MBJL_Structure_Optimization = "MBJL Structure Optimization"
    MBJL_Deformation = "MBJL Deformation"
    MS0_NSCF_Line = "MS0 NSCF Line"
    MS0_NSCF_Uniform = "MS0 NSCF Uniform"
    MS0_Dielectric = "MS0 Dielectric"
    MS0_DFPT = "MS0 DFPT"
    MS0_DFPT_Dielectric = "MS0 DFPT Dielectric"
    MS0_NMR_Nuclear_Shielding = "MS0 NMR Nuclear Shielding"
    MS0_NMR_Electric_Field_Gradient = "MS0 NMR Electric Field Gradient"
    MS0_Static = "MS0 Static"
    MS0_Structure_Optimization = "MS0 Structure Optimization"
    MS0_Deformation = "MS0 Deformation"
    MS1_NSCF_Line = "MS1 NSCF Line"
    MS1_NSCF_Uniform = "MS1 NSCF Uniform"
    MS1_Dielectric = "MS1 Dielectric"
    MS1_DFPT = "MS1 DFPT"
    MS1_DFPT_Dielectric = "MS1 DFPT Dielectric"
    MS1_NMR_Nuclear_Shielding = "MS1 NMR Nuclear Shielding"
    MS1_NMR_Electric_Field_Gradient = "MS1 NMR Electric Field Gradient"
    MS1_Static = "MS1 Static"
    MS1_Structure_Optimization = "MS1 Structure Optimization"
    MS1_Deformation = "MS1 Deformation"
    MS2_NSCF_Line = "MS2 NSCF Line"
    MS2_NSCF_Uniform = "MS2 NSCF Uniform"
    MS2_Dielectric = "MS2 Dielectric"
    MS2_DFPT = "MS2 DFPT"
    MS2_DFPT_Dielectric = "MS2 DFPT Dielectric"
    MS2_NMR_Nuclear_Shielding = "MS2 NMR Nuclear Shielding"
    MS2_NMR_Electric_Field_Gradient = "MS2 NMR Electric Field Gradient"
    MS2_Static = "MS2 Static"
    MS2_Structure_Optimization = "MS2 Structure Optimization"
    MS2_Deformation = "MS2 Deformation"
    RTPSS_NSCF_Line = "RTPSS NSCF Line"
    RTPSS_NSCF_Uniform = "RTPSS NSCF Uniform"
    RTPSS_Dielectric = "RTPSS Dielectric"
    RTPSS_DFPT = "RTPSS DFPT"
    RTPSS_DFPT_Dielectric = "RTPSS DFPT Dielectric"
    RTPSS_NMR_Nuclear_Shielding = "RTPSS NMR Nuclear Shielding"
    RTPSS_NMR_Electric_Field_Gradient = "RTPSS NMR Electric Field Gradient"
    RTPSS_Static = "RTPSS Static"
    RTPSS_Structure_Optimization = "RTPSS Structure Optimization"
    RTPSS_Deformation = "RTPSS Deformation"
    SCAN_NSCF_Line = "SCAN NSCF Line"
    SCAN_NSCF_Uniform = "SCAN NSCF Uniform"
    SCAN_Dielectric = "SCAN Dielectric"
    SCAN_DFPT = "SCAN DFPT"
    SCAN_DFPT_Dielectric = "SCAN DFPT Dielectric"
    SCAN_NMR_Nuclear_Shielding = "SCAN NMR Nuclear Shielding"
    SCAN_NMR_Electric_Field_Gradient = "SCAN NMR Electric Field Gradient"
    SCAN_Static = "SCAN Static"
    SCAN_Structure_Optimization = "SCAN Structure Optimization"
    SCAN_Deformation = "SCAN Deformation"
    TPSS_NSCF_Line = "TPSS NSCF Line"
    TPSS_NSCF_Uniform = "TPSS NSCF Uniform"
    TPSS_Dielectric = "TPSS Dielectric"
    TPSS_DFPT = "TPSS DFPT"
    TPSS_DFPT_Dielectric = "TPSS DFPT Dielectric"
    TPSS_NMR_Nuclear_Shielding = "TPSS NMR Nuclear Shielding"
    TPSS_NMR_Electric_Field_Gradient = "TPSS NMR Electric Field Gradient"
    TPSS_Static = "TPSS Static"
    TPSS_Structure_Optimization = "TPSS Structure Optimization"
    TPSS_Deformation = "TPSS Deformation"
    SCAN_rVV10_NSCF_Line = "SCAN-rVV10 NSCF Line"
    SCAN_rVV10_NSCF_Uniform = "SCAN-rVV10 NSCF Uniform"
    SCAN_rVV10_Dielectric = "SCAN-rVV10 Dielectric"
    SCAN_rVV10_DFPT = "SCAN-rVV10 DFPT"
    SCAN_rVV10_DFPT_Dielectric = "SCAN-rVV10 DFPT Dielectric"
    SCAN_rVV10_NMR_Nuclear_Shielding = "SCAN-rVV10 NMR Nuclear Shielding"
    SCAN_rVV10_NMR_Electric_Field_Gradient = "SCAN-rVV10 NMR Electric Field Gradient"
    SCAN_rVV10_Static = "SCAN-rVV10 Static"
    SCAN_rVV10_Structure_Optimization = "SCAN-rVV10 Structure Optimization"
    SCAN_rVV10_Deformation = "SCAN-rVV10 Deformation"
    optB86b_vdW_NSCF_Line = "optB86b-vdW NSCF Line"
    optB86b_vdW_NSCF_Uniform = "optB86b-vdW NSCF Uniform"
    optB86b_vdW_Dielectric = "optB86b-vdW Dielectric"
    optB86b_vdW_DFPT = "optB86b-vdW DFPT"
    optB86b_vdW_DFPT_Dielectric = "optB86b-vdW DFPT Dielectric"
    optB86b_vdW_NMR_Nuclear_Shielding = "optB86b-vdW NMR Nuclear Shielding"
    optB86b_vdW_NMR_Electric_Field_Gradient = "optB86b-vdW NMR Electric Field Gradient"
    optB86b_vdW_Static = "optB86b-vdW Static"
    optB86b_vdW_Structure_Optimization = "optB86b-vdW Structure Optimization"
    optB86b_vdW_Deformation = "optB86b-vdW Deformation"
    optB88_vdW_NSCF_Line = "optB88-vdW NSCF Line"
    optB88_vdW_NSCF_Uniform = "optB88-vdW NSCF Uniform"
    optB88_vdW_Dielectric = "optB88-vdW Dielectric"
    optB88_vdW_DFPT = "optB88-vdW DFPT"
    optB88_vdW_DFPT_Dielectric = "optB88-vdW DFPT Dielectric"
    optB88_vdW_NMR_Nuclear_Shielding = "optB88-vdW NMR Nuclear Shielding"
    optB88_vdW_NMR_Electric_Field_Gradient = "optB88-vdW NMR Electric Field Gradient"
    optB88_vdW_Static = "optB88-vdW Static"
    optB88_vdW_Structure_Optimization = "optB88-vdW Structure Optimization"
    optB88_vdW_Deformation = "optB88-vdW Deformation"
    optPBE_vdW_NSCF_Line = "optPBE-vdW NSCF Line"
    optPBE_vdW_NSCF_Uniform = "optPBE-vdW NSCF Uniform"
    optPBE_vdW_Dielectric = "optPBE-vdW Dielectric"
    optPBE_vdW_DFPT = "optPBE-vdW DFPT"
    optPBE_vdW_DFPT_Dielectric = "optPBE-vdW DFPT Dielectric"
    optPBE_vdW_NMR_Nuclear_Shielding = "optPBE-vdW NMR Nuclear Shielding"
    optPBE_vdW_NMR_Electric_Field_Gradient = "optPBE-vdW NMR Electric Field Gradient"
    optPBE_vdW_Static = "optPBE-vdW Static"
    optPBE_vdW_Structure_Optimization = "optPBE-vdW Structure Optimization"
    optPBE_vdW_Deformation = "optPBE-vdW Deformation"
    rev_vdW_DF2_NSCF_Line = "rev-vdW-DF2 NSCF Line"
    rev_vdW_DF2_NSCF_Uniform = "rev-vdW-DF2 NSCF Uniform"
    rev_vdW_DF2_Dielectric = "rev-vdW-DF2 Dielectric"
    rev_vdW_DF2_DFPT = "rev-vdW-DF2 DFPT"
    rev_vdW_DF2_DFPT_Dielectric = "rev-vdW-DF2 DFPT Dielectric"
    rev_vdW_DF2_NMR_Nuclear_Shielding = "rev-vdW-DF2 NMR Nuclear Shielding"
    rev_vdW_DF2_NMR_Electric_Field_Gradient = "rev-vdW-DF2 NMR Electric Field Gradient"
    rev_vdW_DF2_Static = "rev-vdW-DF2 Static"
    rev_vdW_DF2_Structure_Optimization = "rev-vdW-DF2 Structure Optimization"
    rev_vdW_DF2_Deformation = "rev-vdW-DF2 Deformation"
    revPBE_vdW_NSCF_Line = "revPBE-vdW NSCF Line"
    revPBE_vdW_NSCF_Uniform = "revPBE-vdW NSCF Uniform"
    revPBE_vdW_Dielectric = "revPBE-vdW Dielectric"
    revPBE_vdW_DFPT = "revPBE-vdW DFPT"
    revPBE_vdW_DFPT_Dielectric = "revPBE-vdW DFPT Dielectric"
    revPBE_vdW_NMR_Nuclear_Shielding = "revPBE-vdW NMR Nuclear Shielding"
    revPBE_vdW_NMR_Electric_Field_Gradient = "revPBE-vdW NMR Electric Field Gradient"
    revPBE_vdW_Static = "revPBE-vdW Static"
    revPBE_vdW_Structure_Optimization = "revPBE-vdW Structure Optimization"
    revPBE_vdW_Deformation = "revPBE-vdW Deformation"
    vdW_DF2_NSCF_Line = "vdW-DF2 NSCF Line"
    vdW_DF2_NSCF_Uniform = "vdW-DF2 NSCF Uniform"
    vdW_DF2_Dielectric = "vdW-DF2 Dielectric"
    vdW_DF2_DFPT = "vdW-DF2 DFPT"
    vdW_DF2_DFPT_Dielectric = "vdW-DF2 DFPT Dielectric"
    vdW_DF2_NMR_Nuclear_Shielding = "vdW-DF2 NMR Nuclear Shielding"
    vdW_DF2_NMR_Electric_Field_Gradient = "vdW-DF2 NMR Electric Field Gradient"
    vdW_DF2_Static = "vdW-DF2 Static"
    vdW_DF2_Structure_Optimization = "vdW-DF2 Structure Optimization"
    vdW_DF2_Deformation = "vdW-DF2 Deformation"
    AM05_U_NSCF_Line = "AM05+U NSCF Line"
    AM05_U_NSCF_Uniform = "AM05+U NSCF Uniform"
    AM05_U_Dielectric = "AM05+U Dielectric"
    AM05_U_DFPT = "AM05+U DFPT"
    AM05_U_DFPT_Dielectric = "AM05+U DFPT Dielectric"
    AM05_U_NMR_Nuclear_Shielding = "AM05+U NMR Nuclear Shielding"
    AM05_U_NMR_Electric_Field_Gradient = "AM05+U NMR Electric Field Gradient"
    AM05_U_Static = "AM05+U Static"
    AM05_U_Structure_Optimization = "AM05+U Structure Optimization"
    AM05_U_Deformation = "AM05+U Deformation"
    GGA_U_NSCF_Line = "GGA+U NSCF Line"
    GGA_U_NSCF_Uniform = "GGA+U NSCF Uniform"
    GGA_U_Dielectric = "GGA+U Dielectric"
    GGA_U_DFPT = "GGA+U DFPT"
    GGA_U_DFPT_Dielectric = "GGA+U DFPT Dielectric"
    GGA_U_NMR_Nuclear_Shielding = "GGA+U NMR Nuclear Shielding"
    GGA_U_NMR_Electric_Field_Gradient = "GGA+U NMR Electric Field Gradient"
    GGA_U_Static = "GGA+U Static"
    GGA_U_Structure_Optimization = "GGA+U Structure Optimization"
    GGA_U_Deformation = "GGA+U Deformation"
    PBE_U_NSCF_Line = "PBE+U NSCF Line"
    PBE_U_NSCF_Uniform = "PBE+U NSCF Uniform"
    PBE_U_Dielectric = "PBE+U Dielectric"
    PBE_U_DFPT = "PBE+U DFPT"
    PBE_U_DFPT_Dielectric = "PBE+U DFPT Dielectric"
    PBE_U_NMR_Nuclear_Shielding = "PBE+U NMR Nuclear Shielding"
    PBE_U_NMR_Electric_Field_Gradient = "PBE+U NMR Electric Field Gradient"
    PBE_U_Static = "PBE+U Static"
    PBE_U_Structure_Optimization = "PBE+U Structure Optimization"
    PBE_U_Deformation = "PBE+U Deformation"
    PBESol_U_NSCF_Line = "PBESol+U NSCF Line"
    PBESol_U_NSCF_Uniform = "PBESol+U NSCF Uniform"
    PBESol_U_Dielectric = "PBESol+U Dielectric"
    PBESol_U_DFPT = "PBESol+U DFPT"
    PBESol_U_DFPT_Dielectric = "PBESol+U DFPT Dielectric"
    PBESol_U_NMR_Nuclear_Shielding = "PBESol+U NMR Nuclear Shielding"
    PBESol_U_NMR_Electric_Field_Gradient = "PBESol+U NMR Electric Field Gradient"
    PBESol_U_Static = "PBESol+U Static"
    PBESol_U_Structure_Optimization = "PBESol+U Structure Optimization"
    PBESol_U_Deformation = "PBESol+U Deformation"
    RevPBE_PADE_U_NSCF_Line = "RevPBE+PADE+U NSCF Line"
    RevPBE_PADE_U_NSCF_Uniform = "RevPBE+PADE+U NSCF Uniform"
    RevPBE_PADE_U_Dielectric = "RevPBE+PADE+U Dielectric"
    RevPBE_PADE_U_DFPT = "RevPBE+PADE+U DFPT"
    RevPBE_PADE_U_DFPT_Dielectric = "RevPBE+PADE+U DFPT Dielectric"
    RevPBE_PADE_U_NMR_Nuclear_Shielding = "RevPBE+PADE+U NMR Nuclear Shielding"
    RevPBE_PADE_U_NMR_Electric_Field_Gradient = (
        "RevPBE+PADE+U NMR Electric Field Gradient"
    )
    RevPBE_PADE_U_Static = "RevPBE+PADE+U Static"
    RevPBE_PADE_U_Structure_Optimization = "RevPBE+PADE+U Structure Optimization"
    RevPBE_PADE_U_Deformation = "RevPBE+PADE+U Deformation"
    optB86b_U_NSCF_Line = "optB86b+U NSCF Line"
    optB86b_U_NSCF_Uniform = "optB86b+U NSCF Uniform"
    optB86b_U_Dielectric = "optB86b+U Dielectric"
    optB86b_U_DFPT = "optB86b+U DFPT"
    optB86b_U_DFPT_Dielectric = "optB86b+U DFPT Dielectric"
    optB86b_U_NMR_Nuclear_Shielding = "optB86b+U NMR Nuclear Shielding"
    optB86b_U_NMR_Electric_Field_Gradient = "optB86b+U NMR Electric Field Gradient"
    optB86b_U_Static = "optB86b+U Static"
    optB86b_U_Structure_Optimization = "optB86b+U Structure Optimization"
    optB86b_U_Deformation = "optB86b+U Deformation"
    optB88_U_NSCF_Line = "optB88+U NSCF Line"
    optB88_U_NSCF_Uniform = "optB88+U NSCF Uniform"
    optB88_U_Dielectric = "optB88+U Dielectric"
    optB88_U_DFPT = "optB88+U DFPT"
    optB88_U_DFPT_Dielectric = "optB88+U DFPT Dielectric"
    optB88_U_NMR_Nuclear_Shielding = "optB88+U NMR Nuclear Shielding"
    optB88_U_NMR_Electric_Field_Gradient = "optB88+U NMR Electric Field Gradient"
    optB88_U_Static = "optB88+U Static"
    optB88_U_Structure_Optimization = "optB88+U Structure Optimization"
    optB88_U_Deformation = "optB88+U Deformation"
    optPBE_U_NSCF_Line = "optPBE+U NSCF Line"
    optPBE_U_NSCF_Uniform = "optPBE+U NSCF Uniform"
    optPBE_U_Dielectric = "optPBE+U Dielectric"
    optPBE_U_DFPT = "optPBE+U DFPT"
    optPBE_U_DFPT_Dielectric = "optPBE+U DFPT Dielectric"
    optPBE_U_NMR_Nuclear_Shielding = "optPBE+U NMR Nuclear Shielding"
    optPBE_U_NMR_Electric_Field_Gradient = "optPBE+U NMR Electric Field Gradient"
    optPBE_U_Static = "optPBE+U Static"
    optPBE_U_Structure_Optimization = "optPBE+U Structure Optimization"
    optPBE_U_Deformation = "optPBE+U Deformation"
    revPBE_U_NSCF_Line = "revPBE+U NSCF Line"
    revPBE_U_NSCF_Uniform = "revPBE+U NSCF Uniform"
    revPBE_U_Dielectric = "revPBE+U Dielectric"
    revPBE_U_DFPT = "revPBE+U DFPT"
    revPBE_U_DFPT_Dielectric = "revPBE+U DFPT Dielectric"
    revPBE_U_NMR_Nuclear_Shielding = "revPBE+U NMR Nuclear Shielding"
    revPBE_U_NMR_Electric_Field_Gradient = "revPBE+U NMR Electric Field Gradient"
    revPBE_U_Static = "revPBE+U Static"
    revPBE_U_Structure_Optimization = "revPBE+U Structure Optimization"
    revPBE_U_Deformation = "revPBE+U Deformation"
    B3LYP_U_NSCF_Line = "B3LYP+U NSCF Line"
    B3LYP_U_NSCF_Uniform = "B3LYP+U NSCF Uniform"
    B3LYP_U_Dielectric = "B3LYP+U Dielectric"
    B3LYP_U_DFPT = "B3LYP+U DFPT"
    B3LYP_U_DFPT_Dielectric = "B3LYP+U DFPT Dielectric"
    B3LYP_U_NMR_Nuclear_Shielding = "B3LYP+U NMR Nuclear Shielding"
    B3LYP_U_NMR_Electric_Field_Gradient = "B3LYP+U NMR Electric Field Gradient"
    B3LYP_U_Static = "B3LYP+U Static"
    B3LYP_U_Structure_Optimization = "B3LYP+U Structure Optimization"
    B3LYP_U_Deformation = "B3LYP+U Deformation"
    HF_U_NSCF_Line = "HF+U NSCF Line"
    HF_U_NSCF_Uniform = "HF+U NSCF Uniform"
    HF_U_Dielectric = "HF+U Dielectric"
    HF_U_DFPT = "HF+U DFPT"
    HF_U_DFPT_Dielectric = "HF+U DFPT Dielectric"
    HF_U_NMR_Nuclear_Shielding = "HF+U NMR Nuclear Shielding"
    HF_U_NMR_Electric_Field_Gradient = "HF+U NMR Electric Field Gradient"
    HF_U_Static = "HF+U Static"
    HF_U_Structure_Optimization = "HF+U Structure Optimization"
    HF_U_Deformation = "HF+U Deformation"
    HSE03_U_NSCF_Line = "HSE03+U NSCF Line"
    HSE03_U_NSCF_Uniform = "HSE03+U NSCF Uniform"
    HSE03_U_Dielectric = "HSE03+U Dielectric"
    HSE03_U_DFPT = "HSE03+U DFPT"
    HSE03_U_DFPT_Dielectric = "HSE03+U DFPT Dielectric"
    HSE03_U_NMR_Nuclear_Shielding = "HSE03+U NMR Nuclear Shielding"
    HSE03_U_NMR_Electric_Field_Gradient = "HSE03+U NMR Electric Field Gradient"
    HSE03_U_Static = "HSE03+U Static"
    HSE03_U_Structure_Optimization = "HSE03+U Structure Optimization"
    HSE03_U_Deformation = "HSE03+U Deformation"
    HSE06_U_NSCF_Line = "HSE06+U NSCF Line"
    HSE06_U_NSCF_Uniform = "HSE06+U NSCF Uniform"
    HSE06_U_Dielectric = "HSE06+U Dielectric"
    HSE06_U_DFPT = "HSE06+U DFPT"
    HSE06_U_DFPT_Dielectric = "HSE06+U DFPT Dielectric"
    HSE06_U_NMR_Nuclear_Shielding = "HSE06+U NMR Nuclear Shielding"
    HSE06_U_NMR_Electric_Field_Gradient = "HSE06+U NMR Electric Field Gradient"
    HSE06_U_Static = "HSE06+U Static"
    HSE06_U_Structure_Optimization = "HSE06+U Structure Optimization"
    HSE06_U_Deformation = "HSE06+U Deformation"
    PB0_U_NSCF_Line = "PB0+U NSCF Line"
    PB0_U_NSCF_Uniform = "PB0+U NSCF Uniform"
    PB0_U_Dielectric = "PB0+U Dielectric"
    PB0_U_DFPT = "PB0+U DFPT"
    PB0_U_DFPT_Dielectric = "PB0+U DFPT Dielectric"
    PB0_U_NMR_Nuclear_Shielding = "PB0+U NMR Nuclear Shielding"
    PB0_U_NMR_Electric_Field_Gradient = "PB0+U NMR Electric Field Gradient"
    PB0_U_Static = "PB0+U Static"
    PB0_U_Structure_Optimization = "PB0+U Structure Optimization"
    PB0_U_Deformation = "PB0+U Deformation"
    M06L_U_NSCF_Line = "M06L+U NSCF Line"
    M06L_U_NSCF_Uniform = "M06L+U NSCF Uniform"
    M06L_U_Dielectric = "M06L+U Dielectric"
    M06L_U_DFPT = "M06L+U DFPT"
    M06L_U_DFPT_Dielectric = "M06L+U DFPT Dielectric"
    M06L_U_NMR_Nuclear_Shielding = "M06L+U NMR Nuclear Shielding"
    M06L_U_NMR_Electric_Field_Gradient = "M06L+U NMR Electric Field Gradient"
    M06L_U_Static = "M06L+U Static"
    M06L_U_Structure_Optimization = "M06L+U Structure Optimization"
    M06L_U_Deformation = "M06L+U Deformation"
    MBJL_U_NSCF_Line = "MBJL+U NSCF Line"
    MBJL_U_NSCF_Uniform = "MBJL+U NSCF Uniform"
    MBJL_U_Dielectric = "MBJL+U Dielectric"
    MBJL_U_DFPT = "MBJL+U DFPT"
    MBJL_U_DFPT_Dielectric = "MBJL+U DFPT Dielectric"
    MBJL_U_NMR_Nuclear_Shielding = "MBJL+U NMR Nuclear Shielding"
    MBJL_U_NMR_Electric_Field_Gradient = "MBJL+U NMR Electric Field Gradient"
    MBJL_U_Static = "MBJL+U Static"
    MBJL_U_Structure_Optimization = "MBJL+U Structure Optimization"
    MBJL_U_Deformation = "MBJL+U Deformation"
    MS0_U_NSCF_Line = "MS0+U NSCF Line"
    MS0_U_NSCF_Uniform = "MS0+U NSCF Uniform"
    MS0_U_Dielectric = "MS0+U Dielectric"
    MS0_U_DFPT = "MS0+U DFPT"
    MS0_U_DFPT_Dielectric = "MS0+U DFPT Dielectric"
    MS0_U_NMR_Nuclear_Shielding = "MS0+U NMR Nuclear Shielding"
    MS0_U_NMR_Electric_Field_Gradient = "MS0+U NMR Electric Field Gradient"
    MS0_U_Static = "MS0+U Static"
    MS0_U_Structure_Optimization = "MS0+U Structure Optimization"
    MS0_U_Deformation = "MS0+U Deformation"
    MS1_U_NSCF_Line = "MS1+U NSCF Line"
    MS1_U_NSCF_Uniform = "MS1+U NSCF Uniform"
    MS1_U_Dielectric = "MS1+U Dielectric"
    MS1_U_DFPT = "MS1+U DFPT"
    MS1_U_DFPT_Dielectric = "MS1+U DFPT Dielectric"
    MS1_U_NMR_Nuclear_Shielding = "MS1+U NMR Nuclear Shielding"
    MS1_U_NMR_Electric_Field_Gradient = "MS1+U NMR Electric Field Gradient"
    MS1_U_Static = "MS1+U Static"
    MS1_U_Structure_Optimization = "MS1+U Structure Optimization"
    MS1_U_Deformation = "MS1+U Deformation"
    MS2_U_NSCF_Line = "MS2+U NSCF Line"
    MS2_U_NSCF_Uniform = "MS2+U NSCF Uniform"
    MS2_U_Dielectric = "MS2+U Dielectric"
    MS2_U_DFPT = "MS2+U DFPT"
    MS2_U_DFPT_Dielectric = "MS2+U DFPT Dielectric"
    MS2_U_NMR_Nuclear_Shielding = "MS2+U NMR Nuclear Shielding"
    MS2_U_NMR_Electric_Field_Gradient = "MS2+U NMR Electric Field Gradient"
    MS2_U_Static = "MS2+U Static"
    MS2_U_Structure_Optimization = "MS2+U Structure Optimization"
    MS2_U_Deformation = "MS2+U Deformation"
    RTPSS_U_NSCF_Line = "RTPSS+U NSCF Line"
    RTPSS_U_NSCF_Uniform = "RTPSS+U NSCF Uniform"
    RTPSS_U_Dielectric = "RTPSS+U Dielectric"
    RTPSS_U_DFPT = "RTPSS+U DFPT"
    RTPSS_U_DFPT_Dielectric = "RTPSS+U DFPT Dielectric"
    RTPSS_U_NMR_Nuclear_Shielding = "RTPSS+U NMR Nuclear Shielding"
    RTPSS_U_NMR_Electric_Field_Gradient = "RTPSS+U NMR Electric Field Gradient"
    RTPSS_U_Static = "RTPSS+U Static"
    RTPSS_U_Structure_Optimization = "RTPSS+U Structure Optimization"
    RTPSS_U_Deformation = "RTPSS+U Deformation"
    SCAN_U_NSCF_Line = "SCAN+U NSCF Line"
    SCAN_U_NSCF_Uniform = "SCAN+U NSCF Uniform"
    SCAN_U_Dielectric = "SCAN+U Dielectric"
    SCAN_U_DFPT = "SCAN+U DFPT"
    SCAN_U_DFPT_Dielectric = "SCAN+U DFPT Dielectric"
    SCAN_U_NMR_Nuclear_Shielding = "SCAN+U NMR Nuclear Shielding"
    SCAN_U_NMR_Electric_Field_Gradient = "SCAN+U NMR Electric Field Gradient"
    SCAN_U_Static = "SCAN+U Static"
    SCAN_U_Structure_Optimization = "SCAN+U Structure Optimization"
    SCAN_U_Deformation = "SCAN+U Deformation"
    TPSS_U_NSCF_Line = "TPSS+U NSCF Line"
    TPSS_U_NSCF_Uniform = "TPSS+U NSCF Uniform"
    TPSS_U_Dielectric = "TPSS+U Dielectric"
    TPSS_U_DFPT = "TPSS+U DFPT"
    TPSS_U_DFPT_Dielectric = "TPSS+U DFPT Dielectric"
    TPSS_U_NMR_Nuclear_Shielding = "TPSS+U NMR Nuclear Shielding"
    TPSS_U_NMR_Electric_Field_Gradient = "TPSS+U NMR Electric Field Gradient"
    TPSS_U_Static = "TPSS+U Static"
    TPSS_U_Structure_Optimization = "TPSS+U Structure Optimization"
    TPSS_U_Deformation = "TPSS+U Deformation"
    SCAN_rVV10_U_NSCF_Line = "SCAN-rVV10+U NSCF Line"
    SCAN_rVV10_U_NSCF_Uniform = "SCAN-rVV10+U NSCF Uniform"
    SCAN_rVV10_U_Dielectric = "SCAN-rVV10+U Dielectric"
    SCAN_rVV10_U_DFPT = "SCAN-rVV10+U DFPT"
    SCAN_rVV10_U_DFPT_Dielectric = "SCAN-rVV10+U DFPT Dielectric"
    SCAN_rVV10_U_NMR_Nuclear_Shielding = "SCAN-rVV10+U NMR Nuclear Shielding"
    SCAN_rVV10_U_NMR_Electric_Field_Gradient = (
        "SCAN-rVV10+U NMR Electric Field Gradient"
    )
    SCAN_rVV10_U_Static = "SCAN-rVV10+U Static"
    SCAN_rVV10_U_Structure_Optimization = "SCAN-rVV10+U Structure Optimization"
    SCAN_rVV10_U_Deformation = "SCAN-rVV10+U Deformation"
    optB86b_vdW_U_NSCF_Line = "optB86b-vdW+U NSCF Line"
    optB86b_vdW_U_NSCF_Uniform = "optB86b-vdW+U NSCF Uniform"
    optB86b_vdW_U_Dielectric = "optB86b-vdW+U Dielectric"
    optB86b_vdW_U_DFPT = "optB86b-vdW+U DFPT"
    optB86b_vdW_U_DFPT_Dielectric = "optB86b-vdW+U DFPT Dielectric"
    optB86b_vdW_U_NMR_Nuclear_Shielding = "optB86b-vdW+U NMR Nuclear Shielding"
    optB86b_vdW_U_NMR_Electric_Field_Gradient = (
        "optB86b-vdW+U NMR Electric Field Gradient"
    )
    optB86b_vdW_U_Static = "optB86b-vdW+U Static"
    optB86b_vdW_U_Structure_Optimization = "optB86b-vdW+U Structure Optimization"
    optB86b_vdW_U_Deformation = "optB86b-vdW+U Deformation"
    optB88_vdW_U_NSCF_Line = "optB88-vdW+U NSCF Line"
    optB88_vdW_U_NSCF_Uniform = "optB88-vdW+U NSCF Uniform"
    optB88_vdW_U_Dielectric = "optB88-vdW+U Dielectric"
    optB88_vdW_U_DFPT = "optB88-vdW+U DFPT"
    optB88_vdW_U_DFPT_Dielectric = "optB88-vdW+U DFPT Dielectric"
    optB88_vdW_U_NMR_Nuclear_Shielding = "optB88-vdW+U NMR Nuclear Shielding"
    optB88_vdW_U_NMR_Electric_Field_Gradient = (
        "optB88-vdW+U NMR Electric Field Gradient"
    )
    optB88_vdW_U_Static = "optB88-vdW+U Static"
    optB88_vdW_U_Structure_Optimization = "optB88-vdW+U Structure Optimization"
    optB88_vdW_U_Deformation = "optB88-vdW+U Deformation"
    optPBE_vdW_U_NSCF_Line = "optPBE-vdW+U NSCF Line"
    optPBE_vdW_U_NSCF_Uniform = "optPBE-vdW+U NSCF Uniform"
    optPBE_vdW_U_Dielectric = "optPBE-vdW+U Dielectric"
    optPBE_vdW_U_DFPT = "optPBE-vdW+U DFPT"
    optPBE_vdW_U_DFPT_Dielectric = "optPBE-vdW+U DFPT Dielectric"
    optPBE_vdW_U_NMR_Nuclear_Shielding = "optPBE-vdW+U NMR Nuclear Shielding"
    optPBE_vdW_U_NMR_Electric_Field_Gradient = (
        "optPBE-vdW+U NMR Electric Field Gradient"
    )
    optPBE_vdW_U_Static = "optPBE-vdW+U Static"
    optPBE_vdW_U_Structure_Optimization = "optPBE-vdW+U Structure Optimization"
    optPBE_vdW_U_Deformation = "optPBE-vdW+U Deformation"
    rev_vdW_DF2_U_NSCF_Line = "rev-vdW-DF2+U NSCF Line"
    rev_vdW_DF2_U_NSCF_Uniform = "rev-vdW-DF2+U NSCF Uniform"
    rev_vdW_DF2_U_Dielectric = "rev-vdW-DF2+U Dielectric"
    rev_vdW_DF2_U_DFPT = "rev-vdW-DF2+U DFPT"
    rev_vdW_DF2_U_DFPT_Dielectric = "rev-vdW-DF2+U DFPT Dielectric"
    rev_vdW_DF2_U_NMR_Nuclear_Shielding = "rev-vdW-DF2+U NMR Nuclear Shielding"
    rev_vdW_DF2_U_NMR_Electric_Field_Gradient = (
        "rev-vdW-DF2+U NMR Electric Field Gradient"
    )
    rev_vdW_DF2_U_Static = "rev-vdW-DF2+U Static"
    rev_vdW_DF2_U_Structure_Optimization = "rev-vdW-DF2+U Structure Optimization"
    rev_vdW_DF2_U_Deformation = "rev-vdW-DF2+U Deformation"
    revPBE_vdW_U_NSCF_Line = "revPBE-vdW+U NSCF Line"
    revPBE_vdW_U_NSCF_Uniform = "revPBE-vdW+U NSCF Uniform"
    revPBE_vdW_U_Dielectric = "revPBE-vdW+U Dielectric"
    revPBE_vdW_U_DFPT = "revPBE-vdW+U DFPT"
    revPBE_vdW_U_DFPT_Dielectric = "revPBE-vdW+U DFPT Dielectric"
    revPBE_vdW_U_NMR_Nuclear_Shielding = "revPBE-vdW+U NMR Nuclear Shielding"
    revPBE_vdW_U_NMR_Electric_Field_Gradient = (
        "revPBE-vdW+U NMR Electric Field Gradient"
    )
    revPBE_vdW_U_Static = "revPBE-vdW+U Static"
    revPBE_vdW_U_Structure_Optimization = "revPBE-vdW+U Structure Optimization"
    revPBE_vdW_U_Deformation = "revPBE-vdW+U Deformation"
    vdW_DF2_U_NSCF_Line = "vdW-DF2+U NSCF Line"
    vdW_DF2_U_NSCF_Uniform = "vdW-DF2+U NSCF Uniform"
    vdW_DF2_U_Dielectric = "vdW-DF2+U Dielectric"
    vdW_DF2_U_DFPT = "vdW-DF2+U DFPT"
    vdW_DF2_U_DFPT_Dielectric = "vdW-DF2+U DFPT Dielectric"
    vdW_DF2_U_NMR_Nuclear_Shielding = "vdW-DF2+U NMR Nuclear Shielding"
    vdW_DF2_U_NMR_Electric_Field_Gradient = "vdW-DF2+U NMR Electric Field Gradient"
    vdW_DF2_U_Static = "vdW-DF2+U Static"
    vdW_DF2_U_Structure_Optimization = "vdW-DF2+U Structure Optimization"
    vdW_DF2_U_Deformation = "vdW-DF2+U Deformation"
    LDA_NSCF_Line = "LDA NSCF Line"
    LDA_NSCF_Uniform = "LDA NSCF Uniform"
    LDA_Dielectric = "LDA Dielectric"
    LDA_DFPT = "LDA DFPT"
    LDA_DFPT_Dielectric = "LDA DFPT Dielectric"
    LDA_NMR_Nuclear_Shielding = "LDA NMR Nuclear Shielding"
    LDA_NMR_Electric_Field_Gradient = "LDA NMR Electric Field Gradient"
    LDA_Static = "LDA Static"
    LDA_Structure_Optimization = "LDA Structure Optimization"
    LDA_Deformation = "LDA Deformation"
    LDA_U_NSCF_Line = "LDA+U NSCF Line"
    LDA_U_NSCF_Uniform = "LDA+U NSCF Uniform"
    LDA_U_Dielectric = "LDA+U Dielectric"
    LDA_U_DFPT = "LDA+U DFPT"
    LDA_U_DFPT_Dielectric = "LDA+U DFPT Dielectric"
    LDA_U_NMR_Nuclear_Shielding = "LDA+U NMR Nuclear Shielding"
    LDA_U_NMR_Electric_Field_Gradient = "LDA+U NMR Electric Field Gradient"
    LDA_U_Static = "LDA+U Static"
    LDA_U_Structure_Optimization = "LDA+U Structure Optimization"
    LDA_U_Deformation = "LDA+U Deformation"
