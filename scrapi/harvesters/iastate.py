'''
Harvester for the Digital Repository @ Iowa State University for the SHARE project

Example API call: http://lib.dr.iastate.edu/do/oai/?verb=ListRecords&metadataPrefix=oai_dc
'''
from __future__ import unicode_literals

from scrapi.base import OAIHarvester


class IastateHarvester(OAIHarvester):
    short_name = 'iastate'
    long_name = 'Digital Repository @ Iowa State University'
    url = 'http://lib.dr.iastate.edu'

    base_url = 'http://lib.dr.iastate.edu/do/oai/'
    property_list = ['source', 'identifier', 'date', 'type', 'format', 'setSpec']
    timezone_granularity = True

    approved_sets = [
        u'museums_rediscoveringshelves',
        u'museums_rediscoveringshelves_installation',
        u'museums_rediscoveringshelves_videos',
        u'extension_4h',
        u'extension_4h_pubs',
        u'abe_carousel',
        u'acct',
        u'acct_pubs',
        u'accounting_pubs',
        u'admin',
        u'abe_eng_advancedmachinery',
        u'abe_ag_advancedmachinery',
        u'abe_ag_advancedmachinery_conf',
        u'abe_eng_advancedmachinery_conf',
        u'abe_ag_advancedmachinery_pubs',
        u'abe_eng_advancedmachinery_pubs',
        u'cbe_advancedmaterials',
        u'cbe_advancedmaterials_conf',
        u'cbe_advancedmaterials_pubs',
        u'aere',
        u'aere_conf',
        u'aere_patents',
        u'aere_pubs',
        u'aere_etd',
        u'afam',
        u'afam_pubs',
        u'agdm',
        u'farms_centraliowa_reports',
        u'ageds',
        u'ageds_etd',
        u'safefarm_ag',
        u'safefarm',
        u'safefarm_ag_pubs',
        u'safefarm_pubs',
        u'agpolicyreview',
        u'ag_researchbulletins',
        u'abe_ag',
        u'abe_eng',
        u'abe_eng_books',
        u'abe_ag_books',
        u'abe_eng_conf',
        u'abe_ag_extensionpubs',
        u'abe_eng_extensionpubs',
        u'abe_eng_patents',
        u'abe_ag_patents',
        u'abe_ag_conf',
        u'abe_ag_reports',
        u'abe_eng_pubs',
        u'abe_ag_pubs',
        u'abe_eng_researchareas',
        u'abe_eng_reports',
        u'abe_ag_etd',
        u'abe_eng_etd',
        u'extension_ag_pubs',
        u'extension_ag',
        u'agron',
        u'agron_conf',
        u'agron_pubs',
        u'agron_reports',
        u'agron_etd',
        u'airforce',
        u'airforce_pubs',
        u'a2ru',
        u'amin',
        u'amin_pubs',
        u'ameslab',
        u'ameslab_manuscripts',
        u'ameslab_conf',
        u'ameslab_iscreports',
        u'ameslab_patents',
        u'ameslab_pubs',
        u'ameslab_software',
        u'ameslab_isreports',
        u'aecl',
        u'aecl_pubs',
        u'aecl_etd',
        u'ans_air',
        u'abe_eng_animalproduction',
        u'abe_ag_animalproduction',
        u'abe_eng_animalproduction_conf',
        u'abe_ag_animalproduction_conf',
        u'abe_eng_animalproduction_pubs',
        u'abe_ag_animalproduction_pubs',
        u'ans',
        u'ans_conf',
        u'ans_pubs',
        u'ans_reports',
        u'ans_etd',
        u'ans_whitepapers',
        u'anthr',
        u'anthr_pubs',
        u'anthr_etd',
        u'aeshm',
        u'aeshm_conf',
        u'aeshm_pubs',
        u'aeshm_etd',
        u'arch',
        u'arch_books',
        u'arch_conf',
        u'arch_announcements',
        u'arch_pubs',
        u'arch_etd',
        u'farms_armstrong_reports',
        u'ad',
        u'ad_conf',
        u'ad_etd',
        u'avc',
        u'avc_creativeworks',
        u'avc_pubs',
        u'asam',
        u'asam_pubs',
        u'baltic_reports',
        u'balticbasin_reports',
        u'beefreports_1996',
        u'beefreports_1997',
        u'beefreports_1998',
        u'beefreports_1999',
        u'beefreports_2000',
        u'beefreports_2001',
        u'beefreports_2002',
        u'beefreports_2003',
        u'bce_proceedings',
        u'bbmb_ag',
        u'bbmb_las',
        u'bbmb_ag_pubs',
        u'bbmb_las_etd',
        u'bbmb_ag_etd',
        u'bbmb_ag_conf',
        u'bei',
        u'bei_reports',
        u'bcb_etd',
        u'abe_ag_biologicalprocess',
        u'abe_eng_biologicalprocess',
        u'abe_ag_biologicalprocess_conf',
        u'abe_eng_biologicalprocess_conf',
        u'abe_ag_biologicalprocess_pubs',
        u'abe_eng_biologicalprocess_pubs',
        u'bms',
        u'bms_pubs',
        u'bms_reports',
        u'bms_etd',
        u'brt_etd',
        u'cbe_biorenewables',
        u'cbe_biorenewables_conf',
        u'cbe_biorenewables_pubs',
        u'bot',
        u'botany_etd',
        u'bot_pubs',
        u'bot_etd',
        u'experimentstation_bulletin',
        u'business_etd',
        u'card_books',
        u'card_briefingpapers',
        u'card_pubs',
        u'card_policybriefs',
        u'card_pres',
        u'card_reports',
        u'card_publications',
        u'card_staffreports',
        u'card_technicalreports',
        u'card_workingpapers',
        u'carver',
        u'carver_narratives',
        u'cbe_catalysis',
        u'cbe_catalysis_conf',
        u'cbe_catalysis_pubs',
        u'card',
        u'cbirc_annualreports',
        u'ccur',
        u'ccur_conf',
        u'ccur_pubs',
        u'cfsph',
        u'cfsph_pubs',
        u'cnde',
        u'cnde_conf',
        u'cnde_reports',
        u'cnde_pubs',
        u'cnde_etd',
        u'edesign',
        u'edesign_newsletters',
        u'edesign_conf',
        u'edesign_pubs',
        u'edesign_etd',
        u'cbe',
        u'cbe_conf',
        u'cbe_pubs',
        u'cbe_researchareas',
        u'cbe_etd',
        u'chem',
        u'chem_conf',
        u'chem_pubs',
        u'chem_etd',
        u'libaccess',
        u'libaccess_conf',
        u'libaccess_workshops',
        u'libaccess_pubs',
        u'ccee',
        u'ccee_books',
        u'ccee_conf',
        u'ccee_pubs',
        u'ccee_researchareas',
        u'ccee_etd',
        u'libcat',
        u'libcat_conf',
        u'libcat_pubs',
        u'ag',
        u'business',
        u'design',
        u'colledu',
        u'engineering',
        u'hs',
        u'chsmatters',
        u'las',
        u'vetmed',
        u'communitymatters',
        u'communityplanning',
        u'communityplanning_pubs',
        u'communityplanning_etd',
        u'cbe_fluiddynamics',
        u'cbe_fluiddynamics_conf',
        u'cbe_fluiddynamics_pubs',
        u'cs_techreports_applications',
        u'cs',
        u'cs_pubs',
        u'cs_techreports',
        u'cs_etd',
        u'cs_techreports_compsystems',
        u'cs_techreports_methodologies',
        u'cs_techreports_milleux',
        u'pres_portfolio',
        u'ccee_construction',
        u'ccee_construction_conf',
        u'ccee_construction_pubs',
        u'cornbeltcowcalf',
        u'ci',
        u'ci_etd',
        u'ci_pubs',
        u'dae-card_sectoranalysis',
        u'ebooks',
        u'cs_techreports_data',
        u'entnewsletter',
        u'housing',
        u'housing_books',
        u'digirep',
        u'digirep_conf',
        u'digirep_outreach',
        u'digirep_pubs',
        u'dimensions',
        u'dgtc_symposium',
        u'diversityreports',
        u'driftlessconference',
        u'eeb_etd',
        u'eeob_las',
        u'eeob_ag',
        u'eeob_conf',
        u'eeob_ag_pubs',
        u'eeob_las_pubs',
        u'eeob_ag_reports',
        u'eeob_las_etd',
        u'eeob_ag_etd',
        u'econ_las_staffpapers',
        u'econ_ag_staffpapers',
        u'econ_ag',
        u'econ_las',
        u'econ_ag_conf',
        u'econ_las_conf',
        u'econ_las_pubs',
        u'econ_ag_etd',
        u'econ_las_etd',
        u'edu_pubs',
        u'elps',
        u'elps_pubs',
        u'elps_etd',
        u'ece',
        u'ece_books',
        u'ece_conf',
        u'ece_pubs',
        u'ece_reports',
        u'ece_etd',
        u'engl',
        u'engl_books',
        u'engl_conf',
        u'engl_pubs',
        u'engl_etd',
        u'ent',
        u'ent_conf',
        u'ent_pubs',
        u'ent_reports',
        u'ent_etd',
        u'ensci_etd',
        u'ensci_studentprojects',
        u'ccee_environmental',
        u'ccee_environmental_conf',
        u'ccee_environmental_pubs',
        u'ethos',
        u'extension_communities',
        u'extension_communities_pubs',
        u'extension',
        u'hs_extension_conf',
        u'extension_conf',
        u'extension_pubs',
        u'extension_research',
        u'hs_extension',
        u'hs_extension_pubs',
        u'fapri_staffreports',
        u'ir_factbooks',
        u'finance',
        u'finance_pubs',
        u'fshn_ag',
        u'fshn_hs',
        u'fshn_ag_extensionpubs',
        u'fshn_hs_extensionpubs',
        u'fshn_ag_patents',
        u'fshn_hs_patents',
        u'fshn_hs_conf',
        u'fshn_ag_conf',
        u'fshn_ag_pubs',
        u'fshn_hs_pubs',
        u'fshn_ag_etd',
        u'fshn_hs_etd',
        u'for',
        u'for_pubs',
        u'for_reports',
        u'for_etd',
        u'gatt_papers',
        u'cs_techreports_general',
        u'genetics_etd',
        u'gdcb_conf',
        u'gdcb_ag',
        u'gdcb_las',
        u'gdcb_las_pubs',
        u'gdcb_ag_etd',
        u'gdcb_las_etd',
        u'gentle_doctor',
        u'ge_at',
        u'ge_at_etd',
        u'ge_at_pubs',
        u'ccee_geotechnical',
        u'ccee_geotechnical_conf',
        u'ccee_geotechnical_pubs',
        u'gerontology_etd',
        u'grad',
        u'grad_reports',
        u'etd',
        u'graphicdesign',
        u'graphicdesign_etd',
        u'jlmc',
        u'cs_techreports_hardware',
        u'cbe_biomedical',
        u'cbe_biomedical_conf',
        u'cbe_biomedical_pubs',
        u'ag_hist',
        u'design_hist',
        u'las_hist',
        u'hs_hist',
        u'history',
        u'history_books',
        u'history_conf',
        u'history_pubs',
        u'history_etd',
        u'honors_posters',
        u'hort',
        u'hort_conf',
        u'hort_pubs',
        u'farms_horticulture_reports',
        u'hort_etd',
        u'hci_etd',
        u'hdfs',
        u'hdfs_extensionpubs',
        u'hdfs_conf',
        u'hdfs_pubs',
        u'hdfs_reports',
        u'hdfs_etd',
        u'extension_families',
        u'extension_families_pubs',
        u'imsenews',
        u'econ_las_economicreports',
        u'econ_ag_economicreports',
        u'immunobiology_etd',
        u'intrans_reports',
        u'industrialdesign',
        u'industrialdesign_etd',
        u'iet_pubs',
        u'iet',
        u'imse',
        u'imse_conf',
        u'imse_pubs',
        u'imse_reports',
        u'imse_etd',
        u'infas_etd',
        u'cs_techreports_infosystems',
        u'is_etd',
        u'inspire',
        u'iprt',
        u'intrans',
        u'ir',
        u'cropnews',
        u'interdisciplinaryprograms_graduate',
        u'cnde_yellowjackets',
        u'grad_etd',
        u'id',
        u'id_conf',
        u'id_etd',
        u'safepork',
        u'iowaagreview',
        u'iaes_circulars',
        u'iahees',
        u'ibc',
        u'cfwru',
        u'cfwru_reports',
        u'ipic',
        u'ipic_factsheets',
        u'ipic_handbooks',
        u'iowastatedaily',
        u'iowastatedaily_2010',
        u'iowastatedaily_2011',
        u'iowastatedaily_2012',
        u'iowastatedaily_2013',
        u'iowastatedaily_2014',
        u'iowastatedaily_2015',
        u'iowastatedaily_2011-04',
        u'iowastatedaily_2012-04',
        u'iowastatedaily_2013-04',
        u'iowastatedaily_2014-04',
        u'iowastatedaily_2015-04',
        u'iowastatedaily_2010-08',
        u'iowastatedaily_2011-08',
        u'iowastatedaily_2012-08',
        u'iowastatedaily_2013-08',
        u'iowastatedaily_2014-08',
        u'iowastatedaily_2015-08',
        u'iowastatedaily_2010-12',
        u'iowastatedaily_2011-12',
        u'iowastatedaily_2012-12',
        u'iowastatedaily_2013-12',
        u'iowastatedaily_2014-12',
        u'iowastatedaily_2015-12',
        u'iowastatedaily_2011-02',
        u'iowastatedaily_2012-02',
        u'iowastatedaily_2013-02',
        u'iowastatedaily_2014-02',
        u'iowastatedaily_2015-02',
        u'iowastatedaily_2011-01',
        u'iowastatedaily_2012-01',
        u'iowastatedaily_2013-01',
        u'iowastatedaily_2014-01',
        u'iowastatedaily_2015-01',
        u'iowastatedaily_2010-07',
        u'iowastatedaily_2011-07',
        u'iowastatedaily_2012-07',
        u'iowastatedaily_2013-07',
        u'iowastatedaily_2014-07',
        u'iowastatedaily_2015-07',
        u'iowastatedaily_2010-06',
        u'iowastatedaily_2011-06',
        u'iowastatedaily_2012-06',
        u'iowastatedaily_2013-06',
        u'iowastatedaily_2014-06',
        u'iowastatedaily_2015-06',
        u'iowastatedaily_2011-03',
        u'iowastatedaily_2012-03',
        u'iowastatedaily_2013-03',
        u'iowastatedaily_2014-03',
        u'iowastatedaily_2015-03',
        u'iowastatedaily_2010-05',
        u'iowastatedaily_2011-05',
        u'iowastatedaily_2012-05',
        u'iowastatedaily_2013-05',
        u'iowastatedaily_2014-05',
        u'iowastatedaily_2015-05',
        u'iowastatedaily_2010-11',
        u'iowastatedaily_2011-11',
        u'iowastatedaily_2012-11',
        u'iowastatedaily_2013-11',
        u'iowastatedaily_2014-11',
        u'iowastatedaily_2015-11',
        u'iowastatedaily_2010-10',
        u'iowastatedaily_2011-10',
        u'iowastatedaily_2012-10',
        u'iowastatedaily_2013-10',
        u'iowastatedaily_2014-10',
        u'iowastatedaily_2015-10',
        u'iowastatedaily_2010-09',
        u'iowastatedaily_2011-09',
        u'iowastatedaily_2012-09',
        u'iowastatedaily_2013-09',
        u'iowastatedaily_2014-09',
        u'iowastatedaily_2015-09',
        u'farms_reports',
        u'farms_reportsbyfarm',
        u'catalog',
        u'patents',
        u'isurf',
        u'farms',
        u'iowastate_veterinarian',
        u'weedbiology',
        u'icip',
        u'jctp',
        u'jlmc_etd',
        u'jlmc_pubs',
        u'kin',
        u'kin_pubs',
        u'kin_etd',
        u'abe_eng_landwaterresources',
        u'abe_ag_landwaterresources',
        u'abe_ag_landwaterresources_conf',
        u'abe_eng_landwaterresources_conf',
        u'abe_eng_landwaterresources_pubs',
        u'abe_ag_landwaterresources_pubs',
        u'landscapearchitecture',
        u'landscapearchitecture_conf',
        u'landscapearchitecture_pubs',
        u'landscapearchitecture_etd',
        u'lau_slideshow',
        u'leadership',
        u'leadership_conf',
        u'leadership_pubs',
        u'leopold_annualreports',
        u'leopold_grantreports',
        u'leopold_extension',
        u'leopold_proceedings',
        u'leopold_pubspapers',
        u'leopold',
        u'leopold_letter',
        u'libadmin',
        u'libadmin_conf',
        u'libadmin_pubs',
        u'library_books',
        u'libit_pubs',
        u'libreports',
        u'livestock',
        u'matric_briefingpapers',
        u'matric_researchpapers',
        u'matric_workingpapers',
        u'management',
        u'management_pubs',
        u'management_reports',
        u'marketing_pubs',
        u'mse',
        u'mse_conf',
        u'mse_pubs',
        u'mse_etd',
        u'math',
        u'math_conf',
        u'math_etd',
        u'cs_techreports_mathematics',
        u'math_pubs',
        u'farms_mcnay_reports',
        u'meatscience',
        u'meatscience_air',
        u'meatscience_pubs',
        u'me',
        u'me_conf',
        u'me_pubs',
        u'me_etd',
        u'me_whitepapers',
        u'im_etd',
        u'micro',
        u'micro_pubs',
        u'micro_etd',
        u'armyrotc',
        u'armyrotc_pubs',
        u'mcdb_etd',
        u'farms_muscatine_reports',
        u'music_pubs',
        u'music_recordings',
        u'music',
        u'ncrac_annualreports',
        u'ncrac_cultureguides',
        u'ncrac_factsheets',
        u'ncrac_techbulletins',
        u'ncrac_whitepapers',
        u'ncrpis_conf',
        u'ncrpis_pubs',
        u'cbirc',
        u'swinefeedefficiency',
        u'nrem',
        u'nrem_conf',
        u'nrem_extensionpubs',
        u'nrem_pubs',
        u'nrem_studentprojects',
        u'nrem_etd',
        u'nrem_reports',
        u'navy',
        u'navy_pubs',
        u'resilientneighborhoods_plans',
        u'neuroscience_etd',
        u'ncrac',
        u'ncrac_pubs',
        u'ncrac_etd',
        u'ncrac_conferences',
        u'ncrpis',
        u'farms_northeast_reports',
        u'farms_northern_reports',
        u'farms_northwest_reports',
        u'igpns_etd',
        u'abe_eng_occupationalsafety',
        u'abe_ag_occupationalsafety',
        u'abe_ag_occupationalsafety_conf',
        u'abe_eng_occupationalsafety_conf',
        u'abe_ag_occupationalsafety_pubs',
        u'abe_eng_occupationalsafety_pubs',
        u'provost_reports',
        u'registrar',
        u'provost',
        u'philrs',
        u'philrs_pubs',
        u'physastro',
        u'physastro_conf',
        u'physastro_pubs',
        u'physastro_etd',
        u'ipb_etd',
        u'plantpath_conf',
        u'plantpath',
        u'plantpath_pubs',
        u'plantpath_etd',
        u'pols',
        u'pols_pubs',
        u'pols_etd',
        u'icip_poverty',
        u'pres',
        u'pres_conf',
        u'pres_workshops',
        u'pres_pubs',
        u'cnde_yellowjackets_1976',
        u'cnde_yellowjackets_1978',
        u'cnde_yellowjackets_1977',
        u'cnde_yellowjackets_1975',
        u'cnde_yellowjackets_1979',
        u'cnde_yellowjackets_1981',
        u'cnde_yellowjackets_1974',
        u'psychology',
        u'psychology_conf',
        u'psychology_pubs',
        u'psychology_etd',
        u'refinst',
        u'refinst_conf',
        u'refinst_pubs',
        u'cbe_renewableenergy',
        u'cbe_renewableenergy_conf',
        u'cbe_renewableenergy_pubs',
        u'ccee_reports',
        u'abe_ag_researchareas',
        u'resilientneighborhoods',
        u'resilientneighborhoods_memos',
        u'resilientneighborhoods_reports',
        u'rtd',
        u'qnde',
        u'revival',
        u'stories',
        u'safefarm_ag_extension',
        u'safefarm_extension',
        u'safefarmminute_ag',
        u'safefarmminute',
        u'safefarm_minutes',
        u'safepork_covers',
        u'edu',
        u's2erc',
        u's2erc_reports',
        u'stb_etd',
        u'sheepreports_1997',
        u'sketch',
        u'soc_las',
        u'soc_ag',
        u'soc_las_extensionpubs',
        u'soc_las_pubs',
        u'soc_las_reports',
        u'soc_las_etd',
        u'soc_ag_etd',
        u'cs_techreports_software',
        u'farms_southeast_reports',
        u'soybeanaphid_podcasts',
        u'speccoll_conf',
        u'speccoll_exhibits',
        u'speccoll_outreach',
        u'speccoll_pubs',
        u'speccoll',
        u'stat_las',
        u'stat_ag',
        u'stat_ag_conf',
        u'stat_las_conf',
        u'stat_las_preprints',
        u'stat_ag_preprints',
        u'stat_las_pubs',
        u'stat_las_etd',
        u'stat_ag_etd',
        u'stories_covers',
        u'ccee_structural',
        u'ccee_structural_conf',
        u'ccee_structural_pubs',
        u'scm_conf',
        u'scm',
        u'scm_pubs',
        u'susag_conf',
        u'susag',
        u'susag_pubs',
        u'gpsa_etd',
        u'swinefeedefficiency_air',
        u'swinefeedefficiency_conf',
        u'swinefeedefficiency_factsheets',
        u'swinefeedefficiency_pubs',
        u'swinefeedefficiency_etd',
        u'swinereports_1996',
        u'swinereports_1997',
        u'swinereports_1998',
        u'swinereports_1999',
        u'swinereports_2000',
        u'swinereports_2001',
        u'swinereports_2002',
        u'undergradresearch_symposium',
        u'systemseng_etd',
        u'intrans_techtransfer',
        u'cs_techreports_subjects',
        u'tcmuseum',
        u'tcmuseum_exhibits',
        u'tcmuseum_installation',
        u'cs_techreports_theory',
        u'toxicology_etd',
        u'trans_etd',
        u'ccee_transportation',
        u'ccee_transportation_conf',
        u'ccee_transportation_pubs',
        u'trend',
        u'usls',
        u'usls_pubs',
        u'uhuru',
        u'undergradresearch',
        u'honors',
        u'library',
        u'bookmarks',
        u'museums',
        u'museums_exhibitguides',
        u'museums_exhibits',
        u'museums_installation',
        u'museums_videos',
        u'vcs',
        u'vcs_conf',
        u'vcs_pubs',
        u'vcs_reports',
        u'vcs_etd',
        u'vdpam',
        u'vdpam_conf',
        u'vdpam_pubs',
        u'vdpam_reports',
        u'vdpam_etd',
        u'vmpm',
        u'vmpm_pubs',
        u'vmpm_reports',
        u'vmpm_etd',
        u'vpath',
        u'vpath_conf',
        u'vpath_pubs',
        u'vpath_reports',
        u'vpath_etd',
        u'vrac',
        u'vrac_conf',
        u'vrac_pubs',
        u'weedscience_reports',
        u'farms_western_reports',
        u'withhonors',
        u'tcmuseum_exhibits_womenforwomen',
        u'language',
        u'language_conf',
        u'language_pubs',
        u'zool',
        u'zool_pubs',
        u'zool_etd',
        u'a2ru_photos'
    ]
