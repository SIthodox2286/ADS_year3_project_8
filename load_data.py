import pandas as pd 
import numpy as np
import openpyxl

def load_council_tax_data():
    # Open the Council tax data set
    workbook = openpyxl.load_workbook('Data/ENGLAND_council_tax_band_properties.xlsx')
    
    # read columns that contains the lastest property counts for all bands (2021's) and administrative area names in England.
    council_tax_band = workbook['CTSOP4.0']
    council_tax_band = pd.DataFrame(council_tax_band.values)
    council_tax_band = council_tax_band.drop(labels=range(0,5), axis=0)
    council_tax_band = council_tax_band.drop(columns=range(council_tax_band.columns[6],council_tax_band.columns[31]))
    council_tax_band = council_tax_band.drop(columns=range(council_tax_band.columns[0],council_tax_band.columns[4]))
    council_tax_band = pd.DataFrame(council_tax_band)
    council_tax_band = council_tax_band.rename(columns={4:'area_name', 5:'band', 31:'number_of_properties'})
    
    # Extract the Area Name labels
    area_names = list(pd.unique(council_tax_band[:]['area_name']))
    
    # Extract the properties in each band.
    band_A = council_tax_band[council_tax_band["band"]=='A'].replace('-', 0) # A, Up to and including £40,000, tax charge £1,486.91
    band_B = council_tax_band[council_tax_band["band"]=='B'].replace('-', 0) # B, £40,001 - £52,000, tax charge £1,734.73
    band_C = council_tax_band[council_tax_band["band"]=='C'].replace('-', 0) # C, £52,001 - £68,000, tax charge £1,982.55
    band_D = council_tax_band[council_tax_band["band"]=='D'].replace('-', 0) # D, £68,001 - £88,000, tax charge £2,230.37
    band_E = council_tax_band[council_tax_band["band"]=='E'].replace('-', 0) # E, £88,001 - £120,000, tax charge £2,726.01
    band_F = council_tax_band[council_tax_band["band"]=='F'].replace('-', 0) # F, £120,001 - £160,000, tax charge £3,221.64
    band_G = council_tax_band[council_tax_band["band"]=='G'].replace('-', 0) # G, £160,001 - £320,000, tax charge £3,717.28
    band_H = council_tax_band[council_tax_band["band"]=='H'].replace('-', 0) # H, Over £320,000, tax charge £4,460.74

    # Transform them into nd.array for vector sum purpose.
    band_A = np.array(band_A['number_of_properties']).reshape(-1,1)
    band_B = np.array(band_B['number_of_properties']).reshape(-1,1)
    band_C = np.array(band_C['number_of_properties']).reshape(-1,1)
    band_D = np.array(band_D['number_of_properties']).reshape(-1,1)
    band_E = np.array(band_E['number_of_properties']).reshape(-1,1)
    band_F = np.array(band_F['number_of_properties']).reshape(-1,1)
    band_G = np.array(band_G['number_of_properties']).reshape(-1,1)
    band_H = np.array(band_H['number_of_properties']).reshape(-1,1)
    
    # 8 groups are too many for analysis, thus put them into four groups, catergorized by their valuations.
    # 0 ~ 52k, approximately the houses that are around 50k, mostly small flats or less favoured housing;
    houses_above_0k = pd.DataFrame({'area_names':list(area_names),'property_counts':list((band_A+band_B).reshape(1,-1)[0])})
    # 52 ~ 88k, around 100k, low-average standard;
    houses_above_52k = pd.DataFrame({'area_names':area_names,'property_counts':list((band_C+band_D).reshape(1,-1)[0])})
    # 88k ~ 160k, from 100k to 150k, high-average standard;
    houses_above_88k = pd.DataFrame({'area_names':area_names,'property_counts':list((band_E+band_F).reshape(1,-1)[0])})
    # 160k above, above 150k, more or less luxury houses;
    houses_above_160k = pd.DataFrame({'area_names':area_names,'property_counts':list((band_G+band_H).reshape(1,-1)[0])})
    
    # Return the tables
    return houses_above_0k, houses_above_52k, houses_above_88k, houses_above_160k

def load_homeless_demographic():
    workbook = pd.ExcelFile('Data/England_HomelessData_until2020.xlsx')
    worksheet = workbook.parse(workbook.sheet_names[7])
    hl_demographic = worksheet.drop(labels=range(325,342), axis=0)
    hl_demographic = hl_demographic.drop(columns=hl_demographic.columns[range(11,60)])
    
    hl_demographic.iloc[1,[0]] = 'Code'
    hl_demographic.iloc[1,[1]] = 'Area_name'
    hl_demographic.columns = list(hl_demographic.iloc[1,:])
    hl_demographic = hl_demographic.drop(labels=range(0,16), axis=0)
    hl_demographic.index = range(0,len(hl_demographic.index))
    
    return hl_demographic

