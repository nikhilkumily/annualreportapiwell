import pandas as pd
from django.core.management.base import BaseCommand
from api_details.models import WellData

class Command(BaseCommand):
    help = 'Import annual production data from Excel and save it to the database'

    def handle(self, *args, **options):
        # Load the Excel file
        # for xlsxwe can use the engine as openpyxl
        df = pd.read_excel('api_well_data.xls', engine='xlrd')  
        # Group by 'API WELL  NUMBER' and sum the production data across quarters
        annual_data = df.groupby('API WELL  NUMBER').agg({
            'OIL': 'sum',
            'GAS': 'sum',
            'BRINE': 'sum',
        }).reset_index()

        # Create a list of WellData objects
        annual_productions = [
            WellData(
                well_id=row['API WELL  NUMBER'],
                oil=row['OIL'],
                gas=row['GAS'],
                brine=row['BRINE'],
            )
            for _, row in annual_data.iterrows()
        ]

        # Use bulk_create to insert all records at once
        WellData.objects.bulk_create(annual_productions)

        print(f"Annual production data has been successfully loaded into the database. \n{annual_data['API WELL  NUMBER'].count()} data entered")