import pandas as pd

df = pd.read_csv('covid-data.csv')

df.drop(["iso_code", "continent", "date", "excess_mortality_cumulative_per_million", "excess_mortality",
         "excess_mortality_cumulative", "excess_mortality_cumulative_absolute",
         "human_development_index", "life_expectancy", "hospital_beds_per_thousand",
         "handwashing_facilities", "male_smokers", "female_smokers",
         "diabetes_prevalence", "cardiovasc_death_rate", "extreme_poverty",
         "median_age", "population_density", "population", "stringency_index",
         "new_people_vaccinated_smoothed_per_hundred", "new_vaccinations_smoothed_per_million",
         "total_boosters_per_hundred", "people_fully_vaccinated_per_hundred",
         "people_vaccinated_per_hundred", "total_vaccinations_per_hundred",
         "tests_units", "tests_per_case", "new_tests_smoothed_per_thousand",
         "new_tests_per_thousand", "total_tests_per_thousand", "new_tests",
         "weekly_hosp_admissions_per_million", "weekly_icu_admissions_per_million",
         "hosp_patients_per_million", "icu_patients_per_million", "reproduction_rate",
         "new_deaths_smoothed_per_million", "new_deaths_per_million",
         "total_deaths_per_million", "new_cases_smoothed_per_million",
         "new_cases_per_million", "total_cases_per_million"], axis=1, inplace=True)



# to show the length of the data set
print(len(df))

# to show the dimensions of the pandas dataset
print(df.shape)


# to show the first 6 lines of the pandas dataset
print(df.head)

print(df.isnull().sum().sum())



print(df.isnull().sum().sum())

df = df.fillna(0)

print(df.keys())

prueba = df.loc[df['location'] == 'Spain']
print(prueba)
