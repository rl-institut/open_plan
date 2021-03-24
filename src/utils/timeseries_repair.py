import numpy as np
import pandas as pd
import warnings


def fill_missing_timestamps(timeseries, timestep=np.timedelta64(900, 's'), full_year=False,
                            daylight_saving_dates=(np.datetime64("2019-03-31T03:00:00."),
                                                   np.datetime64("2019-10-27T02:00:00."))):
    """

    Parameters
    ----------
    timeseries: pandas.DataFrame
        timeseries with timestamps as index, one column labeled "Wert" with values and the other one labeled "Status" indicating whether the value is good or not
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

    # how many timesteps fit witin an hour
    n_timestep = np.timedelta64(1, 'h') / timestep.astype('timedelta64[60s]')
    print(f"There are {len(timeseries) / n_timestep} hourly values within the timeseries")

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
        # each interval should be in unit of timestep. For timestep=15 min, if the interval is 30 min = 2 * 15 min --> there is one timestamp missing
        t_interval = dt[i] - dt[i - 1]
        n_interval_missing = int(t_interval / timestep - 1)
        n_inserted_timestamps = n_inserted_timestamps + n_interval_missing

        if dt[i] in daylight_saving_dates:
            print(f"--> Summer or Winter time change: {n_interval_missing} interval(s) missing")
        else:
            # compute the value for the missing interval as average of value just before and just after provided their status is flagged as "Gut"
            # if only one value is "Gut" take this one, if none of them are "Gut" raise an error
            mean_val = 0
            n_val = 0
            if timeseries.Status.iloc[i - 1] == "Gut":
                mean_val = mean_val + timeseries.Wert.iloc[i - 1]
                n_val = n_val + 1
            if timeseries.Status.iloc[i + 1] == "Gut":
                mean_val = mean_val + timeseries.Wert.iloc[i + 1]
                n_val = n_val + 1
            if n_val == 0:
                warnings.warn(
                    f"The status before or after the missing timestamp {dt[i]} is not 'Gut'")
                mean_val = np.nan
            else:
                mean_val = mean_val / n_val

            if n_interval_missing >= 1:
                print(f"--> {n_interval_missing} interval(s) missing")
                # construct a DatetimeIndex starting from the timestamp just before + timestep, with period timestep and of length equal to the number of missing timesteps
                new_dtidx = pd.date_range(start=dt[i - 1] + timestep, periods=n_interval_missing,
                                          freq="15T")
                new_timestamps = pd.DataFrame(
                    [[mean_val, "Replaced"] for i in range(n_interval_missing)],
                    columns=timeseries.columns).set_index(new_dtidx)
                timeseries = timeseries.append(new_timestamps, ignore_index=False,
                                               verify_integrity=False)
                print(
                    f"filled {n_interval_missing} intervals with mean value taken from average between previous and next values close to the missing interval")
            else:
                warnings.warn(f"The timestamp {dt[i]} is likely corresponding to the change to winter time of this year please add this date to the daylight_saving_dates argument, type `help(fill_missing_timestamps)` for formatting info")

    if full_year is True and n_inserted_timestamps != n_missing_timestamps:
        warnings.warn(
            f"{n_missing_timestamps} timestamps were missing to have 8760 hourly values and {n_inserted_timestamps} timestamp were inserted.\n If the difference is one timestep it could be due mismatch between winter and summer daylight savings")

    timeseries = timeseries.sort_index()
    # create a datetimeindex with the expected frequence as it is hard to assign a freq to an existing datatimeindex object which has it to None
    datetime_index = pd.date_range(start=timeseries.index[0], freq=f'{60 / n_timestep}min',
                                   periods=len(timeseries))

    return timeseries.set_index(datetime_index)


def prepare_wind_data(timeseries, output_fname=None, full_year=True, installed_cap=3000):
    timeseries = timeseries.copy()
    # Select only the relevant columns from the spreadsheet
    timeseries = timeseries[["Unnamed: 0", "Wert", "Status"]].rename(
        columns={"Unnamed: 0": "Timestamp"}).set_index("Timestamp")
    # Select only values for 2019
    timeseries = timeseries.loc[timeseries.index < "2020-01-01 00:00:00"]
    # Fill the missing timestamps
    timeseries = fill_missing_timestamps(timeseries, full_year=full_year, daylight_saving_dates=(
    np.datetime64("2019-03-31T03:00:00."), np.datetime64("2019-10-27T02:00:00.")))

    if output_fname is None:
        output_fname = "timeseries_wind.csv"

    timeseries.loc[timeseries.Status == 'Gestört', "Wert"] = 0
    max_val = timeseries.Wert.resample("H").mean().max()
    print(max_val)
    resampled_timeseries = timeseries.copy()

    resampled_timeseries["Wert"] = resampled_timeseries["Wert"] / installed_cap
    resampled_timeseries.Wert.resample("H").mean().to_csv(output_fname, index=False)
    # timeseries.to_csv(output_fname)
    return timeseries


def repair_timeseries():
    df = karholz_min.copy()

    timeseries = df.loc[df.Status == 'Gestört'].copy()
    timestep = np.timedelta64(900, 's')
    dt = timeseries.index.to_numpy()
    # take the interval between each value of the array, if array has length N, there is N-1 intervals
    dt_diff = np.diff(dt)
    # find the indexes where the interval is not equal to exactly one timestep
    idx = np.where(dt_diff != timestep)[0]
    dt_diff[idx]

    # The very first element is a start of troubled interval, so we append it
    idx = np.append([-1], idx)

    error_interval = []

    for i in range(0, len(idx) - 1, 1):
        # build an interval with timestamps at beginning and end of a troubled interval
        tstart = dt[idx[i] + 1]
        tstop = timestep + dt[idx[i + 1]]
        interv = pd.Interval(pd.Timestamp(tstart), pd.Timestamp(tstop), closed="both")

        # for interval less than 5 hours
        if interv.length < np.timedelta64(5, 'h'):
            # compute mean value based on value before and after the interval
            val_before = df.loc[pd.Timestamp(tstart - timestep), "Wert"]
            val_after = df.loc[pd.Timestamp(tstop + timestep), "Wert"]
            mean_val = (val_before + val_after) / 2
            timeseries.loc[interv.left:interv.right, "Wert"] = mean_val
            timeseries.loc[interv.left:interv.right, "Status"] = "Gut/interpolated"

        else:
            # find a patch in the previous days to replace the troubled values
            no_fit_interval = True
            n = 0
            while no_fit_interval:
                val_before = df.loc[pd.Timestamp(tstart - (n + 1) * interv.length):pd.Timestamp(
                    tstart - n * interv.length - timestep)]

                no_fit_interval = not (len(
                    val_before.Status.unique()) == 1 and "Gut" in val_before.Status.unique())  # ,  val_before.Status.unique()
                n = n + 1

            assert len(val_before.Status.unique()) == 1 and "Gut" in val_before.Status.unique()
            timeseries.loc[interv.left:interv.right, "Wert"] = val_before.Wert.values
            timeseries.loc[interv.left:interv.right, "Status"] = "Gut/pasted"
        error_interval.append(interv)

    error_interval