import filecmp
import pathlib
from typing import Union
import pandas as pd


def concat_data(
        path: Union[str, pathlib.Path],
):
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)

    full_data = []

    for file in path.iterdir():
        data = pd.read_csv(file)
        same_day = pd.to_datetime(data['created']).dt.date == pd.to_datetime(data['applicable_date']).dt.date
        full_data.append(data[same_day])

    full_data = pd.concat(full_data)

    data_to_save = pd.DataFrame(full_data, columns=['created', 'min_temp', 'the_temp', 'max_temp', 'air_pressure', 'humidity', 'visibility', 'wind_direction_compass', 'wind_direction', 'wind_speed'])
    data_to_save.rename({'the_temp': 'temp'}, inplace=True, axis='columns')
    data_to_save['created'] = data_to_save['created'].apply(lambda x: x[0:16])
    data_to_save.sort_values('created', inplace=True)
    data_to_save.to_csv(f'{path}.csv', index=False)


if __name__ == '__main__':
    concat_data('weather_data/523920_2017_03')
    assert filecmp.cmp(
        'expected_523920_2017_03.csv',
        'weather_data/523920_2017_03.csv'
    )
