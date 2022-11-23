import openpyxl
from KaAryaProperties.settings import BASE_DIR
from core_app.models import Property


def import_property_data():
    file_path = str(BASE_DIR) + "/excel_data_files/property_data.xlsx"
    dataframe = openpyxl.load_workbook(file_path)
    dataframe1 = dataframe.active
    property_field = ['property_for', 'property_type', 'furniture_type', 'name', 'short_desc', 'long_desc', 'location',
                      'price', 'address', 'landmark', 'no_of_bed', 'no_of_bath', 'no_of_balcony', 'carper_area',
                      'builtup_area', 'super_builtup_area', 'no_of_floor', 'floor', 'allowed_for', 'facing',
                      'type_of_ownership', 'age_of_construction', 'builder', 'rera_id', 'lifts', 'parking', 'property_contact']

    for row in range(1, dataframe1.max_row):
        # property_record = Property.objects.create()
        i = 0
        for col in dataframe1.iter_cols(1, dataframe1.max_column):
            print(col[row].value, "======", property_field[i])
            property_field[i] = col[row].value
            i += 1
        # property_record.save()


import_property_data()
