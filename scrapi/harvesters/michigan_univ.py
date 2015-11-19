'''
Harvester for the Deep Blue for the SHARE project

Example API call: http://deepblue.lib.umich.edu/dspace-oai/request?verb=ListRecords&metadataPrefix=oai_dc
'''
from __future__ import unicode_literals

from scrapi.base import OAIHarvester


class UmichHarvester(OAIHarvester):
    short_name = 'umich'
    long_name = 'Deep Blue University of Michigan'
    url = 'http://deepblue.lib.umich.edu'

    base_url = 'http://deepblue.lib.umich.edu/dspace-oai/request'
    property_list = ['date', 'identifier', 'setSpec']
    timezone_granularity = True

    approved_sets = [
        'col_2027.42_57773',
        'col_2027.42_62481',
        'col_2027.42_60130',
        'col_2027.42_51534',
        'col_2027.42_58597',
        'com_2027.42_65133',
        'col_2027.42_41237',
        'col_2027.42_60475',
        'col_2027.42_78358',
        'col_2027.42_57483',
        'col_2027.42_49245',
        'col_2027.42_78359',
        'col_2027.42_49252',
        'col_2027.42_61182',
        'col_2027.42_58060',
        'col_2027.42_50691',
        'col_2027.42_64026',
        'col_2027.42_35324',
        'col_2027.42_50473',
        'col_2027.42_61365',
        'col_2027.42_78361',
        'col_2027.42_63588',
        'col_2027.42_58625',
        'col_2027.42_58741',
        'col_2027.42_57485',
        'col_2027.42_63030',
        'col_2027.42_51400',
        'col_2027.42_39366',
        'col_2027.42_77949',
        'col_2027.42_58366',
        'col_2027.42_60161',
        'col_2027.42_58605',
        'col_2027.42_60937',
        'col_2027.42_39212',
        'col_2027.42_13915',
        'col_2027.42_61837',
        'col_2027.42_40242',
        'com_2027.42_79040',
        'col_2027.42_57190',
        'col_2027.42_64867',
        'col_2027.42_55692',
        'col_2027.42_60175',
        'col_2027.42_62180',
        'col_2027.42_55467',
        'col_2027.42_55461',
        'col_2027.42_40241',
        'col_2027.42_56218',
        'col_2027.42_57418',
        'col_2027.42_57738',
        'col_2027.42_21621',
        'col_2027.42_21609',
        'col_2027.42_78207',
        'col_2027.42_55736',
        'col_2027.42_55473',
        'col_2027.42_71387',
        'col_2027.42_40243',
        'col_2027.42_57759',
        'col_2027.42_58219',
        'col_2027.42_61172',
        'col_2027.42_49548',
        'col_2027.42_57420',
        'col_2027.42_61002',
        'col_2027.42_49477',
        'col_2027.42_78360',
        'col_2027.42_77456',
        'col_2027.42_58188',
        'col_2027.42_64496',
        'col_2027.42_35325',
        'col_2027.42_64452',
        'col_2027.42_65119',
        'col_2027.42_64002',
        'col_2027.42_49538',
        'col_2027.42_60933',
        'col_2027.42_64343',
        'col_2027.42_61282',
        'col_2027.42_55277',
        'col_2027.42_41251',
        'col_2027.42_58662',
        'col_2027.42_61259',
        'col_2027.42_69349',
        'col_2027.42_51549',
        'col_2027.42_58620',
        'col_2027.42_56193',
        'col_2027.42_55486',
        'col_2027.42_61401',
        'com_2027.42_13913',
        'col_2027.42_55256',
        'col_2027.42_49331',
        'col_2027.42_57558',
        'col_2027.42_64010',
        'col_2027.42_57275',
        'col_2027.42_50792',
        'col_2027.42_55208',
        'col_2027.42_49482',
        'col_2027.42_39193',
        'col_2027.42_57498',
        'col_2027.42_13914',
        'col_2027.42_50621',
        'col_2027.42_39392',
        'col_2027.42_49534'
    ]
