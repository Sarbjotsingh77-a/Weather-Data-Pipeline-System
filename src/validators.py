def validate_temperature(temp):
    """
    Validate temperature range
    """

    try:

        temp = float(temp)

        if -50 <= temp <= 60:
            return True

        return False

    except:
        return False


def validate_humidity(humidity):
    """
    Validate humidity
    """

    try:

        humidity = int(humidity)

        if 0 <= humidity <= 100:
            return True

        return False

    except:
        return False


def validate_pressure(pressure):
    """
    Validate pressure
    """

    try:

        pressure = float(pressure)

        if 800 <= pressure <= 1200:
            return True

        return False

    except:
        return False


def validate_wind_speed(speed):
    """
    Validate wind speed
    """

    try:

        speed = float(speed)

        if 0 <= speed <= 150:
            return True

        return False

    except:
        return False


def validate_weather_record(record):
    """
    Complete weather record validation
    """

    if record is None:
        return False

    return (
        validate_temperature(
            record["temperature"]
        )
        and
        validate_humidity(
            record["humidity"]
        )
        and
        validate_pressure(
            record["pressure"]
        )
        and
        validate_wind_speed(
            record["wind_speed"]
        )
    )
