import os
import numpy as np
import pandas as pd
import warnings

VALUE_COL_NAME = "value"
STATUS_COL_NAME = "status"
TIMESTAMP_COL_NAME = "time"
STATUS_OK = "good"
STATUS_BAD = "bad"
STATUS_NAN = "nan"


def format_timeseries(
    timeseries,
    value_col_name=None,
    timestamp_col_name=None,
    status_col_name=None,
    status_ok_value=None,
    status_bad_value=None,
):
    """Format a timeseries into a Datetimeindex Dataframe with columns for values and status

    Parameters
    ----------
    timeseries: pandas.DataFrame
        DataFrame containing at least one column with the values of the timeseries, and at best
        one column with timestamps and one column with status (often timeseries from devices
        indicate whether the measuring apparatus was working under normal conditions)
    value_col_name: str or int
        The name or index of the column holding the values of the timeseries
        Default: None
    timestamp_col_name: str or int
        The name or index of the column holding the timestamps of the timeseries
        Default: None
    status_col_name: str or int
        The name or index of the column holding the status of the timeseries
        Default: None
    status_ok_value: str
        The label associated to a good status of the measuring device
    status_bad_value: str
        The label associated to a bad status of the measuring device

    Returns
    -------
    A pandas.DataFrame with one column containing values of the timeseries, labeled VALUE_COL_NAME,
    one column with status of the values, labeled STATUS_COLUMN_NAME and index as timastamps if
    timestamp_col_name was provided.
    """

    if VALUE_COL_NAME not in timeseries.columns:
        if value_col_name in timeseries.columns:
            timeseries = timeseries.rename(columns={value_col_name: VALUE_COL_NAME})
        else:
            # The value_col_name is the column number corresponding to the value column
            if isinstance(value_col_name, int):
                timeseries[VALUE_COL_NAME] = timeseries.iloc[:, value_col_name]
            else:
                print(
                    "The timeseries as no column labeled 'value' and no "
                    "value for the argument 'value_col_name' was provided"
                )
                # no value column labeled
                # test if only one column --> assign to value
                # if two column, maybe one of them is status, or timestamps
                # if three columns, maybe one column is status and the otherwise timestamps

                # assign the first column to value by default

    if STATUS_COL_NAME not in timeseries.columns:
        if status_col_name in timeseries.columns:
            timeseries = timeseries.rename(columns={status_col_name: STATUS_COL_NAME})
        else:
            # The status_col_name is the column number corresponding to the status column
            if isinstance(status_col_name, int):
                timeseries[STATUS_COL_NAME] = timeseries.iloc[:, status_col_name]
            else:
                # create a new status column
                timeseries[STATUS_COL_NAME] = STATUS_OK
                timeseries.loc[
                    timeseries[VALUE_COL_NAME].isna(), [STATUS_COL_NAME]
                ] = STATUS_BAD

    if TIMESTAMP_COL_NAME not in timeseries.columns:
        if timestamp_col_name in timeseries.columns:
            timeseries = timeseries.rename(
                columns={timestamp_col_name: TIMESTAMP_COL_NAME}
            )
        else:
            # The timestamp_col_name is the column number corresponding to the timestamp column
            if isinstance(timestamp_col_name, int):
                timeseries[TIMESTAMP_COL_NAME] = timeseries.iloc[:, timestamp_col_name]

    if TIMESTAMP_COL_NAME in timeseries.columns:
        timeseries[TIMESTAMP_COL_NAME] = pd.to_datetime(timeseries[TIMESTAMP_COL_NAME])
        timeseries = timeseries.set_index(TIMESTAMP_COL_NAME)

    # Replace the values for STATUS_OK and STATUS_BAD
    if status_ok_value is not None:
        timeseries[STATUS_COL_NAME].replace(
            to_replace=status_ok_value, value=STATUS_OK, inplace=True
        )
    if status_bad_value is not None:
        timeseries[STATUS_COL_NAME].replace(
            to_replace=status_bad_value, value=STATUS_BAD, inplace=True
        )

    # If there were missing rows in the status column, NaN was attributed and is now replaced by STATUS_BAD
    timeseries.loc[timeseries[STATUS_COL_NAME].isna()] = STATUS_BAD

    # check that the only values in column status are labelled with STATUS_OK and STATUS_BAD
    if set(timeseries[STATUS_COL_NAME].unique()) != set([STATUS_OK, STATUS_BAD]):
        # TODO raise a warning
        print("You status column does not contain only good or bad values")

    # fmt: off
    timeseries.loc[
        (timeseries[VALUE_COL_NAME].isna())
        & (timeseries[STATUS_COL_NAME] == STATUS_OK), [STATUS_COL_NAME]
    ] = STATUS_BAD + ":" + STATUS_NAN
    # fmt: on

    return timeseries[[VALUE_COL_NAME, STATUS_COL_NAME]]


def fill_missing_timestamps(
    timeseries,
    timestep=np.timedelta64(900, "s"),
    full_year=False,
    daylight_saving_dates=(
        np.datetime64("2019-03-31T03:00:00."),
        np.datetime64("2019-10-27T02:00:00."),
    ),
):
    """

    Parameters
    ----------
    timeseries: pandas.DataFrame
        timeseries with timestamps as index, one column labeled VALUE_COL_NAME with values and the
        other one labeled STATUS_COL_NAME indicating whether the value is good or not
    timestep: numpy.timedelta64
        expected interval in s between two timestamps in the timeseries
        default: 15min, expressed in s
    full_year: bool
        if True then expect the timeseries to be on one year
    daylight_saving_dates: list of np.datetime64("YYYY-MM-DDTHH:MM:SS.")
        dates of the summer or winter time change for daylight saving
    Returns
    -------
    copy of the timeseries with inserted missing timestamps

    Notes
    -----

    One need to input the time of summer or winter time change in

    """
    timeseries = timeseries.copy()

    # how many timesteps fit within an hour
    n_timestep = np.timedelta64(1, "h") / timestep.astype("timedelta64[60s]")
    print(f"There are {len(timeseries)/n_timestep} hourly values within the timeseries")

    if full_year is True:
        n_missing_timestamps = (8760 - len(timeseries) / n_timestep) * n_timestep
        print(f"{n_missing_timestamps} timesteps are missing")

    dt = timeseries.index.to_numpy()
    # take the interval between each value of the array, if array has length N, there is N-1 intervals
    dt_diff = np.diff(dt)
    # find the indexes where the interval is not equal to exactly one timestep
    idx = np.where(dt_diff != timestep)[0]
    # add one to match the indexes of dt
    idx = idx + 1
    # to keep track of how many timestamps we added
    n_inserted_timestamps = 0

    for i in idx:
        print(dt[i - 1 : i + 1])
        # each interval should be in unit of timestep. For timestep=15 min, if the interval is 30 min = 2 * 15 min --> there is one timestamp missing
        t_interval = dt[i] - dt[i - 1]
        n_interval_missing = int(t_interval / timestep - 1)
        n_inserted_timestamps = n_inserted_timestamps + n_interval_missing

        if dt[i] in daylight_saving_dates:
            print(
                f"--> Summer or Winter time change: {n_interval_missing} interval(s) missing"
            )
        else:
            # compute the value for the missing interval as average of value just before and just after provided their status is flagged as STATUS_OK
            # if only one value is STATUS_OK take this one, if none of them are STATUS_OK raise an error
            mean_val = 0
            n_val = 0
            if timeseries[STATUS_COL_NAME].iloc[i - 1] == STATUS_OK:
                mean_val = mean_val + timeseries[VALUE_COL_NAME].iloc[i - 1]
                n_val = n_val + 1
            if timeseries[STATUS_COL_NAME].iloc[i + 1] == STATUS_OK:
                mean_val = mean_val + timeseries[VALUE_COL_NAME].iloc[i + 1]
                n_val = n_val + 1
            if n_val == 0:
                warnings.warn(
                    f"The status before or after the missing timestamp {dt[i]} is not '{STATUS_OK}'"
                )
                mean_val = np.nan
            else:
                mean_val = mean_val / n_val

            if n_interval_missing >= 1:
                print(f"--> {n_interval_missing} interval(s) missing")
                # construct a DatetimeIndex starting from the timestamp just before + timestep, with period timestep and of length equal to the number of missing timesteps
                new_dtidx = pd.date_range(
                    start=dt[i - 1] + timestep, periods=n_interval_missing, freq="15T"
                )
                new_timestamps = pd.DataFrame(
                    [[mean_val, "Replaced"] for i in range(n_interval_missing)],
                    columns=timeseries.columns,
                ).set_index(new_dtidx)
                timeseries = timeseries.append(
                    new_timestamps, ignore_index=False, verify_integrity=False
                )
                print(
                    f"filled {n_interval_missing} intervals with mean value taken from average between previous and next values close to the missing interval"
                )
            else:
                warnings.warn(
                    f"The timestamp {dt[i]} is likely corresponding to the change to winter time of this year please add this date to the daylight_saving_dates argument, type `help(fill_missing_timestamps)` for formatting info"
                )

    if full_year is True and n_inserted_timestamps != n_missing_timestamps:
        warnings.warn(
            f"{n_missing_timestamps} timestamps were missing to have 8760 hourly values and {n_inserted_timestamps} timestamp were inserted.\n If the difference is one timestep it could be due mismatch between winter and summer daylight savings"
        )

    timeseries = timeseries.sort_index()
    # create a datetimeindex with the expected frequence as it is hard to assign a freq to an existing datatimeindex object which has it to None
    datetime_index = pd.date_range(
        start=timeseries.index[0], freq=f"{60/n_timestep}min", periods=len(timeseries)
    )

    return timeseries.set_index(datetime_index)


def prepare_wind_data(
    timeseries, output_fname=None, full_year=True, installed_cap=3000
):
    timeseries = timeseries.copy()
    # Select only the relevant columns from the spreadsheet
    timeseries = format_timeseries(
        timeseries,
        value_col_name="Wert",
        timestamp_col_name=0,
        status_col_name="Status",
        status_ok_value="Gut",
        status_bad_value="Gestört",
    )

    # Select only values for 2019
    timeseries = timeseries.loc[timeseries.index < "2020-01-01 00:00:00"]
    # Fill the missing timestamps
    timeseries = fill_missing_timestamps(
        timeseries,
        full_year=full_year,
        daylight_saving_dates=(
            np.datetime64("2019-03-31T03:00:00."),
            np.datetime64("2019-10-27T02:00:00."),
        ),
    )

    if output_fname is None:
        output_fname = "timeseries_wind.csv"

    # Set the value to 0 where the the status is not good
    # timeseries.loc[timeseries.Status == 'Gestört', "Wert"] = 0
    # max_val = timeseries.Wert.resample("H").mean().max()
    # resampled_timeseries = timeseries.copy()

    # resampled_timeseries["Wert"] = resampled_timeseries["Wert"] / installed_cap
    # resampled_timeseries.Wert.resample("H").mean().to_csv(output_fname, index=False)
    timeseries.to_csv(output_fname)
    return timeseries


def resample_feedin(
    simulated_timeseries, start_timestamp, timestep=np.timedelta64(900, "s"), duration=1
):
    """Resample a feedin timeseries to a given period

    Parameters
    ----------
    simulated_timeseries: pandas.DataFrame
        timeseries of simulated feedin profile (i.e. for wind or PV production)
    start_timestamp: timestamp or str
        the starting time of the timeseries in ISO format YYYY-MM-DDTHH:MM:SS
    timestep: numpy.timedelta64
        the timestep between two values of the timeseries
    duration: float
        duration of the timeseries in unit of years
    Returns
    -------
    up or down sampled timeseries
    """

    # Determines the frequency of the timeseries based on the number of occurences
    freq = (60 * 8760 * duration) / len(simulated_timeseries)

    # Assign a datetime index to the timeseries
    datetime_index = pd.date_range(
        start=start_timestamp, freq=f"{freq}min", periods=len(simulated_timeseries)
    )
    sim_df = simulated_timeseries.set_index(datetime_index)

    # Determines how many timesteps fit in one hour and resample the timeseries
    n_timestep = int(np.timedelta64(1, "h") / timestep.astype("timedelta64[60s]"))

    if 60 / n_timestep < freq:
        # Upsamples the timeseries and assign new timestamps with value of the earlier timestamp or the lower temporal resolution
        sim_df_resampled = pd.DataFrame(
            sim_df[VALUE_COL_NAME].resample(f"{60/n_timestep}T").pad()
        )
        new_dtidx = pd.date_range(
            start=sim_df_resampled.index[-1] + timestep,
            periods=n_timestep - 1,
            freq=f"{60/n_timestep}T",
        )
        new_timestamps = pd.DataFrame(
            [[sim_df_resampled[VALUE_COL_NAME][-1]] for i in range(n_timestep - 1)],
            columns=sim_df_resampled.columns,
        ).set_index(new_dtidx)
        answer = sim_df_resampled.append(
            new_timestamps, ignore_index=False, verify_integrity=False
        )
    elif 60 / n_timestep == freq:
        answer = sim_df
    else:
        # Downsample the time and replace the value by the mean of the values at higher temporal resolution
        answer = pd.DataFrame(
            sim_df[VALUE_COL_NAME].resample(f"{60/n_timestep}T").mean()
        )

    return answer
