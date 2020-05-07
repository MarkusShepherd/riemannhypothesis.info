from datetime import date
from dateutil.rrule import DAILY, rrule
from sympy import isprime


def is_prime_date(date, date_format):
    date_str = date.strftime(date_format)
    date_int = int(date_str)
    return isprime(date_int)


def count_prime_dates(start, end, date_format):
    dates_total = 0
    dates_prime = 0

    for date in rrule(DAILY, dtstart=start, until=end):
        dates_total += 1
        dates_prime += is_prime_date(date, date_format)

    return dates_total, dates_prime


start = date(2000, 1, 1)
end = date(2399, 12, 31)
reference = date(1707, 4, 15)
reference_str = "Euler's birthday"

date_formats = (
    "%d%m",
    "%m%d",
    "%d%m%y",
    "%m%d%y",
    "%d%m%Y",
    "%m%d%Y",
    "%y%m%d",
    "%Y%m%d",
)

for date_format in date_formats:
    print(
        f"* Format: `{date_format}` "
        + f"({reference_str}: {reference.strftime(date_format)} "
        + ("👍" if is_prime_date(reference, date_format) else "👎")
        + ") \\"
    )
    total, primes = count_prime_dates(start, end, date_format)
    print(
        f"  {100 * primes / total:.1f}% of dates are primes in this format! "
        + f"({primes} out of {total})"
    )
