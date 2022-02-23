from django.db import models
from ..locations.models import Location


class TaxonNameType(models.Model):
    taxon_name_type_key = models.CharField(db_column='TAXON_NAME_TYPE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    authority = models.CharField(db_column='AUTHORITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXON_NAME_TYPE'

class TaxonListType(models.Model):
    taxon_list_type_key = models.CharField(db_column='TAXON_LIST_TYPE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    schedule = models.BooleanField(db_column='SCHEDULE')  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allow_data_entry = models.BooleanField(db_column='Allow_Data_Entry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXON_LIST_TYPE'

class TaxonList(models.Model):
    taxon_list_key = models.CharField(db_column='TAXON_LIST_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=200)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    authority = models.CharField(db_column='AUTHORITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    taxon_list_type_key = models.ForeignKey('TaxonListType', models.DO_NOTHING, db_column='TAXON_LIST_TYPE_KEY', blank=True, null=True)  # Field name made lowercase.
    local_disk = models.BooleanField(db_column='LOCAL_DISK')  # Field name made lowercase.
    update_mechanism = models.CharField(db_column='UPDATE_MECHANISM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    preferred = models.BooleanField(db_column='PREFERRED')  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXON_LIST'


class TaxonListVersion(models.Model):
    taxon_list_version_key = models.CharField(db_column='TAXON_LIST_VERSION_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    taxon_list_key = models.ForeignKey(TaxonList, models.DO_NOTHING, db_column='TAXON_LIST_KEY', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.
    authority = models.CharField(db_column='AUTHORITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vague_date_start = models.IntegerField(db_column='VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    vague_date_end = models.IntegerField(db_column='VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    vague_date_type = models.CharField(db_column='VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    version_is_amendment = models.BooleanField(db_column='VERSION_IS_AMENDMENT')  # Field name made lowercase.
    quality = models.TextField(db_column='QUALITY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    source_key = models.CharField(db_column='SOURCE_KEY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXON_LIST_VERSION'

class TaxonGroup(models.Model):
    taxon_group_key = models.CharField(db_column='TAXON_GROUP_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    taxon_group_name = models.CharField(db_column='TAXON_GROUP_NAME', max_length=50)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    use_taxon_list_key = models.ForeignKey('TaxonList', models.DO_NOTHING, db_column='USE_TAXON_LIST_KEY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXON_GROUP'

class Taxon(models.Model):
    taxon_key = models.CharField(db_column='TAXON_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=75, blank=True, null=True)  # Field name made lowercase.
    authority = models.CharField(db_column='AUTHORITY', max_length=80, blank=True, null=True)  # Field name made lowercase.
    introduced_vague_date_start = models.IntegerField(db_column='INTRODUCED_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    introduced_vague_date_end = models.IntegerField(db_column='INTRODUCED_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    introduced_vague_date_type = models.CharField(db_column='INTRODUCED_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='LANGUAGE', max_length=2)  # Field name made lowercase.
    taxon_name_type_key = models.ForeignKey('TaxonNameType', models.DO_NOTHING, db_column='TAXON_NAME_TYPE_KEY')  # Field name made lowercase.
    abbreviation = models.CharField(db_column='ABBREVIATION', max_length=5, blank=True, null=True)  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXON'

class TaxonRank(models.Model):
    taxon_rank_key = models.CharField(db_column='TAXON_RANK_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    sequence = models.SmallIntegerField(db_column='SEQUENCE', blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    list_font_italic = models.BooleanField(db_column='LIST_FONT_ITALIC')  # Field name made lowercase.
    image = models.BinaryField(db_column='IMAGE', blank=True, null=True)  # Field name made lowercase.
    display_in_details = models.BooleanField(db_column='DISPLAY_IN_DETAILS')  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXON_RANK'

class TaxonVersion(models.Model):
    taxon_version_key = models.CharField(db_column='TAXON_VERSION_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    taxon_key = models.ForeignKey(Taxon, models.DO_NOTHING, db_column='TAXON_KEY', blank=True, null=True)  # Field name made lowercase.
    attribute = models.CharField(db_column='ATTRIBUTE', max_length=65, blank=True, null=True)  # Field name made lowercase.
    authority = models.CharField(db_column='AUTHORITY', max_length=40, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    validation_level = models.SmallIntegerField(db_column='VALIDATION_LEVEL', blank=True, null=True)  # Field name made lowercase.
    uk_native = models.BooleanField(db_column='UK_NATIVE')  # Field name made lowercase.
    quality = models.CharField(db_column='QUALITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source_key = models.CharField(db_column='SOURCE_KEY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    output_group_key = models.ForeignKey(TaxonGroup, models.DO_NOTHING, db_column='OUTPUT_GROUP_KEY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXON_VERSION'

class TaxonListItem(models.Model):
    taxon_list_item_key = models.CharField(db_column='TAXON_LIST_ITEM_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    taxon_version_key = models.ForeignKey('TaxonVersion', models.DO_NOTHING, db_column='TAXON_VERSION_KEY')  # Field name made lowercase.
    taxon_list_version_key = models.ForeignKey('TaxonListVersion', models.DO_NOTHING, db_column='TAXON_LIST_VERSION_KEY')  # Field name made lowercase.
    taxon_list_version_to = models.CharField(db_column='TAXON_LIST_VERSION_TO', max_length=16, blank=True, null=True)  # Field name made lowercase.
    preferred_name = models.ForeignKey('self', models.DO_NOTHING, db_column='PREFERRED_NAME', related_name='preferred_taxon_list_item')  # Field name made lowercase.
    sort_code = models.IntegerField(db_column='SORT_CODE', blank=True, null=True)  # Field name made lowercase.
    lst_itm_code = models.CharField(db_column='LST_ITM_CODE', max_length=35, blank=True, null=True)  # Field name made lowercase.
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='PARENT', blank=True, null=True, related_name='parent_taxon_list_item')  # Field name made lowercase.
    taxon_rank_key = models.ForeignKey('TaxonRank', models.DO_NOTHING, db_column='TAXON_RANK_KEY')  # Field name made lowercase.
    code_source = models.CharField(db_column='CODE_SOURCE', max_length=16, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='NOTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXON_LIST_ITEM'

class Licence(models.Model):
    licence_key = models.CharField(db_column='LICENCE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=10)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION')  # Field name made lowercase. This field type is a guess.
    url_readable = models.CharField(db_column='URL_READABLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url_legal = models.CharField(db_column='URL_LEGAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LICENCE'

class Name(models.Model):
    name_key = models.CharField(db_column='NAME_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    organisation = models.BooleanField(db_column='ORGANISATION')  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NAME'

class Survey(models.Model):
    survey_key = models.CharField(db_column='SURVEY_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=100)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    from_vague_date_start = models.IntegerField(db_column='FROM_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    from_vague_date_end = models.IntegerField(db_column='FROM_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    from_vague_date_type = models.CharField(db_column='FROM_VAGUE_DATE_TYPE', max_length=2)  # Field name made lowercase.
    to_vague_date_start = models.IntegerField(db_column='TO_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    to_vague_date_end = models.IntegerField(db_column='TO_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    to_vague_date_type = models.CharField(db_column='TO_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sw_spatial_ref = models.CharField(db_column='SW_SPATIAL_REF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ne_spatial_ref = models.CharField(db_column='NE_SPATIAL_REF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    spatial_ref_system = models.CharField(db_column='SPATIAL_REF_SYSTEM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sw_lat = models.FloatField(db_column='SW_LAT', blank=True, null=True)  # Field name made lowercase.
    sw_long = models.FloatField(db_column='SW_LONG', blank=True, null=True)  # Field name made lowercase.
    ne_lat = models.FloatField(db_column='NE_LAT', blank=True, null=True)  # Field name made lowercase.
    ne_long = models.FloatField(db_column='NE_LONG', blank=True, null=True)  # Field name made lowercase.
    geographic_coverage = models.TextField(db_column='GEOGRAPHIC_COVERAGE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    periodicity = models.CharField(db_column='PERIODICITY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ne_spatial_ref_qualifier = models.CharField(db_column='NE_SPATIAL_REF_QUALIFIER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sw_spatial_ref_qualifier = models.CharField(db_column='SW_SPATIAL_REF_QUALIFIER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    run_by = models.ForeignKey(Name, models.DO_NOTHING, db_column='RUN_BY')  # Field name made lowercase.
    survey_status_key = models.ForeignKey('SurveyStatus', models.DO_NOTHING, db_column='SURVEY_STATUS_KEY', blank=True, null=True)  # Field name made lowercase.
    survey_media_key = models.ForeignKey('SurveyMedia', models.DO_NOTHING, db_column='SURVEY_MEDIA_KEY')  # Field name made lowercase.
    survey_type_key = models.ForeignKey('SurveyType', models.DO_NOTHING, db_column='SURVEY_TYPE_KEY')  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    op_from_vague_date_start = models.IntegerField(db_column='OP_FROM_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    op_from_vague_date_end = models.IntegerField(db_column='OP_FROM_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    op_from_vague_date_type = models.CharField(db_column='OP_FROM_VAGUE_DATE_Type', max_length=2, blank=True, null=True)  # Field name made lowercase.
    op_to_vague_date_start = models.IntegerField(db_column='OP_TO_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    op_to_vague_date_end = models.IntegerField(db_column='OP_TO_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    op_to_vague_date_type = models.CharField(db_column='OP_TO_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    licence_key = models.ForeignKey(Licence, models.DO_NOTHING, db_column='LICENCE_KEY', blank=True, null=True)  # Field name made lowercase.
    private_notes = models.TextField(db_column='PRIVATE_NOTES', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attribution = models.TextField(db_column='ATTRIBUTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    import_date = models.DateTimeField(db_column='Import_Date', blank=True, null=True)  # Field name made lowercase.
    temporary_survey = models.BooleanField(db_column='Temporary_Survey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SURVEY'

class Source(models.Model):
    source_key = models.CharField(db_column='SOURCE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    internal = models.BooleanField(db_column='INTERNAL')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOURCE'

class DeterminerRole(models.Model):
    determiner_role_key = models.CharField(db_column='DETERMINER_ROLE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    validation_competency = models.SmallIntegerField(db_column='VALIDATION_COMPETENCY')  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    hide = models.BooleanField(db_column='Hide')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETERMINER_ROLE'

class DeterminationType(models.Model):
    determination_type_key = models.CharField(db_column='DETERMINATION_TYPE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=21)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    verified = models.SmallIntegerField(db_column='Verified')  # Field name made lowercase.
    hide = models.BooleanField(db_column='Hide')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETERMINATION_TYPE'

class RecordType(models.Model):
    record_type_key = models.CharField(db_column='RECORD_TYPE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=40)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RECORD_TYPE'

class Substrate(models.Model):
    substrate_key = models.CharField(db_column='SUBSTRATE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SUBSTRATE'

class Sample(models.Model):
    sample_key = models.CharField(db_column='SAMPLE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    sample_reference = models.CharField(db_column='SAMPLE_REFERENCE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    vague_date_start = models.IntegerField(db_column='VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    vague_date_end = models.IntegerField(db_column='VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    vague_date_type = models.CharField(db_column='VAGUE_DATE_TYPE', max_length=2)  # Field name made lowercase.
    spatial_ref = models.CharField(db_column='SPATIAL_REF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    spatial_ref_system = models.CharField(db_column='SPATIAL_REF_SYSTEM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT', blank=True, null=True)  # Field name made lowercase.
    long = models.FloatField(db_column='LONG', blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='DURATION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='TIME', blank=True, null=True)  # Field name made lowercase.
    outstanding_card = models.SmallIntegerField(db_column='OUTSTANDING_CARD')  # Field name made lowercase.
    spatial_ref_qualifier = models.CharField(db_column='SPATIAL_REF_QUALIFIER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sample_type_key = models.ForeignKey('SampleType', models.DO_NOTHING, db_column='SAMPLE_TYPE_KEY')  # Field name made lowercase.
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', blank=True, null=True)  # Field name made lowercase.
    survey_event_key = models.ForeignKey('SurveyEvent', models.DO_NOTHING, db_column='SURVEY_EVENT_KEY')  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    recorders = models.CharField(db_column='RECORDERS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='LOCATION_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    private_location = models.CharField(db_column='PRIVATE_LOCATION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    private_code = models.CharField(db_column='PRIVATE_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SAMPLE'

class TaxonOccurrence(models.Model):
    taxon_occurrence_key = models.CharField(db_column='TAXON_OCCURRENCE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zero_abundance = models.BooleanField(db_column='ZERO_ABUNDANCE')  # Field name made lowercase.
    confidential = models.BooleanField(db_column='CONFIDENTIAL')  # Field name made lowercase.
    verified = models.SmallIntegerField(db_column='VERIFIED')  # Field name made lowercase.
    checked = models.BooleanField(db_column='CHECKED')  # Field name made lowercase.
    checked_by = models.CharField(db_column='CHECKED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    checked_date = models.DateTimeField(db_column='CHECKED_DATE', blank=True, null=True)  # Field name made lowercase.
    surveyors_ref = models.CharField(db_column='SURVEYORS_REF', max_length=30, blank=True, null=True)  # Field name made lowercase.
    provenance = models.CharField(db_column='PROVENANCE', max_length=16, blank=True, null=True)  # Field name made lowercase.
    sample_key = models.ForeignKey(Sample, models.DO_NOTHING, db_column='SAMPLE_KEY')  # Field name made lowercase.
    substrate_key = models.ForeignKey(Substrate, models.DO_NOTHING, db_column='SUBSTRATE_KEY', blank=True, null=True)  # Field name made lowercase.
    record_type_key = models.ForeignKey(RecordType, models.DO_NOTHING, db_column='RECORD_TYPE_KEY', blank=True, null=True)  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXON_OCCURRENCE'

class TaxonDetermination(models.Model):
    taxon_determination_key = models.CharField(db_column='TAXON_DETERMINATION_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    taxon_list_item_key = models.ForeignKey('TaxonListItem', models.DO_NOTHING, db_column='TAXON_LIST_ITEM_KEY')  # Field name made lowercase.
    taxon_occurrence_key = models.ForeignKey('TaxonOccurrence', models.DO_NOTHING, db_column='TAXON_OCCURRENCE_KEY')  # Field name made lowercase.
    vague_date_start = models.IntegerField(db_column='VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    vague_date_end = models.IntegerField(db_column='VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    vague_date_type = models.CharField(db_column='VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    preferred = models.BooleanField(db_column='PREFERRED')  # Field name made lowercase.
    determiner = models.ForeignKey(Name, models.DO_NOTHING, db_column='DETERMINER')  # Field name made lowercase.
    determination_type_key = models.ForeignKey(DeterminationType, models.DO_NOTHING, db_column='DETERMINATION_TYPE_KEY')  # Field name made lowercase.
    determiner_role_key = models.ForeignKey(DeterminerRole, models.DO_NOTHING, db_column='DETERMINER_ROLE_KEY')  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    source_key = models.ForeignKey(Source, models.DO_NOTHING, db_column='SOURCE_KEY', blank=True, null=True)  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXON_DETERMINATION'



class SampleType(models.Model):
    sample_type_key = models.CharField(db_column='SAMPLE_TYPE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    image = models.BinaryField(db_column='IMAGE', blank=True, null=True)  # Field name made lowercase.
    recording_card = models.CharField(db_column='RECORDING_CARD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SAMPLE_TYPE'

class SurveyEvent(models.Model):
    survey_event_key = models.CharField(db_column='SURVEY_EVENT_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    survey_event_weather = models.CharField(db_column='SURVEY_EVENT_WEATHER', max_length=200, blank=True, null=True)  # Field name made lowercase.
    spatial_ref = models.CharField(db_column='SPATIAL_REF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    spatial_ref_system = models.CharField(db_column='SPATIAL_REF_SYSTEM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT', blank=True, null=True)  # Field name made lowercase.
    long = models.FloatField(db_column='LONG', blank=True, null=True)  # Field name made lowercase.
    spatial_ref_qualifier = models.CharField(db_column='SPATIAL_REF_QUALIFIER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vague_date_start = models.IntegerField(db_column='VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    vague_date_end = models.IntegerField(db_column='VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    vague_date_type = models.CharField(db_column='VAGUE_DATE_TYPE', max_length=2)  # Field name made lowercase.
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', blank=True, null=True)  # Field name made lowercase.
    survey_key = models.ForeignKey(Survey, models.DO_NOTHING, db_column='SURVEY_KEY')  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    location_name = models.CharField(db_column='LOCATION_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SURVEY_EVENT'

class SurveyStatus(models.Model):
    survey_status_key = models.CharField(db_column='SURVEY_STATUS_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SURVEY_STATUS'

class SurveyMedia(models.Model):
    survey_media_key = models.CharField(db_column='SURVEY_MEDIA_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SURVEY_MEDIA'

class SurveyType(models.Model):
    survey_type_key = models.CharField(db_column='SURVEY_TYPE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SURVEY_TYPE'
